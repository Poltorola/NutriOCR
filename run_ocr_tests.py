"""Run all active NutriOCR model tests sequentially."""

import subprocess
import sys
import time
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent

TESTS = (
    # ("ocr_paddle", "ocr_paddle.py", ()),
    # ("ocr_gpt5", "ocr_gpt5.py", ()),
    # ("gemma3:12", "orc_gemma.py", ("--model", "gemma3:12")),
    ("gemma4:12", "orc_gemma.py", ("--model", "gemma4:12")),
    # ("gemma4:e4b", "orc_gemma.py", ("--model", "gemma4:e4b")),
    # ("gemma3:26", "orc_gemma.py", ("--model", "gemma3:26")),
    ("gemma4:26", "orc_gemma.py", ("--model", "gemma4:26")),
    ("gemma4:31", "orc_gemma.py", ("--model", "gemma4:31")),
)


def run_test(name, script, arguments):
    command = [sys.executable, str(PROJECT_DIR / script), *arguments]
    print(f"\n{'=' * 72}\nStarting {name}\n{'=' * 72}", flush=True)

    started_at = time.perf_counter()
    completed = subprocess.run(command, cwd=PROJECT_DIR, check=False)
    elapsed = time.perf_counter() - started_at

    status = "passed" if completed.returncode == 0 else "failed"
    print(f"Finished {name}: {status} in {elapsed:.2f} seconds", flush=True)
    return completed.returncode, elapsed


def main():
    results = []

    for name, script, arguments in TESTS:
        return_code, elapsed = run_test(name, script, arguments)
        results.append((name, return_code, elapsed))

    verifier_result = run_test("verificator2", "verificator2.py", ())

    print(f"\n{'=' * 72}\nFinal summary\n{'=' * 72}")
    for name, return_code, elapsed in results:
        status = "passed" if return_code == 0 else f"failed (code {return_code})"
        print(f"{name}: {status}, {elapsed:.2f} seconds")

    failed_count = sum(return_code != 0 for _, return_code, _ in results)
    print(f"\nCompleted: {len(results) - failed_count}/{len(results)} tests passed")

    verifier_code, verifier_elapsed = verifier_result
    verifier_status = (
        "passed" if verifier_code == 0 else f"failed (code {verifier_code})"
    )
    print(f"verificator2: {verifier_status}, {verifier_elapsed:.2f} seconds")
    return 1 if failed_count or verifier_code else 0


if __name__ == "__main__":
    raise SystemExit(main())
