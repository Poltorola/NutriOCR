### ----------------------- GPT-5 image recognition ----------------------- ###

from openai import OpenAI
import base64
import os
from tqdm import tqdm

IMAGE_DIR_PATH = "/home/k3l/projects/NutriOCR/input_photos/"
RESULT_DIR_PATH = "/home/k3l/projects/NutriOCR/results_gpt5"

client = OpenAI()

os.makedirs(RESULT_DIR_PATH, exist_ok=True)


def process_image(image_path):
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")

    response = client.responses.create(
        model="gpt-5",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "Extract all visible text from this image. "
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


for image_name in tqdm(os.listdir(IMAGE_DIR_PATH)):

    if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(IMAGE_DIR_PATH, image_name)

    try:
        text = process_image(image_path)
    except Exception as e:
        print(f"Failed: {image_name}: {e}")
        continue

    output_file = os.path.join(
        RESULT_DIR_PATH,
        os.path.splitext(image_name)[0] + ".md"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)