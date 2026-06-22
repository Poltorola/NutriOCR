
# Verificator checks each text/md file in <model>_results folder and assesses recognition accuracy.

# Reference values (14pics lables, june dataset) are provided by me. 
# Later for getting reference values might implement: barcode search / web or databases search.
# Verificator is strict: "-1.0" or "1.0g" instead of "1.0 g" are incorrect (despite being close)
# If model misses one value out of [3*macronutrients, energy, mass] recognition is considered incorrect.

import re
from pathlib import Path
from tqdm import tqdm

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
        "fats": "10",
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

model = "PaddleOCR"  #  "Gemma27b" "Gemma12b"   "PaddleOCR" "gpt-5"   constant to change model 

RESULTS_DIRS = {
    "Gemma27b": "/home/k3l/projects/NutriOCR/results_gemma27b",
    "Gemma12b": "/home/k3l/projects/NutriOCR/results_gemma12b",
    "PaddleOCR": "/home/k3l/projects/NutriOCR/results_paddleocr",
    "gpt-5": "/home/k3l/projects/NutriOCR/results_gpt5"
}
results_dir = Path(RESULTS_DIRS[model])
model_scores_path = Path("/home/k3l/projects/NutriOCR/model_scores.md")

score = 0
model_score = {model : score}         # every correct (kcal, nutrient) value: score = +1
correct_transcriptions = {0 : []}     # amount : [names] of correctly recognized photos. file is correct if all four values are correct
incorrect_transcriptions = {0 : []}   # amount : [names] of incorrectly recognized photos.


### ------------------------------- Values Comparison ------------------------------------- ###

def value_found(text, value, keywords):
    escaped_value = re.escape(value)

    if "," in value:
        escaped_value = escaped_value.replace(",", r"[,.]") # 1.1 and 1,1 both correct

    keyword_pattern = "|".join(re.escape(k) for k in sorted(keywords, key=len, reverse=True))  # regular variables magic...

    text = re.sub(r"\s+", " ", text.lower())

    value_pattern = rf"(?<![\d.,]){escaped_value}(?![\d.,])"

    pattern_1 = rf"({keyword_pattern}).{{0,100}}{value_pattern}"
    pattern_2 = rf"{value_pattern}.{{0,100}}({keyword_pattern})"

    return (
        re.search(pattern_1, text, re.IGNORECASE) is not None 
        or re.search(pattern_2, text, re.IGNORECASE) is not None
    )



### ---------------------------------------- Score Tracking ---------------------------------------------- ###

def verify():
    
    total_score = 0     # every correct (kcal, nutrient) value: score = +1
    max_score = 0

    correct_transcriptions = []   # names of correctly recognized photos. file is correct if all four values are correct
    incorrect_transcriptions = [] # names of incorrectly recognized photos.
    detailed_results = {}


    for file_path in tqdm(list(results_dir.glob("*.md"))):  # progress bar to track operation state
        product_name = file_path.stem

        if product_name not in verified_nutrients:
            print(f"Skipping unknown file: {file_path.name}") # exclude non .md
            continue


        text = file_path.read_text(encoding="utf-8").lower()  # reads file content

        expected_values = verified_nutrients[product_name]

        file_score = 0
        file_max_score = len(expected_values)
        missing_values = []


        for nutrient_name, correct_value in expected_values.items(): # calls search
            keywords = NUTRIENT_KEYWORDS[nutrient_name]

            if value_found(text, correct_value, keywords):
                file_score += 1
            else:
                print(
                    f"{product_name}: missing "
                    f"{nutrient_name} = {correct_value}"
                )
                missing_values.append(f"{nutrient_name}: {correct_value}")


        total_score += file_score       # detailed records about model's accuracy
        max_score += file_max_score

        detailed_results[product_name] = {
            "score": file_score,
            "max_score": file_max_score,
            "missing": missing_values,
        }

        if file_score == file_max_score:
            correct_transcriptions.append(product_name)
        else:
            incorrect_transcriptions.append(product_name)

    write_report(
        total_score,
        max_score,
        correct_transcriptions,
        incorrect_transcriptions,
        detailed_results,
    )


### -------------------------------- Writes the score into model_scores.md ----------------------------------- ###

def write_report(
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


verify()


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