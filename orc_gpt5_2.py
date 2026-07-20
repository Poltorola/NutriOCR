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
RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gpt5_2"
FIRST_PASS_RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gpt5_2_first_pass"
SCORES_DIR_PATH = "/home/k3l/projects/NutriOCR/model_scores/model_scores.md"
IMAGE_NAME_FILTER = None  # Example: {"cheese.jpg"}
MAX_TEXT_CROPS = 4
SAVE_DEBUG_CROPS = False
DEBUG_CROPS_DIR_PATH = "/home/k3l/projects/NutriOCR/debug_crops_gpt5_2"

client = OpenAI()

os.makedirs(RESULT_DIR_PATH, exist_ok=True)
os.makedirs(FIRST_PASS_RESULT_DIR_PATH, exist_ok=True)
if SAVE_DEBUG_CROPS:
    os.makedirs(DEBUG_CROPS_DIR_PATH, exist_ok=True)

### ------------------------------------ Text Recognition ------------------------------------ ###

def rotate_image(image, degrees):
    if degrees == 90:
        return image.rotate(-90, expand=True)
    if degrees == 180:
        return image.rotate(180, expand=True)
    if degrees == 270:
        return image.rotate(90, expand=True)
    return image

def horizontal_text_score(image):
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

def auto_orient_image(image):
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

def resize_for_api(image, max_side):
    width, height = image.size
    scale = max_side / max(width, height)
    if scale >= 1:
        return image

    new_size = (int(width * scale), int(height * scale))
    return image.resize(new_size, Image.Resampling.LANCZOS)

def upscale_crop(image, factor=2):
    width, height = image.size
    return image.resize((width * factor, height * factor), Image.Resampling.LANCZOS)

def encode_image(image, max_side=1800):
    image = resize_for_api(image, max_side=max_side)
    buffer = BytesIO()
    image.save(buffer, format="JPEG", quality=90)
    image_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return {
        "type": "input_image",
        "image_url": f"data:image/jpeg;base64,{image_b64}",
    }

def overlaps_or_near(first, second, gap):
    left_a, top_a, right_a, bottom_a = first
    left_b, top_b, right_b, bottom_b = second
    return not (
        right_a + gap < left_b
        or right_b + gap < left_a
        or bottom_a + gap < top_b
        or bottom_b + gap < top_a
    )

def merge_boxes(boxes, gap):
    merged = []
    for box in boxes:
        current = box
        changed = True
        while changed:
            changed = False
            next_merged = []
            for existing in merged:
                if overlaps_or_near(current, existing, gap):
                    current = (
                        min(current[0], existing[0]),
                        min(current[1], existing[1]),
                        max(current[2], existing[2]),
                        max(current[3], existing[3]),
                    )
                    changed = True
                else:
                    next_merged.append(existing)
            merged = next_merged
        merged.append(current)

    return merged

def expand_box(box, image_width, image_height, padding):
    left, top, right, bottom = box
    return (
        max(0, left - padding),
        max(0, top - padding),
        min(image_width, right + padding),
        min(image_height, bottom + padding),
    )

def text_boxes_for_orientation(image, orientation):
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image_height, image_width = cv_image.shape[:2]
    scale = 1400 / max(image_height, image_width)
    if scale < 1:
        resized = cv2.resize(cv_image, (int(image_width * scale), int(image_height * scale)))
    else:
        resized = cv_image
        scale = 1

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        31,
        15,
    )

    if orientation == "horizontal":
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 5))
        min_aspect_ratio = 1.8
    else:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 25))
        min_aspect_ratio = 1.8

    closed = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    boxes = []
    resized_area = gray.size
    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)
        area = width * height
        if area < resized_area * 0.0004 or area > resized_area * 0.25:
            continue

        aspect_ratio = width / height if orientation == "horizontal" else height / width
        if aspect_ratio < min_aspect_ratio:
            continue

        original_box = (
            int(x / scale),
            int(y / scale),
            int((x + width) / scale),
            int((y + height) / scale),
        )
        boxes.append(original_box)

    boxes = merge_boxes(boxes, gap=max(image_width, image_height) // 40)
    boxes = [
        expand_box(box, image_width, image_height, padding=max(image_width, image_height) // 60)
        for box in boxes
    ]

    return boxes

def crop_score(box):
    left, top, right, bottom = box
    width = right - left
    height = bottom - top
    area = width * height
    aspect_ratio = max(width / max(height, 1), height / max(width, 1))
    return area * min(aspect_ratio, 6)

def smart_text_crops(image):
    image_width, image_height = image.size
    image_area = image_width * image_height
    candidates = []

    for box in text_boxes_for_orientation(image, "horizontal"):
        left, top, right, bottom = box
        area = (right - left) * (bottom - top)
        if area < image_area * 0.015 or area > image_area * 0.65:
            continue
        candidates.append((crop_score(box), "horizontal", box))

    for box in text_boxes_for_orientation(image, "vertical"):
        left, top, right, bottom = box
        area = (right - left) * (bottom - top)
        if area < image_area * 0.015 or area > image_area * 0.65:
            continue
        candidates.append((crop_score(box), "vertical", box))

    candidates.sort(key=lambda item: item[0], reverse=True)

    crops = []
    used_boxes = []
    for _, orientation, box in candidates:
        if any(overlaps_or_near(box, used_box, gap=max(image_width, image_height) // 30) for used_box in used_boxes):
            continue

        crop = image.crop(box)
        if orientation == "vertical":
            crop = crop.rotate(-90, expand=True)

        crops.append((orientation, upscale_crop(crop)))
        used_boxes.append(box)

        if len(crops) >= MAX_TEXT_CROPS:
            break

    return crops

def build_full_image_inputs(image_path):
    with Image.open(image_path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image = auto_orient_image(image)

        return [
            {"type": "input_text", "text": "Full product photo:"},
            encode_image(image, max_side=1800),
        ]

def build_crop_image_inputs(image_path):
    with Image.open(image_path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image = auto_orient_image(image)

        image_inputs = []
        for index, (orientation, crop) in enumerate(smart_text_crops(image), start=1):
            if SAVE_DEBUG_CROPS:
                crop.save(
                    os.path.join(
                        DEBUG_CROPS_DIR_PATH,
                        f"{os.path.splitext(os.path.basename(image_path))[0]}_crop_{index}_{orientation}.jpg",
                    ),
                    quality=90,
                )
            image_inputs.extend([
                {
                    "type": "input_text",
                    "text": f"Detected text crop {index} ({orientation}, enlarged for readability):",
                },
                encode_image(crop, max_side=1800),
            ])

        return image_inputs

def nutrition_schema_format():
    return {
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
                    },
                    "extraction_quality": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "score": {
                                "type": "number"
                            },
                            "needs_retry": {
                                "type": "boolean"
                            },
                            "retry_reason": {
                                "type": ["string", "null"]
                            }
                        },
                        "required": [
                            "score",
                            "needs_retry",
                            "retry_reason"
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
                    "nutrition",
                    "extraction_quality"
                ]
            }
        }
    }

def base_prompt():
    return (
        "Extract nutrition information from the product label image. "
        "The label may use any language, including multiple languages in parallel. "
        "Use equivalent text in another language on the same label to recover a field when one version is blurred or poorly recognized. "
        "Cross-check translations and repeated nutrition panels, but do not combine values from different products or unrelated sections. "
        "Nutrition data may appear in a table, paragraph, pie chart, icon, illustration, or mixed layout. "
        "Extract the visible product name, company/manufacturer name, and barcode when visible. "
        "Return barcode as digits only, preserving leading zeros. "
        "Extract net product weight from package-size text such as net weight, net wt, масса нетто, салмағы, or вес нетто. "
        "Extract product volume from package-size text such as volume, объем, объём, көлемі, ml, мл, l, or л. "
        "Return net_weight_g in grams and volume_ml in milliliters as JSON numbers only. "
        "Do not use nutrition serving size or per-100-g/per-100-ml table headers as net_weight_g or volume_ml. "
        "Extract energy/calories and macronutrients where visible. "
        "Return nutrition values per 100 g when the label uses a mass basis, or per 100 ml when it uses a volume basis. "
        "Both per-100-g and per-100-ml nutrition values are valid. "
        "Nutrition tables may show adjacent columns for per 100 g/ml, per serving, per package, and percent daily intake. "
        "Read the column headers carefully and select the explicitly labeled per-100-g or per-100-ml column. "
        "Never take values from a serving, whole-package, or percent-daily-intake column when a per-100-g/ml column is present. "
        "If no per-100-g/ml column exists and the label gives values per serving, convert them to per 100 g when the serving mass is visible, "
        "or to per 100 ml when the serving volume is visible. "
        "Do not convert between a mass basis and a volume basis unless product density is explicitly provided. "
        "If a serving value cannot be converted to either basis without guessing, use null. "
        "Return only JSON numbers in nutrition fields: no units, no text, no ranges, no explanations. "
        "Energy may be printed in both kJ and kcal, often next to each other. The kcal field must contain kilocalories, never the kJ number. "
        "When both are present, copy the explicitly labeled kcal value. If only kJ is clearly present, convert it to kcal by dividing by 4.184. "
        "Use grams for macronutrients. "
        "Use a dot as the decimal separator, for example 4.7, even when the label uses a comma. "
        "Do not round converted or extracted values. "
        "Fat may appear as total fat, saturated fat, or other subcategories. "
        "Carbohydrates may include sugars or fiber. "
        "Transcribe only text that is actually visible into recognized_text; do not reconstruct or invent unreadable text. "
        "Use null for product name, company name, barcode, net weight, or volume if not visible or uncertain. "
        "Do not invent missing values; use null if a value is not visible or uncertain. "
        "In extraction_quality, score the overall extraction quality from 0 to 1. "
        "Set extraction_quality.needs_retry to true if important nutrition facts, barcode, product name, net weight, or manufacturer "
        "are likely present on the package but not confidently extracted because text is too small, curved, vertical, blurred, rotated, glared, or cropped. "
        "Set needs_retry to false when the important visible fields were extracted confidently or are genuinely not visible. "
        "Use retry_reason to briefly explain why another pass with close-up crops is or is not needed."
    )

def run_gpt_pass(image_inputs, prompt):
    response = client.responses.create(
        model="gpt-5",
        input=[             # prompt
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt,
                    },
                    *image_inputs,
                ],
            }
        ],
        text=nutrition_schema_format()
    )

    data = json.loads(response.output_text)
    metadata = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "total_tokens": response.usage.total_tokens,
    }
    
    return data, metadata

def count_present(values):
    return sum(value is not None for value in values)

def is_good_enough(data):
    nutrition = data["nutrition"]
    core_nutrition_values = [
        nutrition["kcal"],
        nutrition["protein_g"],
        nutrition["fat_g"],
        nutrition["carbs_g"],
    ]
    quality = data["extraction_quality"]

    if quality["needs_retry"]:
        return False

    if quality["score"] < 0.65:
        return False

    if count_present(core_nutrition_values) == 0:
        return False

    return True

def refinement_prompt(first_pass_data):
    return (
        base_prompt()
        + " You are doing a second-pass verification using close-up crops from the same photo. "
        + "The previous JSON draft is provided below. Treat it as the current draft: keep correct values, "
        + "fill missing values when the crops make them visible, and correct a value only if the crops clearly contradict it. "
        + "Do not discard the draft and start over. Update extraction_quality after reviewing the crops; "
        + "set needs_retry to false if the crops resolve the important missing or uncertain fields. "
        + "Return the same JSON schema with the refined result. "
        + "Previous JSON draft: "
        + json.dumps(first_pass_data, ensure_ascii=False, sort_keys=True)
    )

def save_first_pass_result(image_path, data):
    data = dict(data)
    data["image"] = os.path.basename(image_path)
    data["model"] = "gpt-5-full-first-pass"
    output_file = os.path.join(
        FIRST_PASS_RESULT_DIR_PATH,
        os.path.splitext(os.path.basename(image_path))[0] + ".json"
    )
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def process_image(image_path):
    first_pass_data, first_pass_metadata = run_gpt_pass(
        build_full_image_inputs(image_path),
        base_prompt(),
    )
    save_first_pass_result(image_path, first_pass_data)

    used_crop_retry = not is_good_enough(first_pass_data)
    if used_crop_retry:
        crop_inputs = build_full_image_inputs(image_path) + build_crop_image_inputs(image_path)
        final_data, crop_metadata = run_gpt_pass(
            crop_inputs,
            refinement_prompt(first_pass_data),
        )
        final_model = "gpt-5-crops-refine"
    else:
        final_data = first_pass_data
        crop_metadata = {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
        final_model = "gpt-5-full-first-pass"

    final_data["image"] = os.path.basename(image_path)
    final_data["model"] = final_model
    final_data["crop_retry_used"] = used_crop_retry

    metadata = {
        "input_tokens": first_pass_metadata["input_tokens"] + crop_metadata["input_tokens"],
        "output_tokens": first_pass_metadata["output_tokens"] + crop_metadata["output_tokens"],
        "total_tokens": first_pass_metadata["total_tokens"] + crop_metadata["total_tokens"],
        "first_pass_input_tokens": first_pass_metadata["input_tokens"],
        "first_pass_output_tokens": first_pass_metadata["output_tokens"],
        "first_pass_total_tokens": first_pass_metadata["total_tokens"],
        "crop_pass_input_tokens": crop_metadata["input_tokens"],
        "crop_pass_output_tokens": crop_metadata["output_tokens"],
        "crop_pass_total_tokens": crop_metadata["total_tokens"],
        "crop_retry_used": used_crop_retry,
    }

    return final_data, metadata


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
    if IMAGE_NAME_FILTER is not None and image_name not in IMAGE_NAME_FILTER:
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
            "crop_retry_used": metadata["crop_retry_used"],
            "first_pass_total_tokens": metadata["first_pass_total_tokens"],
            "crop_pass_total_tokens": metadata["crop_pass_total_tokens"],
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

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


### ----------------- Writing processing time and token cost into scores.md--------------------------- ###

with open(SCORES_DIR_PATH, "a", encoding="utf-8") as f:
    f.write("# Model timing: GPT-5 with crops\n\n")

    for image_name, data in timing_results.items():  # writing processing time & tokens into scores.md
        f.write(
            f"{image_name}: "
            f"{data['elapsed']:.2f} seconds, "
            f"input tokens: {data['input_tokens']}, "
            f"output tokens: {data['output_tokens']}, "
            f"total tokens: {data['total_tokens']}, "
            f"crop retry: {data['crop_retry_used']}, "
            f"first pass tokens: {data['first_pass_total_tokens']}, "
            f"crop pass tokens: {data['crop_pass_total_tokens']}\n"
        )  

    if timing_results:
        total_time = sum(data["elapsed"] for data in timing_results.values())
        avg_time = total_time / len(timing_results)
        f.write(f"\nAverage runtime: **{avg_time:.2f}** sec\n")
        f.write(f"Total runtime: **{total_time:.2f}** sec\n")
