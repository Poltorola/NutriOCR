# --------------------------------- Gemma3 12b or 27b Text Recognition --------------------------------- #

# 11.06: extract photo from folder => feed to Gemma3 through Ollama => save the transcripted output

import json
import requests

from prompts import EXTRACTION_PROMPT
from utils import (
    NUTRITION_SCHEMA,
    PROJECT_DIR,
    encode_image_base64,
    prepare_image,
    run_batch,
    save_json_result,
)


IMAGE_DIR_PATH = PROJECT_DIR / "input_photos"
SCORES_DIR_PATH = PROJECT_DIR / "model_scores" / "model_scores.md"

MODEL = "gemma3:12b-it-q8_0"
#MODEL = "gemma3:27b-it-q4_K_M"
RESULT_DIR_PATH = PROJECT_DIR / "results_gemma12b"

### ------------------------------------ Text Recognition ------------------------------------ ###

def build_image_input(image_path):
    image = prepare_image(image_path)
    return encode_image_base64(image)


def process_image(image_path):
    metadata = {}
    image_b64 = build_image_input(image_path)

    r = requests.post(
        "http://172.19.48.1:11434/api/chat",        # calling Gemma via Ollama
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": EXTRACTION_PROMPT,
                    "images": [
                        image_b64
                    ]
                }
            ],
            "format": NUTRITION_SCHEMA,
            "options": {
                "temperature": 0
            }
        },
        stream=True
    )

    r.raise_for_status()

    response_parts = []
    for line in r.iter_lines(decode_unicode=True):
        if not line:
            continue

        data = json.loads(line)
        token = data.get("message", {}).get("content", "")

        if token:
            response_parts.append(token)

        if data.get("done"):
            metadata = {
                "prompt_tokens": data.get("prompt_eval_count", 0),
                "output_tokens": data.get("eval_count", 0),
            }

    result = json.loads("".join(response_parts))
    return result, metadata


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


