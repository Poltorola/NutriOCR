EXTRACTION_PROMPT = (
    "Extract structured product and nutrition information from this product-label image. "
    "The label may use any language, including multiple languages in parallel. "
    "Use equivalent text in another language on the same label to recover a field when one version is blurred or poorly recognized. "
    "Cross-check translations and repeated nutrition panels, but do not combine values from different products or unrelated sections. "
    "Nutrition data may appear in a table, paragraph, pie chart, icon, illustration, or mixed layout. "
    "Transcribe only text that is actually visible into recognized_text; do not reconstruct or invent unreadable text. "
    "Extract the visible product name, company/manufacturer name, and barcode. "
    "Return barcode as digits only, preserving leading zeros. "
    "Extract net product weight from package-size text such as net weight, net wt, масса нетто, салмағы, or вес нетто. "
    "Extract product volume from package-size text such as volume, объем, объём, көлемі, ml, мл, l, or л. "
    "Return net_weight_g in grams and volume_ml in milliliters as JSON numbers only. "
    "Convert kilograms to grams and liters to milliliters when necessary. "
    "Do not use nutrition serving size or per-100-g/per-100-ml table headers as net_weight_g or volume_ml. "
    "Extract energy/calories and macronutrients where visible. "
    "Return nutrition values per 100 g when the label uses a mass basis, or per 100 ml when it uses a volume basis. "
    "Both per-100-g and per-100-ml nutrition values are valid. "
    "Nutrition tables may show adjacent columns for per 100 g/ml, per serving, per package, and percent daily intake. "
    "Read the column headers carefully and select the explicitly labeled per-100-g or per-100-ml column. "
    "Never take values from a serving, whole-package, or percent-daily-intake column when a per-100-g/ml column is present. "
    "If no per-100-g/ml column exists and values are per serving, convert them to per 100 g when the serving mass is visible, "
    "or to per 100 ml when the serving volume is visible. "
    "Do not convert between a mass basis and a volume basis unless product density is explicitly provided. "
    "If a serving value cannot be converted to either basis without guessing, return null. "
    "Return only JSON numbers in nutrition, weight, and volume fields: no units, text, ranges, or explanations. "
    "Energy may be printed in both kJ and kcal, often next to each other. "
    "The kcal field must contain kilocalories, never the kJ number. "
    "When both are present, copy the explicitly labeled kcal value. "
    "If only kJ is clearly present, convert it to kcal by dividing by 4.184. "
    "kcal means calories / energy value / энергетическая ценность / ккал. "
    "protein_g means proteins / белки / ақуыз. "
    "fat_g means total fats / жиры / май. "
    "carbs_g means carbohydrates / углеводы / көмірсу. "
    "Use grams for macronutrients. "
    "Convert comma decimal separators to dots, for example 4,7 to 4.7, and do not round values. "
    "Fat may appear as total fat, saturated fat, or other subcategories. "
    "Carbohydrates may include sugars or fiber. "
    "Extract saturated fat, sugars, fiber, and salt only when clearly present. "
    "Use null for every missing or uncertain scalar value, including product name, company name, barcode, net weight, and volume. "
    "Do not invent missing values."
)


OCR_TEXT_SYSTEM_PROMPT = (
    "You extract structured product-label information from multilingual OCR text. "
    "Use only information clearly present in the supplied OCR text. "
    "Do not guess or invent missing values."
)


OCR_TEXT_EXTRACTION_PROMPT = """\
Extract product and nutrition information from this OCR text.

Rules:
- Copy the supplied OCR text verbatim into recognized_text; do not reconstruct unreadable fragments.
- The label may contain any language or several parallel translations.
- Use a clearer equivalent in another language on the same label to recover poorly recognized fields.
- Cross-check translations and repeated nutrition panels, but do not combine values from different products or unrelated sections.
- Extract the product name, company/manufacturer name, and barcode when clearly present in the supplied OCR text.
- Return barcode as digits only, preserving leading zeros.
- Extract net product weight from package-size text such as net weight, net wt, масса нетто, салмағы, or вес нетто.
- Extract product volume from package-size text such as volume, объем, объём, көлемі, ml, мл, l, or л.
- Return net_weight_g in grams and volume_ml in milliliters as JSON numbers only.
- Convert kilograms to grams and liters to milliliters when necessary.
- Do not use nutrition serving size or per-100-g/per-100-ml table headers as net_weight_g or volume_ml.
- Return nutrition values per 100 g when the OCR text uses a mass basis, or per 100 ml when it uses a volume basis.
- Both per-100-g and per-100-ml nutrition values are valid.
- Nutrition tables may show adjacent columns for per 100 g/ml, per serving, per package, and percent daily intake.
- Read the column headers carefully and select the explicitly labeled per-100-g or per-100-ml column.
- Never take values from a serving, whole-package, or percent-daily-intake column when a per-100-g/ml column is present.
- If no per-100-g/ml column exists and values are per serving, convert them to per 100 g when the serving mass is visible, or to per 100 ml when the serving volume is visible.
- Do not convert between a mass basis and a volume basis unless product density is explicitly provided.
- If a serving value cannot be converted to either basis without guessing, return null.
- Energy may be printed in both kJ and kcal, often next to each other. The kcal field must contain kilocalories, never the kJ number.
- When both are present, copy the explicitly labeled kcal value. If only kJ is clearly present, convert it to kcal by dividing by 4.184.
- kcal means calories / energy value / энергетическая ценность / ккал.
- protein_g means proteins / белки / ақуыз.
- fat_g means total fats / жиры / май.
- carbs_g means carbohydrates / углеводы / көмірсу.
- Fat may appear as total fat, saturated fat, or other subcategories.
- Carbohydrates may include sugars or fiber.
- Extract saturated fat, sugars, fiber, and salt only when clearly present.
- Return only JSON numbers in nutrition, weight, and volume fields: no units, text, ranges, or explanations.
- Convert comma decimal separators to dots and do not round values.
- Return null for every missing or uncertain scalar value.
- Do not invent values.

OCR text:
{ocr_text}
"""
