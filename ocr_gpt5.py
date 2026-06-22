### ----------------------- GPT-5 Text Recognition ----------------------- ###

from openai import OpenAI
import base64
import os
from tqdm import tqdm
import time

IMAGE_DIR_PATH = "/home/k3l/projects/NutriOCR/input_photos/"
RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gpt5"
SCORES_DIR_PATH = "/home/k3l/projects/NutriOCR/model_scores.md"

client = OpenAI()

os.makedirs(RESULT_DIR_PATH, exist_ok=True)


def process_image(image_path):
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")

    response = client.responses.create(     # sending image data to gpt-5 by API
        model="gpt-5",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "Extract macronutrients and weight or volume from this label."   # prompt
                            "Preserve line breaks where possible."
                        ),
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{image_b64}",
                    },
                ],
            }
        ],
    )

    return response.output_text


def measure_runtime(func, *args, **kwargs): # timer
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    return result, end - start

timing_results = {}


for image_name in tqdm(os.listdir(IMAGE_DIR_PATH)):     # progress bar

    if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(IMAGE_DIR_PATH, image_name)   

    try:
        text, elapsed = measure_runtime(process_image, image_path)
        timing_results[image_name] = elapsed
    except Exception as e:
        print(f"Failed: {image_name}: {e}")
        continue

    output_file = os.path.join(                 # creating output file
        RESULT_DIR_PATH,
        os.path.splitext(image_name)[0] + ".md"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)


with open(SCORES_DIR_PATH, "w", encoding="utf-8") as f:
    f.write("# Model timing: GPT-5\n\n")

    for image_name, elapsed in timing_results.items():
        f.write(f"{image_name}: {elapsed:.2f} seconds\n")   # writing processing time into scores.md

    if timing_results:
        avg_time = sum(timing_results.values()) / len(timing_results)
        f.write(f"\nAverage runtime: **{avg_time:.2f}** sec\n")
        f.write(f"Total runtime: **{sum(timing_results.values()):.2f}** sec\n")
