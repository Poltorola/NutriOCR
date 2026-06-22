# --------------------------------- Gemma3 12b or 27b Text Recognition --------------------------------- #

# 11.06: extract photo from folder => feed to Gemma3 through Ollama => save the transcripted output

import requests
import base64
import json
import os
from tqdm import tqdm
import time


IMAGE_DIR_PATH = "/home/k3l/projects/NutriOCR/input_photos/"
RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gemma12b"
# RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gemma27b"

SCORES_DIR_PATH = "/home/k3l/projects/NutriOCR/model_scores.md"

MODEL = "gemma3:12b-it-q8_0"
# MODEL = "gemma3:27b-it-q4_K_M"


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
                    "content": "Extract macronutrients and weight or volume from this label.",
                    "images": [
                        image_b64
                    ]
                }
            ]
        },
        stream=True
    )

    output_file = os.path.join(
        RESULT_DIR_PATH,
        os.path.splitext(os.path.basename(image))[0] + ".md"    # creating a file for each result
    )

    with open(output_file, "w", encoding="utf-8") as f:
        for line in r.iter_lines(decode_unicode=True):
            if not line:
                continue

            try:
                data = json.loads(line)             # gets Ollama output
                    
                token = data.get("message", {}).get("content", "")

                if token:
                    f.write(token)  # writes into file
                    f.flush()       # streaming writing

                if data.get("done"):
                    metadata = {
                        "prompt_tokens": data.get("prompt_eval_count", 0),
                        "output_tokens": data.get("eval_count", 0),
                        "total_duration": data.get("total_duration", 0),
                        "prompt_eval_duration": data.get("prompt_eval_duration", 0),
                        "eval_duration": data.get("eval_duration", 0),
                    }
                #print(token, end="", flush=True)   # online print in terminal                        

            except Exception as e:
                print("-" * 50)
                print(line)
                print(e)
                print("-" * 50)
    return metadata


### ------------------------------------ Timer and metadata records ------------------------------------ ###

def measure_runtime(func, *args, **kwargs): # timer
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    return result, end - start

timing_results = {}


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
        avg_time = sum(data["elapsed"] for data in timing_results.values()) / len(timing_results)
        f.write(f"\nAverage runtime: **{avg_time:.2f}** sec\n")
        f.write(f"Total runtime: **{sum(timing_results.values()):.2f}** sec\n")



#--------------------------- RESULTS 12b ------------------------------------------------------

# Failed:   cheese, metat, milk(wrong), redbull(hallucinated Kcal), sausages, softcheese(?)
# Passed:   bread, carrots, cocomilk, cookie, nutsandseeds, pesto, test, waffle
# 8/14, ~57% success rate

#--------------------------- RESULTS 72b ------------------------------------------------------

# Failed:   cheese
# Passed:   bread, carrots, 
# /14, ~% success rate



