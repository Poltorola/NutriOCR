### ----------------------- GPT-5 Text Recognition ----------------------- ###

from openai import OpenAI
import base64
import os
from tqdm import tqdm
import time
import json
from io import BytesIO
from PIL import Image, ImageOps
import cv2
import numpy as np

IMAGE_DIR_PATH = "/home/k3l/projects/NutriOCR/input_photos/"
RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gpt5"
SCORES_DIR_PATH = "/home/k3l/projects/NutriOCR/model_scores.md"

client = OpenAI()

os.makedirs(RESULT_DIR_PATH, exist_ok=True)

### ------------------------------------ Image Preparation ------------------------------------ ###

def rotate_image(image, degrees):
    if degrees == 90:
        return image.rotate(-90, expand=True)
    if degrees == 180:
        return image.rotate(180, expand=True)
    if degrees == 270:
        return image.rotate(90, expand=True)
    return image


def horizontal_text_score(image): # grayscale, resize, searches contours of text lines
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    height, width = cv_image.shape[:2]
    scale = 1000 / max(height, width)
    if scale < 1:
        cv_image = cv2.resize(cv_image, (int(width * scale), int(height * scale)))

    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        31,
        15,
    )
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 3))
    closed = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    score = 0
    image_area = gray.size
    for contour in contours:
        _, _, box_width, box_height = cv2.boundingRect(contour)
        box_area = box_width * box_height
        if box_area < 100 or box_area > image_area * 0.1:
            continue
        if box_width < 8 or box_height < 5:
            continue

        aspect_ratio = box_width / box_height
        if aspect_ratio > 1.5:
            score += box_area * min(aspect_ratio, 8)

    return score


def auto_orient_image(image):   # rotates the image according to text lines
    scored_variants = []
    for degrees in (0, 90, 180, 270):
        variant = rotate_image(image, degrees)
        scored_variants.append((horizontal_text_score(variant), degrees, variant))

    scored_variants.sort(key=lambda item: item[0], reverse=True)
    best_score, _, best_image = scored_variants[0]
    original_score = next(score for score, degrees, _ in scored_variants if degrees == 0)

    if best_score > original_score * 1.5:
        return best_image

    return image


def build_image_input(image_path):
    with Image.open(image_path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image = auto_orient_image(image)
        buffer = BytesIO()
        image.save(buffer, format="JPEG", quality=90)

    image_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return {
        "type": "input_image",
        "image_url": f"data:image/jpeg;base64,{image_b64}",
    }


### ------------------------------------ Text Recognition ------------------------------------ ###

def process_image(image_path):
    image_input = build_image_input(image_path)

    response = client.responses.create(
        model="gpt-5",
        input=[             # prompt
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "Extract nutrition information from the product label image. "
                            "The label may use different languages, including English, Russian, Kazakh, or others. "
                            "Nutrition data may appear in a table, paragraph, pie chart, icon, illustration, or mixed layout. "
                            "Extract the visible product name, company/manufacturer name, and barcode when visible. "
                            "Return barcode as digits only, preserving leading zeros. "
                            "Extract net product weight from package-size text such as net weight, net wt, масса нетто, салмағы, or вес нетто. "
                            "Extract product volume from package-size text such as volume, объем, объём, көлемі, ml, мл, l, or л. "
                            "Return net_weight_g in grams and volume_ml in milliliters as JSON numbers only. "
                            "Do not use nutrition serving size or per-100-g/per-100-ml table headers as net_weight_g or volume_ml. "
                            "Extract energy/calories and macronutrients where visible. "
                            "Return nutrition values normalized per 100 g of product. "
                            "If the label gives values per serving and the serving weight in grams is visible, convert them to per 100 g. "
                            "If a value cannot be converted to per 100 g without guessing, use null. "
                            "Return only JSON numbers in nutrition fields: no units, no text, no ranges, no explanations. "
                            "Use grams for macronutrients and kcal for energy. "
                            "Use a dot as the decimal separator, for example 4.7, even when the label uses a comma. "
                            "Do not round converted or extracted values. "
                            "Fat may appear as total fat, saturated fat, or other subcategories. "
                            "Carbohydrates may include sugars or fiber. "
                            "Preserve all visible text in recognized_text. "
                            "Use null for product name, company name, barcode, net weight, or volume if not visible or uncertain. "
                            "Do not invent missing values; use null if a value is not visible or uncertain."
                        ),
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
                "schema": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "recognized_text": {
                            "type": "string"
                        },
                        "product_name": {
                            "type": ["string", "null"]
                        },
                        "company_name": {
                            "type": ["string", "null"]
                        },
                        "barcode": {
                            "type": ["string", "null"]
                        },
                        "net_weight_g": {
                            "type": ["number", "null"]
                        },
                        "volume_ml": {
                            "type": ["number", "null"]
                        },
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
                                "kcal",
                                "protein_g",
                                "fat_g",
                                "saturated_fat_g",
                                "carbs_g",
                                "sugars_g",
                                "fiber_g",
                                "salt_g"
                            ]
                        }
                    },
                    "required": [
                        "recognized_text",
                        "product_name",
                        "company_name",
                        "barcode",
                        "net_weight_g",
                        "volume_ml",
                        "nutrition"
                    ]
                }
            }
        }
    )

    data = json.loads(response.output_text)

    data["image"] = os.path.basename(image_path)
    data["model"] = "gpt-5"

    metadata = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "total_tokens": response.usage.total_tokens,
    }
    
    return data, metadata


### ------------------------------------ Timer and metadata records ------------------------------------ ###

def measure_runtime(func, *args, **kwargs): # timer
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    return result, end - start

timing_results = {}


### ------------------------------------ Main Loop ------------------------------------ ###

for image_name in tqdm(os.listdir(IMAGE_DIR_PATH)):     # progress bar

    if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(IMAGE_DIR_PATH, image_name)   

    try:
        (result, metadata), elapsed = measure_runtime(process_image, image_path)    # time and tokens
        text = result
        timing_results[image_name] = {
            "elapsed": elapsed,
            "input_tokens": metadata["input_tokens"],
            "output_tokens": metadata["output_tokens"],
            "total_tokens": metadata["total_tokens"],
        }
    except Exception as e:
        print(f"Failed: {image_name}: {e}")
        continue

    output_file = os.path.join(                 # creating output file
        RESULT_DIR_PATH,
        os.path.splitext(image_name)[0] + ".json"
    )

    data = text                 # here was jsonification, now it's inside process_image()
    data["image"] = image_name
    data["model"] = "gpt-5"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


### ----------------- Writing processing time and token cost into scores.md--------------------------- ###

with open(SCORES_DIR_PATH, "a", encoding="utf-8") as f:
    f.write("# Model timing: GPT-5\n\n")

    for image_name, data in timing_results.items():  # writing processing time & tokens into scores.md
        f.write(
            f"{image_name}: "
            f"{data['elapsed']:.2f} seconds, "
            f"input tokens: {data['input_tokens']}, "
            f"output tokens: {data['output_tokens']}, "
            f"total tokens: {data['total_tokens']}\n"
        )  

    if timing_results:
        total_time = sum(data["elapsed"] for data in timing_results.values())
        avg_time = total_time / len(timing_results)
        f.write(f"\nAverage runtime: **{avg_time:.2f}** sec\n")
        f.write(f"Total runtime: **{total_time:.2f}** sec\n")
