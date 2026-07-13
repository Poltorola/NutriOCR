### ----------------------- GPT-5 Text Recognition ----------------------- ###

import json

from openai import OpenAI

from prompts import EXTRACTION_PROMPT
from utils import (
    NUTRITION_SCHEMA,
    PROJECT_DIR,
    encode_image_base64,
    prepare_image,
    run_batch,
    save_json_result,
)

MODEL = "gpt-5"
IMAGE_DIR_PATH = PROJECT_DIR / "input_photos"
RESULT_DIR_PATH = PROJECT_DIR / "results_gpt5"
SCORES_DIR_PATH = PROJECT_DIR / "model_scores" / "model_scores.md"

_client = None

### ------------------------------------ Image Preparation ------------------------------------ ###

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
        _client = OpenAI()

    image_input = build_image_input(image_path)

    response = _client.responses.create(
        model=MODEL,
        input=[             # prompt
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
        text={                          # json schema
            "format": {
                "type": "json_schema",
                "name": "nutrition_label_result",
                "strict": True,
                "schema": NUTRITION_SCHEMA,
            }
        }
    )

    data = json.loads(response.output_text)

    metadata = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "total_tokens": response.usage.total_tokens,
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
