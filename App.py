# Main NutriOCR App file

# 09.06: extract photo from folder => feed to PaddleOCR => save the transcripted output

### CPU version
# paddlepaddle==3.2.0 paddleocr==3.3.3

# from pathlib import Path
# from paddleocr import PPStructureV3

# ocr = PPStructureV3(device="cpu")

# input_dir = Path("input_photos")
# output_dir = Path("results")
# output_dir.mkdir(exist_ok=True)

# for image_path in input_dir.glob("*"):
#     if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
#         continue

#     result = ocr.predict(str(image_path))

#     for i, page in enumerate(result):
#         output_file = output_dir / f"{image_path.stem}_{i}.md"
#         page.save_to_markdown(save_path=output_file)

#     print(f"Processed {image_path.name}")

from pathlib import Path
from paddleocr import PaddleOCR, PPStructureV3

ocr = PaddleOCR()
#ocr = PPStructureV3()

input_dir = Path("input_photos")
output_dir = Path("results")

output_dir.mkdir(exist_ok=True)

for image_path in input_dir.glob("*"):                              # iterating on files in input
    if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:  # only photos
        continue

    result = ocr.predict(str(image_path))   # model processing

    text_lines = []
    # page = result[0]
    output_file = output_dir / f"{image_path.stem}.md"
    # page.save_to_markdown(save_path=output_file)

    # print(page)

    for page in result:
        for line in page["rec_texts"]:
            text_lines.append(line)

    full_text = "\n".join(text_lines)


    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"Processed {image_path.name}")
