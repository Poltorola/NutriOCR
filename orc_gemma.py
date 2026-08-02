# --------------------------------- Gemma Text Recognition --------------------------------- #

# 11.06: extract photo from folder => feed to Gemma3 through Ollama => save the transcripted output

import argparse

from prompts import EXTRACTION_PROMPT
from utils import (
    NUTRITION_SCHEMA,
    PROJECT_DIR,
    encode_image_base64,
    infer_local_vision_json,
    local_model_session,
    prepare_image,
    run_batch,
    save_json_result,
)


IMAGE_DIR_PATH = PROJECT_DIR / "input_photos"
SCORES_DIR_PATH = PROJECT_DIR / "model_scores" / "model_scores.md"

DEFAULT_MODEL = "gemma3:12"
OLLAMA_CONTEXT_LENGTH = 16_384
MODEL_OPTIONS = {
    "gemma3:12": ("ollama", "gemma3:12b-it-q8_0"),
    "gemma3:26": ("ollama", "gemma3:27b-it-q4_K_M"),
    "gemma4:26": ("ollama", "gemma4:26b-a4b-it-qat"),
    "gemma4:31": ("ollama", "gemma4:31b-it-qat"),
    "gemma4:12": ("ollama", "gemma4:12b"),
    "gemma4:e4b": ("llama_cpp", "gemma4:E4B"),
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract nutrition labels with Gemma via a local model server."
    )
    parser.add_argument(
        "--model",
        choices=MODEL_OPTIONS,
        default=DEFAULT_MODEL,
        help=f"Gemma test configuration to use (default: {DEFAULT_MODEL})",
    )
    return parser.parse_args()


def result_dir_for(model):
    safe_model_name = model.replace(":", "_").replace("/", "_")
    return PROJECT_DIR / f"results_{safe_model_name}"

### ------------------------------------ Text Recognition ------------------------------------ ###

def build_image_input(image_path):
    image = prepare_image(image_path)
    return encode_image_base64(image)


def process_image(image_path, provider, model):
    image_b64 = build_image_input(image_path)
    return infer_local_vision_json(
        prompt=EXTRACTION_PROMPT,
        image_b64=image_b64,
        provider=provider,
        model=model,
        schema=NUTRITION_SCHEMA,
        context_length=OLLAMA_CONTEXT_LENGTH,
    )


### ------------------------------------ Main Loop ------------------------------------ ###

def main():
    args = parse_args()
    provider, model = MODEL_OPTIONS[args.model]

    with local_model_session(provider, model):
        run_batch(
            process_image=lambda image_path: process_image(
                image_path, provider, model
            ),
            save_result=save_json_result,
            input_dir=IMAGE_DIR_PATH,
            output_dir=result_dir_for(args.model),
            model_name=model,
            scores_file=SCORES_DIR_PATH,
        )


if __name__ == "__main__":
    main()
