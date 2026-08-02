# ------------------------- PaddleOCR Text Recognition ------------------------- #

# CPU version used during development:
# paddlepaddle==3.2.0 paddleocr==3.3.3

import numpy as np
from openai import OpenAI

from prompts import OCR_TEXT_EXTRACTION_PROMPT, OCR_TEXT_SYSTEM_PROMPT
from utils import (
    NUTRITION_SCHEMA,
    PROJECT_DIR,
    parse_json_response,
    prepare_image,
    run_batch,
    save_json_result,
)

from paddleocr import PPStructureV3


MODEL = "paddleocr+gpt-5-jsonifier"
IMAGE_DIR_PATH = PROJECT_DIR / "input_photos"
RESULT_DIR_PATH = PROJECT_DIR / "results_json_paddleocr"
SCORES_DIR_PATH = PROJECT_DIR / "model_scores" / "model_scores.md"

_ocr = None
_jsonifier_client = None


def _get_ocr(): # model creation
    global _ocr

    if _ocr is None:
        _ocr = PPStructureV3(
            text_recognition_model_name="cyrillic_PP-OCRv5_mobile_rec",
            # Whole-image rotation is performed once in prepare_image().
            use_doc_orientation_classify=False,
            use_textline_orientation=True,
        )

    return _ocr


def build_image_input(image_path):  # image preprocessing
    image = prepare_image(image_path)
    return np.asarray(image)


def txt_to_json_llm(ocr_text):  # converting outpt text into json via gpt-5
    global _jsonifier_client

    if _jsonifier_client is None:
        # run_batch owns the single visible retry; disable hidden SDK retries.
        _jsonifier_client = OpenAI(max_retries=0)

    response = _jsonifier_client.responses.create(
        model="gpt-5",
        input=[
            {
                "role": "system",
                "content": OCR_TEXT_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": OCR_TEXT_EXTRACTION_PROMPT.format(
                    ocr_text=ocr_text,
                ),
            },
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "nutrition_facts",
                "schema": NUTRITION_SCHEMA,
                "strict": True,
            }
        },
    )
    source = (
        "OpenAI PaddleOCR JSON converter "
        f"(status={getattr(response, 'status', None)!r}, "
        f"incomplete_details={getattr(response, 'incomplete_details', None)!r})"
    )
    return parse_json_response(response.output_text, source=source)


def process_image(image_path):  # paddleocr
    image_input = build_image_input(image_path)
    result = _get_ocr().predict(image_input)
    page = result[0]

    ocr_text = page.markdown["markdown_texts"]
    json_result = txt_to_json_llm(ocr_text)
    return json_result, {}


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
