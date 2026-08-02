# -------------- MD => JSON Converter -------------------#

import json
import re
from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv
from tqdm import tqdm
import time

from prompts import OCR_TEXT_EXTRACTION_PROMPT, OCR_TEXT_SYSTEM_PROMPT

load_dotenv(Path(__file__).resolve().parent / ".env")

### ---------------------- Reference values ---------------------------------------------- ###

input_dir = Path("/home/k3l/projects/NutriOCR/results_paddleocr")
output_dir = Path("/home/k3l/projects/NutriOCR/results_json_paddleocr")
output_dir.mkdir(exist_ok=True)

text = "..."
NUTRIENT_KEYWORDS = {
    "kcal": [
        "kcal", "energy", "energetic", "energetic value",
        "энергетическая ценность", "пищевая ценность", "ккал"
    ],
    "prots": ["protein", "proteins", "белки", "белок", "белоктар", "ақуыз"],
    "fats": ["fat", "fats", "жиры", "жир", "май", "майлар"],
    "carbs": ["carbohydrate", "carbohydrates", "carbs", "углеводы", "көмірсу", "көмірсулар"],
}
NUMBER_PATTERN = r"\d+(?:[,.]\d+)?"

NUTRITION_SCHEMA = {        # same model-output schema as in ocr_gpt5.py
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
                "salt_g": {"type": ["number", "null"]}
            },
            "required": [
                "kcal", "protein_g", "fat_g", "saturated_fat_g",
                "carbs_g", "sugars_g", "fiber_g", "salt_g"
            ]
        },
    },
    "required": [
        "recognized_text", "product_name", "company_name", "barcode",
        "net_weight_g", "volume_ml", "nutrition"
    ]
}

incorrect_transcriptions = []
correct_transcriptions = []



# --------------------- Text preparation ------------------------------- #

def _normalize_text(text):
    text = text.lower()
    text = text.replace("\xa0", " ")    # sometimes ocr generates weird spaces
    text = re.sub(r"\s+", " ", text)
    return text



# ---------------------- Values search ------------------------------------- #

def find_value_near_keyword(text, target_keywords, all_keywords, window=100): # REDUNDANT searches through text
    target_pattern = "|".join(
        re.escape(k) for k in sorted(target_keywords, key=len, reverse=True)
    )

    all_keyword_pattern = "|".join(
        re.escape(k) for k in sorted(all_keywords, key=len, reverse=True)
    )

    for match in re.finditer(target_pattern, text, re.IGNORECASE):
        start = match.start()
        end = match.end()

        after = text[end:end + window]

        next_keyword = re.search(all_keyword_pattern, after, re.IGNORECASE) # stop at next keyword

        if next_keyword:
            after = after[:next_keyword.start()]

        number_match = re.search(NUMBER_PATTERN, after)

        if number_match:
            return number_match.group(0).replace(",", ".")

        before = text[max(0, start - window):start]
        numbers = re.findall(NUMBER_PATTERN, before)

        if numbers:
            return numbers[-1].replace(",", ".")

    return None



# ---------------------- Mixed text cases -------------------------- #

def table_fallback(text):   # REDUNDANT
    """
    Handles cases like:
    май/жир
    ақуыз/белок
    көмірсу/углеводы
    4,7 г
    2,8 г
    3,2 г
    """
    values = []

    for nutrient, keywords in NUTRIENT_KEYWORDS.items():

        for keyword in keywords:
            match = re.search(re.escape(keyword), text)
            if match:
                values.append((match.start(), nutrient))
                break

    numbers = re.findall(NUMBER_PATTERN, text)

    if len(values) >= 2 and len(numbers) >= len(values):
        result = {}
        for i, (_, nutrient) in enumerate(values):
            result[nutrient] = numbers[i].replace(",", ".")
        return result

    return {}



# ---------------------- Algoritmic converter (obsolete) ---------------------------------------- #
def txt_to_json_algo(text): # REDUNDANT
    clean_text = _normalize_text(text)

    data = {
        "kcal": None,
        "prots": None,
        "fats": None,
        "carbs": None,
        "raw_text": text.strip()
    }

    all_keywords = []
    for keywords in NUTRIENT_KEYWORDS.values():
        all_keywords.extend(keywords)

    for nutrient, keywords in NUTRIENT_KEYWORDS.items():
        data[nutrient] = find_value_near_keyword(
            clean_text,
            target_keywords=keywords,
            all_keywords=all_keywords
        )

    fallback_values = table_fallback(clean_text)

    for nutrient, value in fallback_values.items():
        if data[nutrient] is None:
            data[nutrient] = value

    return data



# ---------------------- LLM converter ---------------------------------------- #

def txt_to_json_llm(text_path):     # promts llm to convert text into json
    client = OpenAI()
    text_path = Path(text_path)
    md_text = text_path.read_text(encoding="utf-8")

    response = client.responses.create(
        model="gpt-5",
        input=[
            {   # prompt
                "role": "system",               
                "content": OCR_TEXT_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": OCR_TEXT_EXTRACTION_PROMPT.format(
                    ocr_text=md_text,
                ),
                                }
                            ],
                            text={
                                "format": {
                                    "type": "json_schema",
                                    "name": "nutrition_facts",
                                    "schema": NUTRITION_SCHEMA,
                                    "strict": True
                                }
                            }
                        )
    return json.loads(response.output_text)



### ------------------------------ Main loop ---------------------------------------------- ###

if __name__ == "__main__":
    for file_path in input_dir.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        # json_data = txt_to_json_algo(text)
        json_data = txt_to_json_llm(file_path)
        json_data["image"] = next(
            (
                image_path.name
                for image_path in Path("input_photos").glob(f"{file_path.stem}.*")
                if image_path.suffix.lower() in {".jpg", ".jpeg", ".png"}
            ),
            file_path.stem,
        )
        json_data["model"] = "paddleocr+gpt-5-jsonifier"


        output_file = output_dir / f"{file_path.stem}.json"

        output_file.write_text(
            json.dumps(json_data, ensure_ascii=False, indent=4),
            encoding="utf-8"
        )

        print(f"Converted: {file_path.name} -> {output_file.name}")
