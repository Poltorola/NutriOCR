from pathlib import Path
from openai import OpenAI
import base64

IMAGE_PATH = "/home/k3l/projects/NutriOCR/input_photos/test.jpg"

client = OpenAI()

with open(IMAGE_PATH, "rb") as f:
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

print(response.output_text)