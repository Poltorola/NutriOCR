
# Verificator checks each text/md file in <model>_results folder and assesses recognition accuracy.

# Reference values (14pics lables, june dataset) are provided by me. 
# Later for getting reference values might implement: barcode search / web or databases search.
# Verificator is strict: "-1.0" or "1.0g" instead of "1.0 g" are incorrect (despite being close)
# If model misses one value out of [3*macronutrients, energy, mass] recognition is considered incorrect.

import re
import json
from pathlib import Path

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    def tqdm(iterable):
        return iterable

### ------------------------------ Reference Values ---------------------------------------------- ###

NUTRIENT_KEYWORDS = {
    "kcal": ["kcal", "energy", "energetic", "energetic value", "энергетическая ценность", "пищевая ценность", "ккал"],
    "prots": ["protein", "proteins", "белки", "белоктар"],
    "fats": ["fat", "fats", "жиры", "майлар"],
    "carbs": ["carbohydrate", "carbohydrates", "carbs", "углеводы", "көмірсулар", "Г"],
    "mass" : ["g", "gram", "grams", "граммы", "грамм", "г"],
    "volume" : ["ml", "l", "мл", "л"]
}

verified_nutrients = {
    "bread": {
        "kcal": "31",
        "prots": "1,1",
        "fats": "0,2",
        "carbs": "5,7"
    },
    "carrots": {
        "kcal": "35",
        "prots": "1,3",
        "fats": "0,1",
        "carbs": "7,2"
    },
    "cheese": {
        "kcal": "270",
        "prots": "26",
        "fats": "18",
        "carbs": "1"
    },
    "cocomilk": {
        "kcal": "237",
        "prots": "2,5",
        "fats": "24",
        "carbs": "2,8"
    },
    "cookie": {
        "kcal": "398",
        "prots": "7,4",
        "fats": "16,1",
        "carbs": "56,2"
    },
    "metat": {
        "kcal": "143",
        "prots": "16",
        "fats": "10"
    },
    "milk": {
        "kcal": "59",
        "prots": "2,8",
        "fats": "3,2",
        "carbs": "4,7"
    },
    "nutsandseeds": {
        "kcal": "557,4",
        "prots": "22,8",
        "fats": "47,3",
        "carbs": "10,6"
    },
    "pesto": {
        "kcal": "329",
        "prots": "3,8",
        "fats": "29",
        "carbs": "12"
    },
    "redbull": {
        "kcal": "3",
        "prots": "0",
        "fats": "0",
        "carbs": "0"
    },
    "sausages": {
        "kcal": "160",
        "prots": "10",
        "fats": "12",
        "carbs": "3"
    },
    "softcheese": {
        "kcal": "198",
        "prots": "7,8",
        "fats": "17,0",
        "carbs": "3,5"
    },
    "waffle": {
        "kcal": "550",
        "prots": "20,0",
        "fats": "32,0",
        "carbs": "45,0"
    },
    "test": {
        "kcal": "42",
        "prots": "0",
        "fats": "0",
        "carbs": "10,6"
    }
}
# verified_nutrients = Path("/home/k3l/projects/NutriOCR/verified_nutrients.json)

KEY_ALIASES = {
    "protein_g": "prots",
    "proteins_g": "prots",
    "prots": "prots",
    "fat_g": "fats",
    "fats_g": "fats",
    "fats": "fats",
    "carbohydrates_g": "carbs",
    "carbs_g": "carbs",
    "carbs": "carbs",
    "kcal": "kcal",
    "calories": "kcal",
    "energy_kcal": "kcal",
    "net_weight_g": "mass",
    "mass": "mass",
    "volume_ml": "volume",
    "volume": "volume",
}


RESULTS_DIRS = {
    "Gemma12b": "/home/k3l/projects/NutriOCR/results_gemma12b",
    "Gemma27b": "/home/k3l/projects/NutriOCR/results_gemma27b",
    "gpt-5": "/home/k3l/projects/NutriOCR/results_gpt5",
    "PaddleOCR": "/home/k3l/projects/NutriOCR/results_json_paddleocr",
}
model_scores_path = Path("/home/k3l/projects/NutriOCR/model_scores.md")



### ------------------------------- Internal Helpers ------------------------------------- ###

def _load_json(content):        # json parsing
    if isinstance(content, (str, Path)):
        return json.loads(Path(content).read_text(encoding="utf-8"))
    return content


def _canonical_values(content): # ensures dict keys are unified: fat_g => fats
    values = {}

    for key, value in content.items():
        canonical_key = KEY_ALIASES.get(key)
        if canonical_key:
            values[canonical_key] = value

    nutrition = content.get("nutrition")
    if isinstance(nutrition, dict):
        for key, value in nutrition.items():
            canonical_key = KEY_ALIASES.get(key)
            if canonical_key:
                values[canonical_key] = value

    return values


def _normalize_value(value):    # prepares text
    if value is None:
        return None

    if isinstance(value, str):
        value = value.strip().replace(",", ".")
        number_match = re.search(r"-?\d+(?:\.\d+)?", value)
        if number_match:
            value = number_match.group(0)

    try:
        return float(value)
    except (TypeError, ValueError):
        return str(value).strip().lower()


def _product_name(text_json, text_source=None): # fetches product name
    for field in ("image", "product_name"):
        value = text_json.get(field)
        if value:
            return Path(str(value)).stem

    if isinstance(text_source, (str, Path)):
        return Path(text_source).stem

    return None



### ------------------------------- Values Comparison ------------------------------------- ###

def _values_equal(actual, expected):    # compares normalized values
    actual = _normalize_value(actual)
    expected = _normalize_value(expected)

    if actual is None or expected is None:
        return actual is expected

    if isinstance(actual, float) and isinstance(expected, float):
        return abs(actual - expected) < 1e-9

    return actual == expected


def value_found(text, value, keywords): # REDUNDANT: compares values based on regex, used for txt or md files
#     escaped_value = re.escape(value)

#     if "," in value:
#         escaped_value = escaped_value.replace(",", r"[,.]") # 1.1 and 1,1 both correct

#     keyword_pattern = "|".join(re.escape(k) for k in sorted(keywords, key=len, reverse=True))  # regular variables magic...

#     text = re.sub(r"\s+", " ", text.lower())

#     value_pattern = rf"(?<![\d.,]){escaped_value}(?![\d.,])"

#     pattern_1 = rf"({keyword_pattern}).{{0,100}}{value_pattern}"
#     pattern_2 = rf"{value_pattern}.{{0,100}}({keyword_pattern})"

#     return (
#         re.search(pattern_1, text, re.IGNORECASE) is not None 
#         or re.search(pattern_2, text, re.IGNORECASE) is not None
#     )
    pass


def verify_content(text_json, verified_content): # compares two JSONs
    text_source = text_json
    text_json = _load_json(text_json)
    verified_content = _load_json(verified_content)

    product_name = _product_name(text_json, text_source)
    expected_values = verified_content.get(product_name, verified_content)
    actual_values = _canonical_values(text_json)
    expected_values = _canonical_values(expected_values)

    correct_values = []
    missed_values = []

    for nutrient, expected_value in expected_values.items():
        if expected_value is None or nutrient not in actual_values:
            continue

        actual_value = actual_values[nutrient]

        if _values_equal(actual_value, expected_value):
            correct_values.append(f"{nutrient}: {expected_value}")
        else:
            missed_values.append(
                f"{nutrient}: expected {expected_value}, got {actual_value}"
            )

    return len(missed_values) == 0, correct_values, missed_values


def verify_md(file_path): # REDUNDANT: was used to verify .md until all output was changed into .json

    # text = file_path.read_text(encoding="utf-8").lower()  # reads file content
    # product_name = product_name = file_path.stem

    # file_score = 0
    # missing_values = []


    # for nutrient_name, correct_value in expected_values.items(): # calls search
    #     keywords = NUTRIENT_KEYWORDS[nutrient_name]

    #     if value_found(text, correct_value, keywords):
    #         file_score += 1
    #     else:
    #         print(
    #             f"{product_name}: missing "
    #             f"{nutrient_name} = {correct_value}"
    #         )
    #         missing_values.append(f"{nutrient_name}: {correct_value}")

    # detailed_results[product_name] = {
    #     "score": file_score,
    #     "max_score": file_max_score,
    #     "missing": missing_values,
    # }

    # return (file_score)
    pass



### -------------------------- Score Calculation ---------------------------------------------- ###

def score_results(results_dir, verified_nutrients): # how many files are fully correct?
    results_dir = Path(results_dir)
    verified_nutrients = _load_json(verified_nutrients)

    total_score = 0
    max_score = 0
    correct_transcriptions = []
    incorrect_transcriptions = []
    detailed_results = {}

    json_files = {file_path.stem: file_path for file_path in results_dir.glob("*.json")}

    for product_name, expected_values in verified_nutrients.items():
        file_path = json_files.get(product_name)

        if file_path is None:
            max_score += 1
            incorrect_transcriptions.append(product_name)
            detailed_results[product_name] = {
                "score": 0,
                "max_score": 1,
                "correct": [],
                "missing": [f"JSON file is missing: {product_name}.json"],
            }
            continue

        is_correct, correct_values, missed_values = verify_content(
            file_path,
            expected_values,
        )

        max_score += 1
        if is_correct:
            total_score += 1
            correct_transcriptions.append(product_name)
        else:
            incorrect_transcriptions.append(product_name)

        detailed_results[product_name] = {
            "score": 1 if is_correct else 0,
            "max_score": 1,
            "correct": correct_values,
            "missing": missed_values,
        }

    for product_name in sorted(set(json_files) - set(verified_nutrients)):
        print(f"Skipping unknown file: {json_files[product_name].name}")

    return (
        total_score,
        max_score,
        correct_transcriptions,
        incorrect_transcriptions,
        detailed_results,
    )



### ----------------------- Writes the score into model_scores.md ----------------------------------- ###

def write_report(
    model,
    total_score,
    max_score,
    correct_transcriptions,
    incorrect_transcriptions,
    detailed_results,
):
    percent = round(total_score / max_score * 100, 2) if max_score else 0

    report_lines = []

    report_lines.append(f"# ---------------------- Model scores: {model} ------------------------------- #")
    report_lines.append("")
    report_lines.append(f"Total score: **{total_score}/{max_score}**")
    report_lines.append(f"Accuracy: **{percent}%**")
    report_lines.append("")
    report_lines.append(f"Correct transcriptions: **{len(correct_transcriptions)}**")
    report_lines.append(", ".join(correct_transcriptions) if correct_transcriptions else "-")
    report_lines.append("")
    report_lines.append(f"Incorrect transcriptions: **{len(incorrect_transcriptions)}**")
    report_lines.append(", ".join(incorrect_transcriptions) if incorrect_transcriptions else "-")
    report_lines.append("")
    report_lines.append("## Details")
    report_lines.append("")

    for product_name, result in detailed_results.items():
        report_lines.append(
            f"### {product_name}: {result['score']}/{result['max_score']}"
        )

        if result["missing"]:
            report_lines.append("Missing values:")
            for missing in result["missing"]:
                report_lines.append(f"- {missing}")
        else:
            report_lines.append("All values found.")

        report_lines.append("")

    with open(model_scores_path, "a", encoding="utf-8") as f:
        f.write("\n\n")
        f.write("\n".join(report_lines))



### ------------------------------ Main loop ---------------------------------------------- ###

if __name__ == "__main__":
    for model, results_dir in RESULTS_DIRS.items():
        total_score, max_score, correct, incorrect, details = score_results(
            results_dir,
            verified_nutrients
        )

        write_report(
            model,
            total_score,
            max_score,
            correct,
            incorrect,
            details,
        )

        print(f"{model}: {total_score}/{max_score}")


# Lable info transcripted by my hooman eyes: 

# Name             Cal  prots  fats   carbs

# 1. bread         31     1,1    0,2    5,7
# 2. carrots       35     1,3    0,1    7,2
# 3. cheese        270    26     18     1
# 4. cocomilk      237    2,5    24     2,8
# 5. cookie        398    7,4    16,1   56,2
# 6. metat         143    16     10     -
# 7. milk          59     2,8    3,2    4,7
# 8. nutsandseeds  557,4  22,8   47,3   10,6
# 9. pesto         329    3,8    29     12
# 10. redbull      3      0      0      0
# 11. sausages     160    10     12     3
# 12. softcheese   198    7,8    17     3,5
# 13. waffle       550    20     32     45
# 14. test         42     0      0      10,6
