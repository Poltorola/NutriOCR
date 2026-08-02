### ----------------------- GPT-5 Text Recognition file ----------------------- ###

import time

from openai import OpenAI
from tqdm import tqdm

from prompts import EXTRACTION_PROMPT
from utils import (
    NUTRITION_SCHEMA,
    PROJECT_DIR,
    encode_image_base64,
    parse_json_response,
    prepare_image,
    run_batch,
    save_json_result,
)

MODEL = "gpt-5"
IMAGE_DIR_PATH = PROJECT_DIR / "input_photos"
RESULT_DIR_PATH = PROJECT_DIR / "results_gpt5"
SCORES_DIR_PATH = PROJECT_DIR / "model_scores" / "model_scores.md"

_client = None


class OpenAIStreamError(RuntimeError):
    def __init__(self, message, request_id=None, response_id=None):
        super().__init__(message)
        self.request_id = request_id
        self.response_id = response_id

### ------------------------------------ Image Preprocessing ------------------------------------ ###

def build_image_input(image_path):
    image = prepare_image(image_path)
    image_b64 = encode_image_base64(image)
    return {
        "type": "input_image",
        "image_url": f"data:image/jpeg;base64,{image_b64}",
    }


### ------------------------------------ Text Recognition ------------------------------------ ###

def process_image(image_path):
    global _client

    if _client is None:
        # run_batch owns the single visible retry; disable hidden SDK retries.
        _client = OpenAI(max_retries=0)

    preparation_started_at = time.perf_counter()
    image_input = build_image_input(image_path)
    preparation_seconds = time.perf_counter() - preparation_started_at

    request_started_at = time.perf_counter()
    first_event_seconds = None
    first_text_seconds = None
    event_count = 0
    last_event_type = None
    request_id = None
    response_id = None
    completed_response = None
    response_parts = []

    try:
        with _client.responses.stream(
            model=MODEL,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": EXTRACTION_PROMPT,
                        },
                        image_input,
                    ],
                }
            ],
            text={
                "format": {
                    "type": "json_schema",
                    "name": "nutrition_label_result",
                    "strict": True,
                    "schema": NUTRITION_SCHEMA,
                }
            },
        ) as stream:
            headers = getattr(getattr(stream, "_response", None), "headers", None)
            if headers:
                request_id = headers.get("x-request-id")

            for event in stream:
                now = time.perf_counter()
                event_count += 1
                last_event_type = event.type

                if first_event_seconds is None:
                    first_event_seconds = now - request_started_at
                    tqdm.write(
                        f"[{MODEL}] Stream connected after "
                        f"{first_event_seconds:.2f} seconds."
                    )

                if event.type == "response.created":
                    response_id = event.response.id
                elif event.type == "response.output_text.delta":
                    if first_text_seconds is None:
                        first_text_seconds = now - request_started_at
                        tqdm.write(
                            f"[{MODEL}] First text received after "
                            f"{first_text_seconds:.2f} seconds."
                        )
                    response_parts.append(event.delta)
                elif event.type == "response.completed":
                    completed_response = event.response
                    response_id = completed_response.id
                elif event.type in {"response.failed", "response.incomplete"}:
                    completed_response = event.response
                    response_id = completed_response.id
    except Exception as error:
        request_seconds = time.perf_counter() - request_started_at
        raise OpenAIStreamError(
            f"OpenAI stream failed after {request_seconds:.2f} seconds; "
            f"first_event_seconds={first_event_seconds!r}; "
            f"first_text_seconds={first_text_seconds!r}; "
            f"last_event={last_event_type!r}; event_count={event_count}",
            request_id=request_id,
            response_id=response_id,
        ) from error
    request_seconds = time.perf_counter() - request_started_at

    if completed_response is None or last_event_type != "response.completed":
        error_details = getattr(completed_response, "error", None)
        incomplete_details = getattr(completed_response, "incomplete_details", None)
        raise OpenAIStreamError(
            f"OpenAI stream ended without response.completed; "
            f"last_event={last_event_type!r}; event_count={event_count}; "
            f"error={error_details!r}; incomplete_details={incomplete_details!r}",
            request_id=request_id,
            response_id=response_id,
        )

    source = (
        f"OpenAI model {MODEL} "
        f"(status={completed_response.status!r}, "
        f"incomplete_details={completed_response.incomplete_details!r})"
    )
    parsing_started_at = time.perf_counter()
    data = parse_json_response("".join(response_parts), source=source)
    parsing_seconds = time.perf_counter() - parsing_started_at

    usage = completed_response.usage

    metadata = {
        "image_preparation_seconds": round(preparation_seconds, 3),
        "model_response_seconds": round(request_seconds, 3),
        "time_to_first_event_seconds": round(first_event_seconds, 3),
        "time_to_first_text_seconds": round(first_text_seconds, 3),
        "stream_event_count": event_count,
        "stream_last_event": last_event_type,
        "json_parsing_seconds": round(parsing_seconds, 3),
        "openai_request_id": request_id,
        "openai_response_id": response_id,
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "total_tokens": usage.total_tokens,
    }

    return data, metadata


### ------------------------------------ Main Loop ------------------------------------ ###

def main():
    run_batch(
        process_image=process_image,
        save_result=save_json_result,
        input_dir=IMAGE_DIR_PATH,
        output_dir=RESULT_DIR_PATH,
        model_name=MODEL,
        scores_file=SCORES_DIR_PATH,
    )


if __name__ == "__main__":
    main()
