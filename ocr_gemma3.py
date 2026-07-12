# --------------------------------- Gemma3 12b or 27b Text Recognition --------------------------------- #

# 11.06: extract photo from folder => feed to Gemma3 through Ollama => save the transcripted output

import requests
import base64
import json
import os
from tqdm import tqdm
import time


IMAGE_DIR_PATH = "/home/k3l/projects/NutriOCR/input_photos/"

SCORES_DIR_PATH = "/home/k3l/projects/NutriOCR/model_scores.md"

MODEL = "gemma3:12b-it-q8_0"
#MODEL = "gemma3:27b-it-q4_K_M"
RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gemma12b"

NUTRITION_SCHEMA = {
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
        }
    },
    "required": [
        "recognized_text", "product_name", "company_name", "barcode",
        "net_weight_g", "volume_ml", "nutrition"
    ]
}

EXTRACTION_PROMPT = (
    "Extract structured product and nutrition information from this product-label image. "
    "The label may use any language, including multiple languages in parallel. "
    "Use equivalent text in another language on the same label to recover a field when one version is blurred or poorly recognized. "
    "Cross-check translations and repeated nutrition panels, but do not combine values from different products or unrelated sections. "
    "Transcribe only text that is actually visible into recognized_text; do not reconstruct or invent unreadable text. "
    "Extract the visible product name, company/manufacturer name, and barcode. "
    "Return barcode as digits only, preserving leading zeros. "
    "Extract net product weight into net_weight_g and volume into volume_ml. "
    "Convert kilograms to grams and liters to milliliters when necessary. "
    "Do not confuse a nutrition-table basis such as 100 g or 100 ml with net weight or volume. "
    "Return nutrition values per 100 g when the label uses a mass basis, or per 100 ml when it uses a volume basis. "
    "Both per-100-g and per-100-ml nutrition values are valid. "
    "Nutrition tables may show adjacent columns for per 100 g/ml, per serving, per package, and percent daily intake. "
    "Read the column headers carefully and select the explicitly labeled per-100-g or per-100-ml column. "
    "Never take values from a serving, whole-package, or percent-daily-intake column when a per-100-g/ml column is present. "
    "If no per-100-g/ml column exists and values are per serving, convert them to per 100 g when the serving mass is visible, "
    "or to per 100 ml when the serving volume is visible. "
    "Do not convert between a mass basis and a volume basis unless product density is explicitly provided. "
    "If a serving value cannot be converted to either basis without guessing, return null. "
    "Use JSON numbers without units or text for nutrition, weight, and volume. "
    "Energy may be printed in both kJ and kcal, often next to each other. The kcal field must contain kilocalories, never the kJ number. "
    "When both are present, copy the explicitly labeled kcal value. If only kJ is clearly present, convert it to kcal by dividing by 4.184. "
    "Use grams for macronutrients. "
    "Convert comma decimal separators to dots and do not round values. "
    "Extract saturated fat, sugars, fiber, and salt only when clearly present. "
    "Use null for every missing or uncertain scalar value. Do not invent values."
)


### ------------------------------------ Text Recognition ------------------------------------ ###

def process_image(image):
    metadata = {}

    with open(image, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")  # preparing the file

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

    output_file = os.path.join(
        RESULT_DIR_PATH,
        os.path.splitext(os.path.basename(image))[0] + ".json"
    )

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
                "total_duration": data.get("total_duration", 0),
                "prompt_eval_duration": data.get("prompt_eval_duration", 0),
                "eval_duration": data.get("eval_duration", 0),
            }

    result = json.loads("".join(response_parts))
    result["image"] = os.path.basename(image)
    result["model"] = MODEL

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    return metadata


### ------------------------------------ Timer and metadata records ------------------------------------ ###

def measure_runtime(func, *args, **kwargs): # timer
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    return result, end - start

timing_results = {}


### ------------------------------------ Main Loop ------------------------------------ ###

for image in tqdm(os.listdir(IMAGE_DIR_PATH)):                  # tqdm for progress bar
    if not image.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(IMAGE_DIR_PATH, image)

    try:
        metadata, elapsed = measure_runtime(process_image, image_path)

        timing_results[image] = {
            "elapsed": elapsed,
            "prompt_tokens": metadata.get("prompt_tokens", 0),
            "output_tokens": metadata.get("output_tokens", 0),
        }
        print(f"Processed {image}: {elapsed:.2f} seconds")

    except Exception as e:
        print(f"Failed: {image}: {e}")
        continue


### ----------------- Writing processing time and token cost into scores.md--------------------------- ###

with open(SCORES_DIR_PATH, "a", encoding="utf-8") as f:     
    f.write(f"\n\n# Model timing: {MODEL}\n\n")

    for image_name, data in timing_results.items():
        f.write(
            f"{image_name}: "
            f"{data['elapsed']:.2f} seconds, "
            f"prompt tokens: {data['prompt_tokens']}, "
            f"output tokens: {data['output_tokens']}\n"
        )

    if timing_results:
        total_time = sum(data["elapsed"] for data in timing_results.values())
        avg_time = total_time / len(timing_results)
        f.write(f"\nAverage runtime: **{avg_time:.2f}** sec\n")
        f.write(f"Total runtime: **{total_time:.2f}** sec\n")



#--------------------------- RESULTS 12b ------------------------------------------------------

# Failed:   cheese, metat, milk(wrong), redbull(hallucinated Kcal), sausages, softcheese(?)
# Passed:   bread, carrots, cocomilk, cookie, nutsandseeds, pesto, test, waffle
# 8/14, ~57% success rate

#--------------------------- RESULTS 72b ------------------------------------------------------

# Failed:   cheese
# Passed:   bread, carrots, 
# /14, ~% success rate
