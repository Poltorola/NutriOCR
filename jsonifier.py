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

NUTRITION_SCHEMA = {        # json schema
    "type": "object",
    "properties": {
        "kcal": {"type": ["number", "null"]},
        "prots": {"type": ["number", "null"]},
        "fats": {"type": ["number", "null"]},
        "carbs": {"type": ["number", "null"]},
        "basis": {
            "type": ["string", "null"],
            "enum": ["per_100g", "per_100ml", "per_serving", None]
        },
        "notes": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["kcal", "prots", "fats", "carbs", "basis", "notes"],
    "additionalProperties": False
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
                    "You extract nutrition facts from OCR text. "
                    "Return only values that are clearly present in the text. "
                    "Do not guess. If a value is missing or unclear, return null. "
                    "Convert comma decimals to dot decimals."
                )
            },
            {
                "role": "user",
                "content": f"""
Extract nutrition information from this OCR text.

Rules:
- kcal = calories / energy value / энергетическая ценность / ккал
- prots = proteins / белки / ақуыз
- fats = fats / жиры / май
- carbs = carbohydrates / углеводы / көмірсу
- Prefer values per 100 g or per 100 ml.
- If values are for 100 g, basis = "per_100g".
- If values are for 100 ml, basis = "per_100ml".
- If only serving values are visible, basis = "per_serving".
- If basis is unclear, basis = null.
- Return null for missing values.
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



# ---------------------- JSON structure validation ---------------------------------------- #

def verify_json(text_json):
    required_fields = ["kcal", "prots", "fats", "carbs", "basis", "notes"]

    validation = {
        "passed": True,
        "warnings": [],
        "errors": []
    }

    for field in required_fields:   # check required fields
        if field not in text_json:
            validation["passed"] = False
            validation["errors"].append(f"Missing required field: {field}")

    if validation["errors"]:                    # stop if structure too broken
        text_json["validation"] = validation

        return text_json


    nutrient_fields = ["kcal", "prots", "fats", "carbs"] 

    plausible_ranges = {
        "kcal": (0, 1000),
        "prots": (0, 100),
        "fats": (0, 100),
        "carbs": (0, 100)
    }

    for field in nutrient_fields:
        value = text_json[field]

        if value is None:
            validation["warnings"].append(f"{field} is missing.")
            continue

        if not isinstance(value, (int, float)):
            validation["passed"] = False
            validation["errors"].append(
                f"{field} must be a number or null, got {type(value).__name__}."
            )
            continue

        min_value, max_value = plausible_ranges[field]

        if value < min_value or value > max_value:
            validation["warnings"].append(
                f"{field}={value} is outside plausible range {min_value}-{max_value}."
            )

    # check basis
    allowed_basis = ["per_100g", "per_100ml", "per_serving", None]

    if text_json["basis"] not in allowed_basis:
        validation["passed"] = False
        validation["errors"].append(
            f"basis must be one of {allowed_basis}, got {text_json['basis']}."
        )

    # check notes
    if not isinstance(text_json["notes"], list):
        validation["passed"] = False
        validation["errors"].append("notes must be a list.")

    # optional calorie consistency check
    kcal = text_json["kcal"]
    prots = text_json["prots"]
    fats = text_json["fats"]
    carbs = text_json["carbs"]

    if all(isinstance(v, (int, float)) for v in [kcal, prots, fats, carbs]):
        estimated_kcal = prots * 4 + fats * 9 + carbs * 4

        difference = abs(kcal - estimated_kcal)

        if difference > 80:
            validation["warnings"].append(
                f"Calories may be inconsistent: kcal={kcal}, estimated from macros={round(estimated_kcal, 1)}."
            )

    if validation["errors"]:
        validation["passed"] = False

    text_json["validation"] = validation

    return text_json


### ------------------------------ Main loop ---------------------------------------------- ###

if __name__ == "__main__":
    for file_path in input_dir.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        # json_data = txt_to_json_algo(text)
        json_data = txt_to_json_llm(file_path)
        json_data = verify_json(json_data)


        output_file = output_dir / f"{file_path.stem}.json"

        output_file.write_text(
            json.dumps(json_data, ensure_ascii=False, indent=4),
            encoding="utf-8"
        )

        print(f"Converted: {file_path.name} -> {output_file.name}")

