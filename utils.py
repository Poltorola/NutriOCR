import base64
import json
import logging
import os
import time
from contextlib import contextmanager
from io import BytesIO
from pathlib import Path

import cv2
import numpy as np
import requests
from PIL import Image, ImageOps
from dotenv import load_dotenv
from tqdm import tqdm


PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}
PROCESSING_ATTEMPTS = 2

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL", "http://172.19.48.1:11434"
).rstrip("/")
LLAMA_CPP_BASE_URL = os.getenv(
    "LLAMA_CPP_BASE_URL", "http://172.19.48.1:11435"
).rstrip("/")
LOCAL_MODEL_REQUEST_TIMEOUT = float(
    os.getenv("LOCAL_MODEL_REQUEST_TIMEOUT", "900")
)


class _PaddleRoutineMessageFilter(logging.Filter):
    HIDDEN_MESSAGES = (
        "Connectivity check to the model hoster has been skipped",
        "Creating model:",
        "Model files already exist. Using cached files.",
        "Special tokens have been added in the vocabulary",
        "Loading configuration file",
        "Loading weights file",
        "Loaded weights file from disk",
        "All model checkpoint weights were used",
        "All the weights of",
        "If your task is similar to the task the model of the checkpoint",
    )

    def filter(self, record):
        message = record.getMessage()
        return not any(text in message for text in self.HIDDEN_MESSAGES)


logging.getLogger("paddlex").addFilter(_PaddleRoutineMessageFilter())

# Supported values: "paddle", "custom", "none".
ROTATION_METHOD = "paddle"

NUTRITION_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "recognized_text": {"type": "string"},
        "product_name": {"type": ["string", "null"]},
        "company_name": {"type": ["string", "null"]},
        "barcode": {"type": ["string", "null"]},
        "net_weight_g": {"type": ["number", "null"]},
        "volume_ml": {"type": ["number", "null"]},
        "nutrition": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "kcal": {"type": ["number", "null"]},
                "protein_g": {"type": ["number", "null"]},
                "fat_g": {"type": ["number", "null"]},
                "saturated_fat_g": {"type": ["number", "null"]},
                "carbs_g": {"type": ["number", "null"]},
                "sugars_g": {"type": ["number", "null"]},
                "fiber_g": {"type": ["number", "null"]},
                "salt_g": {"type": ["number", "null"]},
            },
            "required": [
                "kcal",
                "protein_g",
                "fat_g",
                "saturated_fat_g",
                "carbs_g",
                "sugars_g",
                "fiber_g",
                "salt_g",
            ],
        },
    },
    "required": [
        "recognized_text",
        "product_name",
        "company_name",
        "barcode",
        "net_weight_g",
        "volume_ml",
        "nutrition",
    ],
}


_paddle_orientation_pipeline = None


def measure_runtime(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    return result, time.perf_counter() - start


def parse_json_response(content, source="Model"):
    if not isinstance(content, str) or not content.strip():
        raise ValueError(f"{source} returned an empty response.")

    try:
        return json.loads(content)
    except json.JSONDecodeError as error:
        preview = content.strip()[:500]
        raise ValueError(
            f"{source} returned invalid JSON at line {error.lineno}, "
            f"column {error.colno}: {error.msg}. "
            f"Response preview: {preview!r}"
        ) from error


def _request_json(method, url, **kwargs):
    try:
        response = requests.request(
            method,
            url,
            timeout=kwargs.pop("timeout", 15),
            **kwargs,
        )
    except requests.RequestException as error:
        raise RuntimeError(f"Could not connect to {url}: {error}") from error

    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        raise RuntimeError(
            f"HTTP {response.status_code} from {url}: {response.text[:1000]!r}"
        ) from error

    if not response.content:
        return {}
    try:
        return response.json()
    except requests.JSONDecodeError as error:
        raise RuntimeError(
            f"Invalid JSON from {url}: {response.text[:1000]!r}"
        ) from error


def _ollama_loaded_models(base_url):
    data = _request_json("GET", f"{base_url}/api/ps")
    return [item.get("name") or item.get("model") for item in data.get("models", [])]


def _llama_cpp_model_states(base_url):
    """Return [(model_id, state)] for router mode, or a single server state."""
    try:
        data = _request_json("GET", f"{base_url}/models")
    except RuntimeError:
        data = None

    if isinstance(data, dict) and isinstance(data.get("data"), list):
        states = []
        for item in data["data"]:
            status = item.get("status", {})
            state = status.get("value") if isinstance(status, dict) else status
            states.append((item.get("id"), state or "unknown"))
        return states

    props = _request_json("GET", f"{base_url}/props")
    state = "sleeping" if props.get("is_sleeping") else "loaded"
    return [(props.get("model_path") or "llama.cpp model", state)]


def ensure_no_local_model_loaded(provider, base_url=None):
    """Fail before a test rather than competing with a model already in VRAM."""
    if provider == "ollama":
        base_url = (base_url or OLLAMA_BASE_URL).rstrip("/")
        loaded = [name for name in _ollama_loaded_models(base_url) if name]
    elif provider == "llama_cpp":
        base_url = (base_url or LLAMA_CPP_BASE_URL).rstrip("/")
        loaded = [
            model_id
            for model_id, state in _llama_cpp_model_states(base_url)
            if state not in {"unloaded", "sleeping"}
        ]
    else:
        raise ValueError(f"Unknown local model provider: {provider}")

    if loaded:
        raise RuntimeError(
            f"Cannot start {provider} test: local model already loaded: "
            f"{', '.join(loaded)}"
        )


def unload_local_model(provider, model, base_url=None):
    """Unload model memory while keeping the model server alive."""
    if provider == "ollama":
        base_url = (base_url or OLLAMA_BASE_URL).rstrip("/")
        _request_json(
            "POST",
            f"{base_url}/api/generate",
            json={"model": model, "keep_alive": 0},
            timeout=60,
        )
        return

    if provider == "llama_cpp":
        base_url = (base_url or LLAMA_CPP_BASE_URL).rstrip("/")
        try:
            _request_json(
                "POST",
                f"{base_url}/models/unload",
                json={"model": model},
                timeout=60,
            )
        except RuntimeError as error:
            raise RuntimeError(
                "llama-server could not unload the model immediately. Start it "
                "in router mode (without --model, using --models-dir or "
                "--models-preset); single-model mode can only unload through "
                "--sleep-idle-seconds."
            ) from error
        return

    raise ValueError(f"Unknown local model provider: {provider}")


@contextmanager
def local_model_session(provider, model, base_url=None):
    ensure_no_local_model_loaded(provider, base_url=base_url)
    try:
        yield
    finally:
        unload_local_model(provider, model, base_url=base_url)


def _ollama_vision_json(prompt, image_b64, model, schema, context_length, base_url):
    request_data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt, "images": [image_b64]}],
        "format": schema,
        "options": {"temperature": 0, "num_ctx": context_length},
        "stream": True,
    }
    if model.startswith("gemma4:"):
        request_data["think"] = False

    response = requests.post(
        f"{base_url}/api/chat",
        json=request_data,
        stream=True,
        timeout=LOCAL_MODEL_REQUEST_TIMEOUT,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        raise RuntimeError(
            f"Ollama HTTP {response.status_code}: {response.text[:500]!r}"
        ) from error

    response_parts = []
    thinking_chars = 0
    done_received = False
    done_reason = None
    metadata = {}
    for raw_line in response.iter_lines():
        if not raw_line:
            continue
        try:
            line = raw_line.decode("utf-8")
        except UnicodeDecodeError as error:
            raise RuntimeError(
                f"Ollama returned a non-UTF-8 streaming event: "
                f"{raw_line[:200]!r}"
            ) from error
        try:
            data = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(
                f"Ollama returned an invalid streaming event: {line[:500]!r}"
            ) from error
        if data.get("error"):
            raise RuntimeError(f"Ollama error: {data['error']}")

        message = data.get("message", {})
        response_parts.append(message.get("content", ""))
        thinking_chars += len(message.get("thinking", ""))
        if data.get("done"):
            done_received = True
            done_reason = data.get("done_reason")
            metadata = {
                "prompt_tokens": data.get("prompt_eval_count", 0),
                "output_tokens": data.get("eval_count", 0),
            }

    source = (
        f"Ollama model {model} (done_received={done_received}, "
        f"done_reason={done_reason!r}, thinking_chars={thinking_chars})"
    )
    return parse_json_response("".join(response_parts), source=source), metadata


def _llama_cpp_vision_json(prompt, image_b64, model, schema, base_url):
    request_data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"},
                    },
                ],
            }
        ],
        "temperature": 0,
        "stream": True,
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "nutrition_label",
                "strict": True,
                "schema": schema,
            },
        },
    }
    response = requests.post(
        f"{base_url}/v1/chat/completions",
        json=request_data,
        stream=True,
        timeout=LOCAL_MODEL_REQUEST_TIMEOUT,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        raise RuntimeError(
            f"llama-server HTTP {response.status_code}: {response.text[:1000]!r}"
        ) from error

    response_parts = []
    finish_reason = None
    usage = {}
    for raw_line in response.iter_lines():
        if not raw_line:
            continue
        try:
            line = raw_line.decode("utf-8")
        except UnicodeDecodeError as error:
            raise RuntimeError(
                f"llama-server returned a non-UTF-8 SSE event: "
                f"{raw_line[:200]!r}"
            ) from error
        if line.startswith(":"):
            continue
        if line.startswith("data:"):
            line = line[5:].strip()
        if line == "[DONE]":
            break
        try:
            data = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(
                f"llama-server returned an invalid SSE event: {line[:500]!r}"
            ) from error
        if data.get("error"):
            raise RuntimeError(f"llama-server error: {data['error']}")
        for choice in data.get("choices", []):
            response_parts.append(choice.get("delta", {}).get("content") or "")
            finish_reason = choice.get("finish_reason") or finish_reason
        usage = data.get("usage") or usage

    metadata = {
        "prompt_tokens": usage.get("prompt_tokens", 0),
        "output_tokens": usage.get("completion_tokens", 0),
    }
    source = f"llama-server model {model} (finish_reason={finish_reason!r})"
    return parse_json_response("".join(response_parts), source=source), metadata


def infer_local_vision_json(
    *, prompt, image_b64, provider, model, schema, context_length=16_384,
    base_url=None,
):
    """Common local vision inference entry point for Ollama and llama.cpp."""
    if provider == "ollama":
        return _ollama_vision_json(
            prompt,
            image_b64,
            model,
            schema,
            context_length,
            (base_url or OLLAMA_BASE_URL).rstrip("/"),
        )
    if provider == "llama_cpp":
        return _llama_cpp_vision_json(
            prompt,
            image_b64,
            model,
            schema,
            (base_url or LLAMA_CPP_BASE_URL).rstrip("/"),
        )
    raise ValueError(f"Unknown local model provider: {provider}")


def format_exception_chain(error):
    parts = []
    seen = set()
    current = error

    while current is not None and id(current) not in seen:
        seen.add(id(current))
        message = str(current).strip()
        part = type(current).__name__
        if message:
            part += f": {message}"
        parts.append(part)
        current = current.__cause__ or current.__context__

    return " <- ".join(parts)


def exception_request_id(error):
    seen = set()
    current = error

    while current is not None and id(current) not in seen:
        seen.add(id(current))

        for attribute in ("request_id", "_request_id"):
            request_id = getattr(current, attribute, None)
            if request_id:
                return request_id

        response = getattr(current, "response", None)
        headers = getattr(response, "headers", None)
        if headers:
            request_id = headers.get("x-request-id")
            if request_id:
                return request_id

        current = current.__cause__ or current.__context__

    return None


def rotate_image(image, degrees):
    if degrees == 90:
        return image.rotate(-90, expand=True)
    if degrees == 180:
        return image.rotate(180, expand=True)
    if degrees == 270:
        return image.rotate(90, expand=True)
    return image


def horizontal_text_score(image):
    cv_image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
    height, width = cv_image.shape[:2]
    scale = 1000 / max(height, width)
    if scale < 1:
        cv_image = cv2.resize(
            cv_image,
            (int(width * scale), int(height * scale)),
        )

    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        31,
        15,
    )
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 3))
    closed = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(
        closed,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    score = 0
    image_area = gray.size
    for contour in contours:
        _, _, box_width, box_height = cv2.boundingRect(contour)
        box_area = box_width * box_height
        if box_area < 100 or box_area > image_area * 0.1:
            continue
        if box_width < 8 or box_height < 5:
            continue

        aspect_ratio = box_width / box_height
        if aspect_ratio > 1.5:
            score += box_area * min(aspect_ratio, 8)

    return score


def custom_auto_orient_image(image):
    scored_variants = []
    for degrees in (0, 90, 180, 270):
        variant = rotate_image(image, degrees)
        score = horizontal_text_score(variant)
        scored_variants.append((score, degrees, variant))

    scored_variants.sort(key=lambda item: item[0], reverse=True)
    best_score, _, best_image = scored_variants[0]
    original_score = next(
        score for score, degrees, _ in scored_variants if degrees == 0
    )

    if best_score > original_score * 1.5:
        return best_image
    return image


def _get_paddle_orientation_pipeline():
    global _paddle_orientation_pipeline

    if _paddle_orientation_pipeline is None:
        from paddleocr import DocPreprocessor

        _paddle_orientation_pipeline = DocPreprocessor(
            use_doc_orientation_classify=True,
            use_doc_unwarping=False,
        )

    return _paddle_orientation_pipeline


def paddle_auto_orient_image(image):
    pipeline = _get_paddle_orientation_pipeline()
    result = pipeline.predict(np.asarray(image))[0]
    output_rgb = result["output_img"][:, :, ::-1]
    return Image.fromarray(output_rgb).convert("RGB")


def auto_orient_image(image, method=None):
    method = ROTATION_METHOD if method is None else method

    if method == "paddle":
        return paddle_auto_orient_image(image)
    if method == "custom":
        return custom_auto_orient_image(image)
    if method == "none":
        return image

    raise ValueError(
        f"Unknown rotation method: {method}. "
        "Expected 'paddle', 'custom' or 'none'."
    )


def prepare_image(image_path, rotation_method=None):
    with Image.open(image_path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image = auto_orient_image(image, method=rotation_method)
        return image.copy()


def image_to_jpeg_bytes(image, quality=90):
    buffer = BytesIO()
    image.save(buffer, format="JPEG", quality=quality)
    return buffer.getvalue()


def encode_image_base64(image, quality=90):
    image_bytes = image_to_jpeg_bytes(image, quality=quality)
    return base64.b64encode(image_bytes).decode("utf-8")


def iter_image_paths(input_dir):
    input_dir = Path(input_dir)
    return [
        path
        for path in sorted(input_dir.iterdir())
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    ]


def save_json_result(result, image_path, output_dir):
    output_file = Path(output_dir) / f"{image_path.stem}.json"
    output_file.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_file


def write_timing_report(scores_file, model_name, timing_results):
    scores_file = Path(scores_file)
    scores_file.parent.mkdir(parents=True, exist_ok=True)

    lines = ["", "", f"# Model timing: {model_name}", ""]
    for image_name, metrics in timing_results.items():
        metric_parts = [f"{metrics['elapsed']:.2f} seconds"]
        metric_parts.extend(
            f"{name.replace('_', ' ')}: {value}"
            for name, value in metrics.items()
            if name != "elapsed"
        )
        lines.append(f"{image_name}: {', '.join(metric_parts)}")

    if timing_results:
        total_time = sum(data["elapsed"] for data in timing_results.values())
        average_time = total_time / len(timing_results)
        lines.extend(
            [
                "",
                f"Average runtime: **{average_time:.2f}** sec",
                f"Total runtime: **{total_time:.2f}** sec",
            ]
        )

    with scores_file.open("a", encoding="utf-8") as file:
        file.write("\n".join(lines))


def run_batch(
    process_image,
    save_result,
    input_dir,
    output_dir,
    model_name,
    scores_file,
):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    timing_results = {}

    image_paths = iter_image_paths(input_dir)
    progress = tqdm(
        image_paths,
        desc=model_name,
        unit="image",
        dynamic_ncols=True,
    )

    for image_number, image_path in enumerate(progress, start=1):
        tqdm.write(
            f"[{model_name}] Processing {image_path.name} "
            f"({image_number}/{len(image_paths)})..."
        )
        result = None
        metadata = {}
        last_error = None
        elapsed = 0.0
        completed_attempts = 0
        attempt_durations = []

        for attempt in range(1, PROCESSING_ATTEMPTS + 1):
            completed_attempts = attempt
            started_at = time.perf_counter()
            try:
                result, metadata = process_image(image_path)
                attempt_elapsed = time.perf_counter() - started_at
                attempt_durations.append(round(attempt_elapsed, 3))
                elapsed += attempt_elapsed
                last_error = None
                if attempt > 1:
                    tqdm.write(
                        f"Retry succeeded for {image_path.name} in "
                        f"{attempt_elapsed:.2f} seconds "
                        f"({elapsed:.2f} seconds total)."
                    )
                break
            except Exception as error:
                attempt_elapsed = time.perf_counter() - started_at
                attempt_durations.append(round(attempt_elapsed, 3))
                elapsed += attempt_elapsed
                last_error = error
                error_text = format_exception_chain(error)
                tqdm.write(
                    f"Failed {image_path.name} "
                    f"(attempt {attempt}/{PROCESSING_ATTEMPTS}, "
                    f"{attempt_elapsed:.2f} seconds; "
                    f"{elapsed:.2f} seconds total): {error_text}"
                )
                if attempt < PROCESSING_ATTEMPTS:
                    tqdm.write(f"Retrying {image_path.name}...")

        if last_error is not None:
            error_text = format_exception_chain(last_error)
            request_id = exception_request_id(last_error)
            result = {
                "image": image_path.name,
                "model": model_name,
                "processing_time_seconds": round(elapsed, 3),
                "processing_attempts": completed_attempts,
                "processing_attempt_durations_seconds": attempt_durations,
                "openai_request_id": request_id,
                "error": error_text,
            }
            metadata = {
                "status": "failed",
                "openai_request_id": request_id,
                "error": error_text,
            }
            tqdm.write(
                f"Giving up on {image_path.name}; saving the error result."
            )
        elif isinstance(result, dict):
            result.setdefault("image", image_path.name)
            result.setdefault("model", model_name)
            result["processing_time_seconds"] = round(elapsed, 3)
            result["processing_attempts"] = completed_attempts
            result["processing_attempt_durations_seconds"] = attempt_durations
            if metadata:
                result["processing_metadata"] = metadata

        try:
            save_result(result, image_path, output_dir)
        except Exception as error:
            tqdm.write(
                f"Could not save {image_path.name}: "
                f"{format_exception_chain(error)}"
            )
            continue

        timing_results[image_path.name] = {
            "elapsed": elapsed,
            **metadata,
        }
        if last_error is None:
            tqdm.write(
                f"[{model_name}] Processed {image_path.name}: "
                f"{elapsed:.2f} seconds"
            )

    write_timing_report(scores_file, model_name, timing_results)
    return timing_results
