# ------------------------- paddleOCR Text Recognition ------------------------------------- #

# 09.06: extract photo from folder => feed to PaddleOCR => save the transcripted output

### CPU version
# paddlepaddle==3.2.0 paddleocr==3.3.3

from pathlib import Path
from paddleocr import PaddleOCR, PPStructureV3
import time
# import psutil

ocr = PPStructureV3(
    text_recognition_model_name="cyrillic_PP-OCRv5_mobile_rec"
)
#ocr = PPStructureV3()


input_dir = Path("input_photos")
output_dir = Path("results_paddleocr")
scores_file = Path("model_scores.md")

output_dir.mkdir(exist_ok=True)

timing_results = {}


def measure_runtime(func, *args, **kwargs): # timer
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()

    return result, end - start

### ------------------------------------ Text Recognition ------------------------------------ ###

def process_image(image_path):
    result = ocr.predict(str(image_path))   # call PaddleOCR

    page = result[0]

    output_file = output_dir / f"{image_path.stem}.md"  # creating a file for descpipted text
    page.save_to_markdown(save_path=output_file)

    return output_file



### ------------------------------------ Main Loop ------------------------------------ ###

for image_path in input_dir.glob("*"):
    if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:  # skip non-images
        continue

    try:
        output_file, elapsed = measure_runtime(process_image, image_path)   # recognition + timer
        timing_results[image_path.name] = elapsed

        print(f"Processed {image_path.name}: {elapsed:.2f} seconds")

    except Exception as e:
        print(f"Failed: {image_path.name}: {e}")
        continue


### ---------------------- Writing processing time into scores.md ---------------------------- ###

with open(scores_file, "a", encoding="utf-8") as f:
    f.write("\n\n# Model timing: PaddleOCR\n\n")

    for image_name, elapsed in timing_results.items():
        f.write(f"{image_name}: {elapsed:.2f} sec\n")       # 

    if timing_results:
        avg_time = sum(timing_results.values()) / len(timing_results)
        f.write(f"\nAverage runtime: **{avg_time:.2f}** sec\n")
        f.write(f"Total runtime: **{sum(timing_results.values()):.2f}** sec\n")





#--------------------------- RESULTS hooman-verified ------------------------------------------------------

# Failed:   bread, carrots, cheese, cocomilk, milk, nutsandseeds(partly), waffle(one number), softcheese(no result)
# Passed:   cookie, metat, pesto(ugly), redbull, sausages, test(cola)
# 6/14, ~42% success rate