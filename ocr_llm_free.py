import requests
import base64
import json

IMAGE_PATH = "/home/k3l/projects/NutriOCR/input_photos/test.jpg"

with open(IMAGE_PATH, "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

r = requests.post(
    "http://172.19.48.1:11434/api/chat",
    json={
        "model": "gemma3:27b-it-q4_K_M", #"gemma3:12b-it-q8_0",
        "messages": [
            {
                "role": "user",
                "content": "Extract all text from this image.",
                "images": [
                    image_b64
                ]
            }
        ]
    }
)

# print(r.text)
for line in r.text.split('\n'):
    if not line:
        continue
    try:
        print(json.loads(line)["message"]["content"], end="")
    except:
        print("-" * 50)
        print(line)
        print("-" * 50)