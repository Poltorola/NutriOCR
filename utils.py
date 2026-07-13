import base64
import json
import time
from io import BytesIO
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageOps
from tqdm import tqdm


PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}

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

    for image_path in tqdm(iter_image_paths(input_dir)):
        try:
            (result, metadata), elapsed = measure_runtime(
                process_image,
                image_path,
            )

            if isinstance(result, dict):
                result.setdefault("image", image_path.name)
                result.setdefault("model", model_name)

            save_result(result, image_path, output_dir)
            timing_results[image_path.name] = {
                "elapsed": elapsed,
                **metadata,
            }
            print(f"Processed {image_path.name}: {elapsed:.2f} seconds")
        except Exception as error:
            print(f"Failed: {image_path.name}: {error}")

    write_timing_report(scores_file, model_name, timing_results)
    return timing_results
