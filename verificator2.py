"""Build comparative Markdown tables for nutrition extraction models."""

import argparse
import json
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
VERIFIED_PATH = PROJECT_DIR / "verified_nutrients.json"
DEFAULT_REPORT_PATH = PROJECT_DIR / "model_comparison.md"

MODELS = {
    "gpt5": PROJECT_DIR / "results_gpt5",
    "gemma3:12": PROJECT_DIR / "results_gemma3_12",
    "gemma3:26": PROJECT_DIR / "results_gemma3_26",
    "gemma4:12": PROJECT_DIR / "results_gemma4_12",
    "gemma4:26": PROJECT_DIR / "results_gemma4_26",
    "gemma4:31": PROJECT_DIR / "results_gemma4_31",
    "gemma4:e4b": PROJECT_DIR / "results_gemma4_e4b",
    "paddle": PROJECT_DIR / "results_json_paddleocr",
}

ATTRIBUTES = ("kcal", "protein", "fat", "carbs")
EXPECTED_KEYS = {
    "kcal": "kcal",
    "protein": "prots",
    "fat": "fats",
    "carbs": "carbs",
}
RESULT_KEYS = {
    "kcal": "kcal",
    "protein": "protein_g",
    "fat": "fat_g",
    "carbs": "carbs_g",
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_model_results(results_dir, test_names):
    results = {}
    errors = {}

    for test_name in test_names:
        result_path = results_dir / f"{test_name}.json"
        if not result_path.exists():
            results[test_name] = None
            errors[test_name] = "file is missing"
            continue

        try:
            results[test_name] = load_json(result_path)
        except (OSError, json.JSONDecodeError) as exc:
            results[test_name] = None
            errors[test_name] = str(exc)

    return results, errors


def result_value(result, attribute):
    if not isinstance(result, dict):
        return None

    nutrition = result.get("nutrition")
    if isinstance(nutrition, dict):
        return nutrition.get(RESULT_KEYS[attribute])

    # Compatibility with older flat PaddleOCR JSON files.
    old_keys = {
        "kcal": "kcal",
        "protein": "prots",
        "fat": "fats",
        "carbs": "carbs",
    }
    return result.get(old_keys[attribute])


def expected_value(expected, attribute):
    return expected.get(EXPECTED_KEYS[attribute])


def values_equal(actual, expected, tolerance=1e-9):
    if actual is None or expected is None:
        return actual is expected

    try:
        return abs(float(actual) - float(expected)) <= tolerance
    except (TypeError, ValueError):
        return str(actual).strip() == str(expected).strip()


def format_value(value):
    if value is None:
        return "—"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def processing_time(result):
    if not isinstance(result, dict):
        return None

    value = result.get("processing_time_seconds")
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None

    return value if value >= 0 else None


def markdown_table(headers, rows):
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend("| " + " | ".join(map(str, row)) + " |" for row in rows)
    return "\n".join(lines)


def build_values_table(verified, model_results):
    headers = ["test"]
    headers.extend(f"original {attribute}" for attribute in ATTRIBUTES)
    for model_name in MODELS:
        headers.extend(f"{model_name} {attribute}" for attribute in ATTRIBUTES)

    rows = []
    for test_name, expected in verified.items():
        row = [test_name]
        row.extend(format_value(expected_value(expected, attribute)) for attribute in ATTRIBUTES)
        for model_name in MODELS:
            result = model_results[model_name][test_name]
            row.extend(format_value(result_value(result, attribute)) for attribute in ATTRIBUTES)
        rows.append(row)

    return markdown_table(headers, rows)


def test_model_stats(verified, model_results):
    rows = []
    summary = {
        model_name: {
            "full": 0,
            "correct": 0,
            "total": 0,
            "testing_time": 0.0,
            "timed_tests": 0,
        }
        for model_name in MODELS
    }

    for test_name, expected in verified.items():
        evaluated_attributes = [
            attribute
            for attribute in ATTRIBUTES
            if expected_value(expected, attribute) is not None
        ]
        row = [test_name]
        models_passed = 0

        for model_name in MODELS:
            result = model_results[model_name][test_name]
            elapsed = processing_time(result)
            if elapsed is not None:
                summary[model_name]["testing_time"] += elapsed
                summary[model_name]["timed_tests"] += 1

            correct = sum(
                values_equal(
                    result_value(result, attribute),
                    expected_value(expected, attribute),
                )
                for attribute in evaluated_attributes
            )
            total = len(evaluated_attributes)
            percent = correct / total * 100 if total else 0.0
            row.append(f"{percent:.2f}% ({correct}/{total})")

            summary[model_name]["correct"] += correct
            summary[model_name]["total"] += total
            if total and correct == total:
                summary[model_name]["full"] += 1
                models_passed += 1

        passed_percent = models_passed / len(MODELS) * 100 if MODELS else 0.0
        row.append(f"{passed_percent:.2f}% ({models_passed}/{len(MODELS)})")
        rows.append(row)

    return rows, summary


def build_summary_table(summary, test_count):
    rows = []
    for model_name, stats in summary.items():
        full_percent = stats["full"] / test_count * 100 if test_count else 0.0
        attribute_percent = (
            stats["correct"] / stats["total"] * 100
            if stats["total"]
            else 0.0
        )
        if stats["timed_tests"]:
            average_testing_time = (
                stats["testing_time"] / stats["timed_tests"]
            )
            testing_time = f"{average_testing_time:.2f} s"
            if stats["timed_tests"] != test_count:
                testing_time += f" ({stats['timed_tests']}/{test_count} tests)"
        else:
            testing_time = "—"

        rows.append([
            model_name,
            f"{full_percent:.2f}% ({stats['full']}/{test_count})",
            f"{attribute_percent:.2f}% ({stats['correct']}/{stats['total']})",
            testing_time,
        ])

    return markdown_table(
        [
            "model",
            "fully recognized images",
            "correct attributes across all images",
            "average testing time",
        ],
        rows,
    )


def build_report():
    verified = load_json(VERIFIED_PATH)
    model_results = {}
    all_errors = {}

    for model_name, results_dir in MODELS.items():
        model_results[model_name], errors = load_model_results(results_dir, verified)
        if errors:
            all_errors[model_name] = errors

    detail_rows, summary = test_model_stats(verified, model_results)
    sections = [
        "# Model comparison",
        "",
        "## Final summary",
        "",
        build_summary_table(summary, len(verified)),
        "",
        "## Accuracy by test and model",
        "",
        markdown_table(["test", *MODELS.keys(), "models passed"], detail_rows),
    ]

    if all_errors:
        sections.extend(["", "## Missing or invalid results", ""])
        for model_name, errors in all_errors.items():
            for test_name, error in errors.items():
                sections.append(f"- {model_name} / {test_name}: {error}")

    sections.extend([
        "",
        "## Extracted values",
        "",
        build_values_table(verified, model_results),
    ])

    return "\n".join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help=f"Markdown report path (default: {DEFAULT_REPORT_PATH.name})",
    )
    args = parser.parse_args()

    report = build_report()
    args.output.write_text(report, encoding="utf-8")
    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
