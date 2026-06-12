import requests
import base64
import json
import os
from tqdm import tqdm


IMAGE_DIR_PATH = "/home/k3l/projects/NutriOCR/input_photos/"
RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gemma12b"
# RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gemma27b"

MODEL = "gemma3:12b-it-q8_0"
# MODEL = "gemma3:27b-it-q4_K_M"


def process_image(image):
    with open(image, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")

    r = requests.post(
        "http://172.19.48.1:11434/api/chat",
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": "Extract all text from this image.",
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
        os.path.splitext(os.path.basename(image))[0] + ".md"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        for line in r.iter_lines(decode_unicode=True):
            if not line:
                continue

            try:
                data = json.loads(line)
                token = data["message"]["content"]

                #print(token, end="", flush=True)  # вывод онлайн в терминал
                f.write(token)                    # запись в файл
                f.flush()                         # запись онлайн, не ждать конца

            except Exception as e:
                print("-" * 50)
                print(line)
                print(e)
                print("-" * 50)


for image in tqdm(os.listdir(IMAGE_DIR_PATH)):
    process_image(os.path.join(IMAGE_DIR_PATH, image))




#--------------------------- RESULTS 12b ------------------------------------------------------

# Failed:   cheese, metat, milk(wrong), redbull(hallucinated Kcal), sausages, softcheese(?)
# Passed:   bread, carrots, cocomilk, cookie, nutsandseeds, pesto, test, waffle
# 8/14, ~57% success rate

#--------------------------- RESULTS 72b ------------------------------------------------------

# Failed:   cheese
# Passed:   bread, carrots, 
# /14, ~% success rate
