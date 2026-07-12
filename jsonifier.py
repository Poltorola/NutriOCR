# -------------- MD => JSON Converter -------------------#

import json
import re
from pathlib import Path
from openai import OpenAI
import os
from tqdm import tqdm
import time

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
                "content": (
                    "You extract structured product-label information from multilingual OCR text. "
                    "Use only information clearly present in the supplied OCR text. "
                    "Do not guess or invent missing values."
                )
            },
            {
                "role": "user",
                "content": f"""
Extract product and nutrition information from this OCR text.

Rules:
- Copy the supplied OCR text verbatim into recognized_text; do not reconstruct unreadable fragments.
- The label may contain any language or several parallel translations.
- Use a clearer equivalent in another language on the same label to recover poorly recognized fields.
- Cross-check translations and repeated nutrition panels, but do not combine values from different products or unrelated sections.
- Extract the visible product name, company/manufacturer name, and barcode.
- Return barcode as digits only, preserving leading zeros.
- Extract net product weight into net_weight_g and volume into volume_ml.
- Convert kilograms to grams and liters to milliliters when necessary.
- Do not confuse a nutrition-table basis such as 100 g or 100 ml with net weight or volume.
- Return nutrition values per 100 g when the OCR text uses a mass basis, or per 100 ml when it uses a volume basis.
- Both per-100-g and per-100-ml nutrition values are valid.
- Nutrition tables may show adjacent columns for per 100 g/ml, per serving, per package, and percent daily intake.
- Read the column headers carefully and select the explicitly labeled per-100-g or per-100-ml column.
- Never take values from a serving, whole-package, or percent-daily-intake column when a per-100-g/ml column is present.
- If no per-100-g/ml column exists and values are per serving, convert them to per 100 g when the serving mass is visible, or to per 100 ml when the serving volume is visible.
- Do not convert between a mass basis and a volume basis unless product density is explicitly provided.
- If a serving value cannot be converted to either basis without guessing, return null.
- Energy may be printed in both kJ and kcal, often next to each other. The kcal field must contain kilocalories, never the kJ number.
- When both are present, copy the explicitly labeled kcal value. If only kJ is clearly present, convert it to kcal by dividing by 4.184.
- kcal means calories / energy value / энергетическая ценность / ккал.
- protein_g means proteins / белки / ақуыз.
- fat_g means total fats / жиры / май.
- carbs_g means carbohydrates / углеводы / көмірсу.
- Extract saturated fat, sugars, fiber, and salt only when clearly present.
- All nutrition, weight, and volume values must be JSON numbers without units or text.
- Convert comma decimal separators to dots and do not round values.
- Return null for every missing or uncertain scalar value.
- Do not invent values.

OCR text:
                    {md_text}
                    """
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
