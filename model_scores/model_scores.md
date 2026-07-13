
# Model timing: GPT-5

nutsandseeds.jpg: 53.39 seconds, input tokens: 1177, output tokens: 3426, total tokens: 4603
redbull.jpg: 25.69 seconds, input tokens: 1177, output tokens: 1644, total tokens: 2821
bread.jpg: 25.20 seconds, input tokens: 1177, output tokens: 1991, total tokens: 3168
test.jpg: 46.95 seconds, input tokens: 1457, output tokens: 3481, total tokens: 4938
softcheese.jpg: 34.87 seconds, input tokens: 1177, output tokens: 2508, total tokens: 3685
cookie.jpg: 31.92 seconds, input tokens: 1177, output tokens: 2408, total tokens: 3585
cheese.jpg: 20.99 seconds, input tokens: 1457, output tokens: 1651, total tokens: 3108
metat.jpg: 32.81 seconds, input tokens: 1177, output tokens: 2306, total tokens: 3483
carrots.jpg: 32.12 seconds, input tokens: 1457, output tokens: 2539, total tokens: 3996
waffle.jpg: 33.24 seconds, input tokens: 1177, output tokens: 2418, total tokens: 3595
milk.jpg: 43.92 seconds, input tokens: 1177, output tokens: 2959, total tokens: 4136
pesto.jpg: 54.24 seconds, input tokens: 3442, output tokens: 970, total tokens: 4412
sausages.jpg: 32.81 seconds, input tokens: 1177, output tokens: 2061, total tokens: 3238
cocomilk.jpg: 31.60 seconds, input tokens: 1177, output tokens: 2806, total tokens: 3983

Average runtime: **35.70** sec
Total runtime: **499.75** sec

# Model timing: GPT-5 with crops

nutsandseeds.jpg: 24.27 seconds, input tokens: 1324, output tokens: 2088, total tokens: 3412, crop retry: False, first pass tokens: 3412, crop pass tokens: 0
redbull.jpg: 35.89 seconds, input tokens: 4165, output tokens: 3387, total tokens: 7552, crop retry: True, first pass tokens: 3486, crop pass tokens: 4066
bread.jpg: 46.13 seconds, input tokens: 4799, output tokens: 5372, total tokens: 10171, crop retry: True, first pass tokens: 4102, crop pass tokens: 6069
test.jpg: 67.23 seconds, input tokens: 4955, output tokens: 6092, total tokens: 11047, crop retry: True, first pass tokens: 5623, crop pass tokens: 5424
softcheese.jpg: 43.47 seconds, input tokens: 3454, output tokens: 4382, total tokens: 7836, crop retry: True, first pass tokens: 3912, crop pass tokens: 3924
cookie.jpg: 56.74 seconds, input tokens: 4978, output tokens: 5411, total tokens: 10389, crop retry: True, first pass tokens: 4734, crop pass tokens: 5655
cheese.jpg: 48.36 seconds, input tokens: 4547, output tokens: 3642, total tokens: 8189, crop retry: True, first pass tokens: 3501, crop pass tokens: 4688
metat.jpg: 75.54 seconds, input tokens: 4130, output tokens: 7419, total tokens: 11549, crop retry: True, first pass tokens: 4494, crop pass tokens: 7055
carrots.jpg: 45.64 seconds, input tokens: 4831, output tokens: 4286, total tokens: 9117, crop retry: True, first pass tokens: 3676, crop pass tokens: 5441
waffle.jpg: 78.11 seconds, input tokens: 4388, output tokens: 5250, total tokens: 9638, crop retry: True, first pass tokens: 3897, crop pass tokens: 5741
milk.jpg: 63.38 seconds, input tokens: 3090, output tokens: 6181, total tokens: 9271, crop retry: True, first pass tokens: 3914, crop pass tokens: 5357
pesto.jpg: 63.93 seconds, input tokens: 5659, output tokens: 6054, total tokens: 11713, crop retry: True, first pass tokens: 4659, crop pass tokens: 7054
sausages.jpg: 47.03 seconds, input tokens: 4910, output tokens: 4349, total tokens: 9259, crop retry: True, first pass tokens: 3077, crop pass tokens: 6182
cocomilk.jpg: 58.05 seconds, input tokens: 4685, output tokens: 6180, total tokens: 10865, crop retry: True, first pass tokens: 4917, crop pass tokens: 5948

Average runtime: **53.84** sec
Total runtime: **753.77** sec


# ---------------------- Model scores: gpt-5 ------------------------------- #

Total score: **7/14**
Accuracy: **50.0%**

Correct transcriptions: **7**
carrots, waffle, cookie, nutsandseeds, pesto, milk, test

Incorrect transcriptions: **7**
sausages, softcheese, bread, redbull, metat, cheese, cocomilk

## Details

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got 3.5
- fats: expected 17,0, got 7.8
- carbs: expected 3,5, got 17

### carrots: 1/1
All values found.

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 11
- fats: expected 0,2, got 2
- carbs: expected 5,7, got 57

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### waffle: 1/1
All values found.

### cookie: 1/1
All values found.

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### metat: 0/1
Missing values:
- fats: expected 10, got 9

### milk: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### test: 1/1
All values found.

### cocomilk: 0/1
Missing values:
- kcal: expected 237, got None
- prots: expected 2,5, got None
- fats: expected 24, got None
- carbs: expected 2,8, got None



# ---------------------- Model scores: gpt-5-cropped ------------------------------- #

Total score: **6/14**
Accuracy: **42.86%**

Correct transcriptions: **6**
carrots, cookie, nutsandseeds, pesto, milk, test

Incorrect transcriptions: **8**
sausages, softcheese, bread, redbull, waffle, metat, cheese, cocomilk

## Details

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got 390
- prots: expected 7,8, got 3.5
- carbs: expected 3,5, got 78.9

### carrots: 1/1
All values found.

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 11
- fats: expected 0,2, got 2
- carbs: expected 5,7, got 57

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### waffle: 0/1
Missing values:
- prots: expected 20,0, got 2

### cookie: 1/1
All values found.

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### metat: 0/1
Missing values:
- kcal: expected 143, got None
- prots: expected 16, got None
- fats: expected 10, got None

### milk: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### test: 1/1
All values found.

### cocomilk: 0/1
Missing values:
- kcal: expected 237, got None
- prots: expected 2,5, got None
- fats: expected 24, got None
- carbs: expected 2,8, got None


# ---------------------- Model scores: PaddleOCR ------------------------------- #

Total score: **0/14**
Accuracy: **0.0%**

Correct transcriptions: **0**
-

Incorrect transcriptions: **14**
sausages, softcheese, carrots, bread, redbull, waffle, cookie, nutsandseeds, pesto, metat, milk, cheese, test, cocomilk

## Details

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got None
- fats: expected 17,0, got None
- carbs: expected 3,5, got None

### carrots: 0/1
Missing values:
- kcal: expected 35, got None
- prots: expected 1,3, got None
- fats: expected 0,1, got None
- carbs: expected 7,2, got None

### bread: 0/1
Missing values:
- kcal: expected 31, got None
- prots: expected 1,1, got None
- fats: expected 0,2, got None
- carbs: expected 5,7, got None

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### waffle: 0/1
Missing values:
- kcal: expected 550, got None
- prots: expected 20,0, got None
- fats: expected 32,0, got None
- carbs: expected 45,0, got None

### cookie: 0/1
Missing values:
- kcal: expected 398, got None
- prots: expected 7,4, got None
- fats: expected 16,1, got None
- carbs: expected 56,2, got None

### nutsandseeds: 0/1
Missing values:
- kcal: expected 557,4, got None
- prots: expected 22,8, got None
- fats: expected 47,3, got None
- carbs: expected 10,6, got None

### pesto: 0/1
Missing values:
- kcal: expected 329, got None
- prots: expected 3,8, got None
- fats: expected 29, got None
- carbs: expected 12, got None

### metat: 0/1
Missing values:
- kcal: expected 143, got None
- prots: expected 16, got None
- fats: expected 10, got None

### milk: 0/1
Missing values:
- kcal: expected 59, got None
- prots: expected 2,8, got None
- fats: expected 3,2, got None
- carbs: expected 4,7, got None

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### test: 0/1
Missing values:
- kcal: expected 42, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 10,6, got None

### cocomilk: 0/1
Missing values:
- kcal: expected 237, got None
- prots: expected 2,5, got None
- fats: expected 24, got None
- carbs: expected 2,8, got None


# Model timing: PaddleOCR

nutsandseeds.jpg: 37.14 sec
redbull.jpg: 65.00 sec
bread.jpg: 34.60 sec
test.jpg: 19.03 sec
softcheese.jpg: 9.40 sec
cookie.jpg: 35.41 sec
cheese.jpg: 29.04 sec
metat.jpg: 24.21 sec
carrots.jpg: 31.78 sec
waffle.jpg: 24.37 sec
milk.jpg: 29.89 sec
pesto.jpg: 18.10 sec
sausages.jpg: 19.29 sec
cocomilk.jpg: 15.14 sec

Average runtime: **28.03** sec
Total runtime: **392.39** sec


# Model timing: PaddleOCR

nutsandseeds.jpg: 14.28 sec
redbull.jpg: 27.92 sec
bread.jpg: 24.06 sec
test.jpg: 11.16 sec
softcheese.jpg: 5.82 sec
cookie.jpg: 19.91 sec
cheese.jpg: 21.07 sec
metat.jpg: 18.21 sec
carrots.jpg: 19.86 sec
waffle.jpg: 11.43 sec
milk.jpg: 19.88 sec
pesto.jpg: 13.55 sec
sausages.jpg: 14.07 sec
cocomilk.jpg: 9.53 sec

Average runtime: **16.48** sec
Total runtime: **230.73** sec


# ---------------------- Model scores: PaddleOCR ------------------------------- #

Total score: **6/14**
Accuracy: **42.86%**

Correct transcriptions: **6**
cookie, nutsandseeds, pesto, metat, test, cocomilk

Incorrect transcriptions: **8**
sausages, softcheese, carrots, bread, redbull, waffle, milk, cheese

## Details

### sausages: 0/1
Missing values:
- prots: expected 10, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got None
- fats: expected 17,0, got None
- carbs: expected 3,5, got None

### carrots: 0/1
Missing values:
- kcal: expected 35, got None
- prots: expected 1,3, got None
- fats: expected 0,1, got None
- carbs: expected 7,2, got None

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 10
- fats: expected 0,2, got 2.0
- carbs: expected 5,7, got 57.0

### redbull: 0/1
Missing values:
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### waffle: 0/1
Missing values:
- prots: expected 20,0, got None
- fats: expected 32,0, got None
- carbs: expected 45,0, got None

### cookie: 1/1
All values found.

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### metat: 1/1
All values found.

### milk: 0/1
Missing values:
- prots: expected 2,8, got None
- fats: expected 3,2, got None
- carbs: expected 4,7, got None

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### test: 1/1
All values found.

### cocomilk: 1/1
All values found.


# Model timing: gemma3:27b-it-q4_K_M

nutsandseeds.jpg: 217.37 seconds, prompt tokens: 516, output tokens: 772
bread.jpg: 77.62 seconds, prompt tokens: 516, output tokens: 436
test.jpg: 84.46 seconds, prompt tokens: 516, output tokens: 466
softcheese.jpg: 70.32 seconds, prompt tokens: 516, output tokens: 385
cookie.jpg: 124.17 seconds, prompt tokens: 516, output tokens: 674
cheese.jpg: 46.96 seconds, prompt tokens: 516, output tokens: 252
metat.jpg: 130.21 seconds, prompt tokens: 516, output tokens: 714
carrots.jpg: 86.32 seconds, prompt tokens: 516, output tokens: 467
waffle.jpg: 120.81 seconds, prompt tokens: 516, output tokens: 662
milk.jpg: 184.95 seconds, prompt tokens: 516, output tokens: 1006
pesto.jpg: 95.61 seconds, prompt tokens: 516, output tokens: 546
sausages.jpg: 115.28 seconds, prompt tokens: 516, output tokens: 652
cocomilk.jpg: 75.07 seconds, prompt tokens: 516, output tokens: 425

Average runtime: **109.93** sec


# Model timing: gemma3:12b-it-q8_0

redbull.jpg: 60.90 seconds, prompt tokens: 516, output tokens: 1681
bread.jpg: 22.82 seconds, prompt tokens: 516, output tokens: 610
test.jpg: 74.63 seconds, prompt tokens: 516, output tokens: 1996
softcheese.jpg: 21.11 seconds, prompt tokens: 516, output tokens: 525
cookie.jpg: 24.16 seconds, prompt tokens: 516, output tokens: 604
cheese.jpg: 23.88 seconds, prompt tokens: 516, output tokens: 600
metat.jpg: 100.02 seconds, prompt tokens: 516, output tokens: 2682
carrots.jpg: 19.17 seconds, prompt tokens: 516, output tokens: 497
waffle.jpg: 25.81 seconds, prompt tokens: 516, output tokens: 685
milk.jpg: 37.71 seconds, prompt tokens: 516, output tokens: 1015
pesto.jpg: 19.29 seconds, prompt tokens: 516, output tokens: 506
sausages.jpg: 23.07 seconds, prompt tokens: 516, output tokens: 613
cocomilk.jpg: 17.48 seconds, prompt tokens: 516, output tokens: 448

Average runtime: **36.16** sec
Total runtime: **470.03** sec


# ---------------------- Model scores: Gemma12b ------------------------------- #

Total score: **4/14**
Accuracy: **28.57%**

Correct transcriptions: **4**
carrots, cocomilk, cookie, waffle

Incorrect transcriptions: **10**
bread, cheese, metat, milk, nutsandseeds, pesto, redbull, sausages, softcheese, test

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310.0

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got 274
- prots: expected 26, got 18
- fats: expected 18, got 20
- carbs: expected 1, got 1.5

### cocomilk: 1/1
All values found.

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- kcal: expected 143, got None
- prots: expected 16, got None
- fats: expected 10, got None

### milk: 0/1
Missing values:
- kcal: expected 59, got 346.0
- prots: expected 2,8, got 7.2
- carbs: expected 4,7, got 4.8

### nutsandseeds: 0/1
Missing values:
- JSON file is missing: nutsandseeds.json

### pesto: 0/1
Missing values:
- kcal: expected 329, got 1360

### redbull: 0/1
Missing values:
- kcal: expected 3, got 15

### sausages: 0/1
Missing values:
- kcal: expected 160, got 268
- prots: expected 10, got 15
- fats: expected 12, got 23
- carbs: expected 3, got 2.9

### softcheese: 0/1
Missing values:
- kcal: expected 198, got 173
- prots: expected 7,8, got 0.0
- fats: expected 17,0, got 0.0
- carbs: expected 3,5, got 47.0

### waffle: 1/1
All values found.

### test: 0/1
Missing values:
- kcal: expected 42, got 105.0
- carbs: expected 10,6, got 27.0


# ---------------------- Model scores: Gemma27b ------------------------------- #

Total score: **7/14**
Accuracy: **50.0%**

Correct transcriptions: **7**
carrots, cocomilk, cookie, nutsandseeds, pesto, waffle, test

Incorrect transcriptions: **7**
bread, cheese, metat, milk, redbull, sausages, softcheese

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310.0
- prots: expected 1,1, got 10.5
- fats: expected 0,2, got 2.0
- carbs: expected 5,7, got 57.0

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 1/1
All values found.

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- kcal: expected 143, got 230.0
- prots: expected 16, got 18.0
- fats: expected 10, got 25.0

### milk: 0/1
Missing values:
- kcal: expected 59, got 159.0
- fats: expected 3,2, got 4.7
- carbs: expected 4,7, got 3.1

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- JSON file is missing: redbull.json

### sausages: 0/1
Missing values:
- kcal: expected 160, got 95.0
- prots: expected 10, got 6.0
- fats: expected 12, got 4.8
- carbs: expected 3, got 3.2

### softcheese: 0/1
Missing values:
- kcal: expected 198, got 273.0
- prots: expected 7,8, got 4.3
- fats: expected 17,0, got 9.5
- carbs: expected 3,5, got 36.6

### waffle: 1/1
All values found.

### test: 1/1
All values found.


# ---------------------- Model scores: gpt-5 ------------------------------- #

Total score: **7/14**
Accuracy: **50.0%**

Correct transcriptions: **7**
carrots, cookie, milk, nutsandseeds, pesto, waffle, test

Incorrect transcriptions: **7**
bread, cheese, cocomilk, metat, redbull, sausages, softcheese

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 11
- fats: expected 0,2, got 2
- carbs: expected 5,7, got 57

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 0/1
Missing values:
- kcal: expected 237, got None
- prots: expected 2,5, got None
- fats: expected 24, got None
- carbs: expected 2,8, got None

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- fats: expected 10, got 9

### milk: 1/1
All values found.

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got 3.5
- fats: expected 17,0, got 7.8
- carbs: expected 3,5, got 17

### waffle: 1/1
All values found.

### test: 1/1
All values found.


# ---------------------- Model scores: PaddleOCR ------------------------------- #

Total score: **4/14**
Accuracy: **28.57%**

Correct transcriptions: **4**
cookie, metat, nutsandseeds, pesto

Incorrect transcriptions: **10**
bread, carrots, cheese, cocomilk, milk, redbull, sausages, softcheese, waffle, test

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 10
- fats: expected 0,2, got 2
- carbs: expected 5,7, got 57

### carrots: 0/1
Missing values:
- kcal: expected 35, got None
- prots: expected 1,3, got None
- fats: expected 0,1, got None
- carbs: expected 7,2, got None

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 0/1
Missing values:
- kcal: expected 237, got None
- prots: expected 2,5, got None
- fats: expected 24, got None
- carbs: expected 2,8, got None

### cookie: 1/1
All values found.

### metat: 1/1
All values found.

### milk: 0/1
Missing values:
- prots: expected 2,8, got None
- fats: expected 3,2, got None
- carbs: expected 4,7, got None

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got None
- fats: expected 17,0, got None
- carbs: expected 3,5, got None

### waffle: 0/1
Missing values:
- prots: expected 20,0, got None
- fats: expected 32,0, got None
- carbs: expected 45,0, got None

### test: 0/1
Missing values:
- kcal: expected 42, got None
- fats: expected 0, got None
- carbs: expected 10,6, got None


# ---------------------- Model scores: Gemma12b ------------------------------- #

Total score: **4/14**
Accuracy: **28.57%**

Correct transcriptions: **4**
carrots, cocomilk, cookie, waffle

Incorrect transcriptions: **10**
bread, cheese, metat, milk, nutsandseeds, pesto, redbull, sausages, softcheese, test

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310.0

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got 274
- prots: expected 26, got 18
- fats: expected 18, got 20
- carbs: expected 1, got 1.5

### cocomilk: 1/1
All values found.

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- kcal: expected 143, got None
- prots: expected 16, got None
- fats: expected 10, got None

### milk: 0/1
Missing values:
- kcal: expected 59, got 346.0
- prots: expected 2,8, got 7.2
- carbs: expected 4,7, got 4.8

### nutsandseeds: 0/1
Missing values:
- JSON file is missing: nutsandseeds.json

### pesto: 0/1
Missing values:
- kcal: expected 329, got 1360

### redbull: 0/1
Missing values:
- kcal: expected 3, got 15

### sausages: 0/1
Missing values:
- kcal: expected 160, got 268
- prots: expected 10, got 15
- fats: expected 12, got 23
- carbs: expected 3, got 2.9

### softcheese: 0/1
Missing values:
- kcal: expected 198, got 173
- prots: expected 7,8, got 0.0
- fats: expected 17,0, got 0.0
- carbs: expected 3,5, got 47.0

### waffle: 1/1
All values found.

### test: 0/1
Missing values:
- kcal: expected 42, got 105.0
- carbs: expected 10,6, got 27.0


# ---------------------- Model scores: Gemma27b ------------------------------- #

Total score: **7/14**
Accuracy: **50.0%**

Correct transcriptions: **7**
carrots, cocomilk, cookie, nutsandseeds, pesto, waffle, test

Incorrect transcriptions: **7**
bread, cheese, metat, milk, redbull, sausages, softcheese

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310.0
- prots: expected 1,1, got 10.5
- fats: expected 0,2, got 2.0
- carbs: expected 5,7, got 57.0

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 1/1
All values found.

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- kcal: expected 143, got 230.0
- prots: expected 16, got 18.0
- fats: expected 10, got 25.0

### milk: 0/1
Missing values:
- kcal: expected 59, got 159.0
- fats: expected 3,2, got 4.7
- carbs: expected 4,7, got 3.1

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- JSON file is missing: redbull.json

### sausages: 0/1
Missing values:
- kcal: expected 160, got 95.0
- prots: expected 10, got 6.0
- fats: expected 12, got 4.8
- carbs: expected 3, got 3.2

### softcheese: 0/1
Missing values:
- kcal: expected 198, got 273.0
- prots: expected 7,8, got 4.3
- fats: expected 17,0, got 9.5
- carbs: expected 3,5, got 36.6

### waffle: 1/1
All values found.

### test: 1/1
All values found.


# ---------------------- Model scores: gpt-5 ------------------------------- #

Total score: **7/14**
Accuracy: **50.0%**

Correct transcriptions: **7**
carrots, cookie, milk, nutsandseeds, pesto, waffle, test

Incorrect transcriptions: **7**
bread, cheese, cocomilk, metat, redbull, sausages, softcheese

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 11
- fats: expected 0,2, got 2
- carbs: expected 5,7, got 57

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 0/1
Missing values:
- kcal: expected 237, got None
- prots: expected 2,5, got None
- fats: expected 24, got None
- carbs: expected 2,8, got None

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- fats: expected 10, got 9

### milk: 1/1
All values found.

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got 3.5
- fats: expected 17,0, got 7.8
- carbs: expected 3,5, got 17

### waffle: 1/1
All values found.

### test: 1/1
All values found.


# ---------------------- Model scores: PaddleOCR ------------------------------- #

Total score: **6/14**
Accuracy: **42.86%**

Correct transcriptions: **6**
cocomilk, cookie, metat, nutsandseeds, pesto, test

Incorrect transcriptions: **8**
bread, carrots, cheese, milk, redbull, sausages, softcheese, waffle

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 10
- fats: expected 0,2, got 2
- carbs: expected 5,7, got 57

### carrots: 0/1
Missing values:
- kcal: expected 35, got None
- prots: expected 1,3, got None
- fats: expected 0,1, got None
- carbs: expected 7,2, got None

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 1/1
All values found.

### cookie: 1/1
All values found.

### metat: 1/1
All values found.

### milk: 0/1
Missing values:
- prots: expected 2,8, got None
- fats: expected 3,2, got None
- carbs: expected 4,7, got None

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got None
- fats: expected 17,0, got None
- carbs: expected 3,5, got None

### waffle: 0/1
Missing values:
- prots: expected 20,0, got None
- fats: expected 32,0, got None
- carbs: expected 45,0, got None

### test: 1/1
All values found.


# Model timing: gemma3:12b-it-q8_0

nutsandseeds.jpg: 40.74 seconds, prompt tokens: 801, output tokens: 736
redbull.jpg: 41.16 seconds, prompt tokens: 801, output tokens: 1114
bread.jpg: 16.99 seconds, prompt tokens: 801, output tokens: 444
test.jpg: 18.75 seconds, prompt tokens: 801, output tokens: 495
softcheese.jpg: 23.51 seconds, prompt tokens: 801, output tokens: 638
cookie.jpg: 18.45 seconds, prompt tokens: 801, output tokens: 488
cheese.jpg: 10.69 seconds, prompt tokens: 801, output tokens: 262
metat.jpg: 34.24 seconds, prompt tokens: 801, output tokens: 919
carrots.jpg: 19.69 seconds, prompt tokens: 801, output tokens: 496
waffle.jpg: 29.29 seconds, prompt tokens: 801, output tokens: 761
milk.jpg: 36.28 seconds, prompt tokens: 801, output tokens: 950
pesto.jpg: 34.49 seconds, prompt tokens: 801, output tokens: 925
sausages.jpg: 23.97 seconds, prompt tokens: 801, output tokens: 638
cocomilk.jpg: 18.83 seconds, prompt tokens: 801, output tokens: 482

Average runtime: **26.22** sec
Total runtime: **367.09** sec


RESULTS 13 JULY

# ---------------------- Model scores: Gemma12b ------------------------------- #

Total score: **6/14**
Accuracy: **42.86%**

Correct transcriptions: **6**
carrots, cocomilk, cookie, nutsandseeds, pesto, waffle

Incorrect transcriptions: **8**
bread, cheese, metat, milk, redbull, sausages, softcheese, test

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310.0
- prots: expected 1,1, got 10.5
- fats: expected 0,2, got 2.0
- carbs: expected 5,7, got 57.0

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 1/1
All values found.

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- kcal: expected 143, got None
- prots: expected 16, got None
- fats: expected 10, got None

### milk: 0/1
Missing values:
- kcal: expected 59, got 62.0
- prots: expected 2,8, got 3.0
- carbs: expected 4,7, got 4.9

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- kcal: expected 3, got 48.0
- prots: expected 0, got 0.1
- carbs: expected 0, got 27.5

### sausages: 0/1
Missing values:
- kcal: expected 160, got 6
- prots: expected 10, got 1.2
- fats: expected 12, got 0.3
- carbs: expected 3, got 4.8

### softcheese: 0/1
Missing values:
- kcal: expected 198, got 172.0
- prots: expected 7,8, got 9.4
- fats: expected 17,0, got 7.8
- carbs: expected 3,5, got 45.0

### waffle: 1/1
All values found.

### test: 0/1
Missing values:
- kcal: expected 42, got 105.0
- carbs: expected 10,6, got 27.0


# ---------------------- Model scores: Gemma27b ------------------------------- #

Total score: **7/14**
Accuracy: **50.0%**

Correct transcriptions: **7**
carrots, cocomilk, cookie, nutsandseeds, pesto, waffle, test

Incorrect transcriptions: **7**
bread, cheese, metat, milk, redbull, sausages, softcheese

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310.0
- prots: expected 1,1, got 10.5
- fats: expected 0,2, got 2.0
- carbs: expected 5,7, got 57.0

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 1/1
All values found.

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- kcal: expected 143, got 230.0
- prots: expected 16, got 18.0
- fats: expected 10, got 25.0

### milk: 0/1
Missing values:
- kcal: expected 59, got 159.0
- fats: expected 3,2, got 4.7
- carbs: expected 4,7, got 3.1

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- JSON file is missing: redbull.json

### sausages: 0/1
Missing values:
- kcal: expected 160, got 95.0
- prots: expected 10, got 6.0
- fats: expected 12, got 4.8
- carbs: expected 3, got 3.2

### softcheese: 0/1
Missing values:
- kcal: expected 198, got 273.0
- prots: expected 7,8, got 4.3
- fats: expected 17,0, got 9.5
- carbs: expected 3,5, got 36.6

### waffle: 1/1
All values found.

### test: 1/1
All values found.


# ---------------------- Model scores: gpt-5 ------------------------------- #

Total score: **7/14**
Accuracy: **50.0%**

Correct transcriptions: **7**
carrots, cookie, milk, nutsandseeds, pesto, waffle, test

Incorrect transcriptions: **7**
bread, cheese, cocomilk, metat, redbull, sausages, softcheese

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 11
- fats: expected 0,2, got 2
- carbs: expected 5,7, got 57

### carrots: 1/1
All values found.

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 0/1
Missing values:
- kcal: expected 237, got None
- prots: expected 2,5, got None
- fats: expected 24, got None
- carbs: expected 2,8, got None

### cookie: 1/1
All values found.

### metat: 0/1
Missing values:
- fats: expected 10, got 9

### milk: 1/1
All values found.

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got 3.5
- fats: expected 17,0, got 7.8
- carbs: expected 3,5, got 17

### waffle: 1/1
All values found.

### test: 1/1
All values found.


# ---------------------- Model scores: PaddleOCR ------------------------------- #

Total score: **6/14**
Accuracy: **42.86%**

Correct transcriptions: **6**
cocomilk, cookie, metat, nutsandseeds, pesto, test

Incorrect transcriptions: **8**
bread, carrots, cheese, milk, redbull, sausages, softcheese, waffle

## Details

### bread: 0/1
Missing values:
- kcal: expected 31, got 310
- prots: expected 1,1, got 10
- fats: expected 0,2, got 2
- carbs: expected 5,7, got 57

### carrots: 0/1
Missing values:
- kcal: expected 35, got None
- prots: expected 1,3, got None
- fats: expected 0,1, got None
- carbs: expected 7,2, got None

### cheese: 0/1
Missing values:
- kcal: expected 270, got None
- prots: expected 26, got None
- fats: expected 18, got None
- carbs: expected 1, got None

### cocomilk: 1/1
All values found.

### cookie: 1/1
All values found.

### metat: 1/1
All values found.

### milk: 0/1
Missing values:
- prots: expected 2,8, got None
- fats: expected 3,2, got None
- carbs: expected 4,7, got None

### nutsandseeds: 1/1
All values found.

### pesto: 1/1
All values found.

### redbull: 0/1
Missing values:
- kcal: expected 3, got None
- prots: expected 0, got None
- fats: expected 0, got None
- carbs: expected 0, got None

### sausages: 0/1
Missing values:
- kcal: expected 160, got None
- prots: expected 10, got None
- fats: expected 12, got None
- carbs: expected 3, got None

### softcheese: 0/1
Missing values:
- kcal: expected 198, got None
- prots: expected 7,8, got None
- fats: expected 17,0, got None
- carbs: expected 3,5, got None

### waffle: 0/1
Missing values:
- prots: expected 20,0, got None
- fats: expected 32,0, got None
- carbs: expected 45,0, got None

### test: 1/1
All values found.
# Model timing: GPT-5

nutsandseeds.jpg: 21.24 seconds, input tokens: 1431, output tokens: 1903, total tokens: 3334
redbull.jpg: 25.89 seconds, input tokens: 1431, output tokens: 1659, total tokens: 3090
bread.jpg: 40.19 seconds, input tokens: 1431, output tokens: 3794, total tokens: 5225
test.jpg: 29.80 seconds, input tokens: 1711, output tokens: 2896, total tokens: 4607
softcheese.jpg: 26.77 seconds, input tokens: 1431, output tokens: 2107, total tokens: 3538
cookie.jpg: 29.01 seconds, input tokens: 1431, output tokens: 2446, total tokens: 3877
cheese.jpg: 16.51 seconds, input tokens: 1711, output tokens: 1186, total tokens: 2897
metat.jpg: 36.60 seconds, input tokens: 1431, output tokens: 3527, total tokens: 4958
carrots.jpg: 23.94 seconds, input tokens: 1711, output tokens: 1842, total tokens: 3553
waffle.jpg: 48.26 seconds, input tokens: 1431, output tokens: 3534, total tokens: 4965
milk.jpg: 25.94 seconds, input tokens: 1431, output tokens: 1863, total tokens: 3294
pesto.jpg: 43.76 seconds, input tokens: 1431, output tokens: 3639, total tokens: 5070
sausages.jpg: 22.74 seconds, input tokens: 1431, output tokens: 1896, total tokens: 3327
cocomilk.jpg: 18.38 seconds, input tokens: 1431, output tokens: 1790, total tokens: 3221

Average runtime: **29.22** sec
Total runtime: **409.02** sec


# Model timing: gemma3:27b-it-q4_K_M

nutsandseeds.jpg: 156.81 seconds, prompt tokens: 801, output tokens: 737
redbull.jpg: 130.90 seconds, prompt tokens: 801, output tokens: 717
bread.jpg: 108.47 seconds, prompt tokens: 801, output tokens: 566
test.jpg: 94.30 seconds, prompt tokens: 801, output tokens: 477
softcheese.jpg: 45.51 seconds, prompt tokens: 801, output tokens: 218
cookie.jpg: 31.95 seconds, prompt tokens: 801, output tokens: 145
cheese.jpg: 42.24 seconds, prompt tokens: 801, output tokens: 200
metat.jpg: 155.39 seconds, prompt tokens: 801, output tokens: 736
carrots.jpg: 99.80 seconds, prompt tokens: 801, output tokens: 461
waffle.jpg: 130.45 seconds, prompt tokens: 801, output tokens: 706
milk.jpg: 203.30 seconds, prompt tokens: 801, output tokens: 1128
pesto.jpg: 103.38 seconds, prompt tokens: 801, output tokens: 511
sausages.jpg: 100.72 seconds, prompt tokens: 801, output tokens: 471
cocomilk.jpg: 92.39 seconds, prompt tokens: 801, output tokens: 428

Average runtime: **106.83** sec
Total runtime: **1495.62** sec


# Model timing: gpt-5


# Model timing: gpt-5


# Model timing: gpt-5

bread.jpg: 49.17 seconds, input tokens: 2058, output tokens: 3002, total tokens: 5060
carrots.jpg: 33.56 seconds, input tokens: 2058, output tokens: 3319, total tokens: 5377
cheese.jpg: 25.90 seconds, input tokens: 2058, output tokens: 1852, total tokens: 3910
cocomilk.jpg: 22.00 seconds, input tokens: 2058, output tokens: 1803, total tokens: 3861
cookie.jpg: 29.11 seconds, input tokens: 2058, output tokens: 2211, total tokens: 4269
metat.jpg: 39.10 seconds, input tokens: 2058, output tokens: 3858, total tokens: 5916
milk.jpg: 24.08 seconds, input tokens: 2058, output tokens: 1662, total tokens: 3720
nutsandseeds.jpg: 31.11 seconds, input tokens: 2058, output tokens: 2538, total tokens: 4596
pesto.jpg: 33.55 seconds, input tokens: 2058, output tokens: 2945, total tokens: 5003
redbull.jpg: 31.77 seconds, input tokens: 2058, output tokens: 2251, total tokens: 4309
sausages.jpg: 28.83 seconds, input tokens: 2058, output tokens: 2350, total tokens: 4408
softcheese.jpg: 27.49 seconds, input tokens: 2058, output tokens: 1754, total tokens: 3812
test.jpg: 26.75 seconds, input tokens: 2058, output tokens: 2683, total tokens: 4741
waffle.jpg: 30.10 seconds, input tokens: 2058, output tokens: 2386, total tokens: 4444

Average runtime: **30.89** sec
Total runtime: **432.51** sec

# Model timing: gemma3:27b-it-q4_K_M

bread.jpg: 182.99 seconds, prompt tokens: 1015, output tokens: 777
carrots.jpg: 80.85 seconds, prompt tokens: 1015, output tokens: 405
cheese.jpg: 39.03 seconds, prompt tokens: 1015, output tokens: 188
cocomilk.jpg: 178.85 seconds, prompt tokens: 1015, output tokens: 917
cookie.jpg: 29.67 seconds, prompt tokens: 1015, output tokens: 139
metat.jpg: 71.47 seconds, prompt tokens: 1015, output tokens: 357
milk.jpg: 127.77 seconds, prompt tokens: 1015, output tokens: 672
nutsandseeds.jpg: 136.60 seconds, prompt tokens: 1015, output tokens: 600
pesto.jpg: 144.16 seconds, prompt tokens: 1015, output tokens: 591
redbull.jpg: 63.58 seconds, prompt tokens: 1015, output tokens: 262
sausages.jpg: 72.19 seconds, prompt tokens: 1015, output tokens: 275
softcheese.jpg: 44.93 seconds, prompt tokens: 1015, output tokens: 165
test.jpg: 231.88 seconds, prompt tokens: 1015, output tokens: 1005
waffle.jpg: 102.16 seconds, prompt tokens: 1015, output tokens: 446

Average runtime: **107.58** sec
Total runtime: **1506.14** sec

# Model timing: PaddleOCR

bread.jpg: 338.84 seconds
carrots.jpg: 180.83 seconds
cheese.jpg: 124.27 seconds
cocomilk.jpg: 84.85 seconds
cookie.jpg: 53.49 seconds
metat.jpg: 20.54 seconds
milk.jpg: 36.40 seconds
nutsandseeds.jpg: 20.05 seconds
pesto.jpg: 16.44 seconds
redbull.jpg: 63.40 seconds
sausages.jpg: 18.78 seconds
softcheese.jpg: 12.28 seconds
test.jpg: 18.38 seconds
waffle.jpg: 20.50 seconds

Average runtime: **72.07** sec
Total runtime: **1009.04** sec

# Model timing: PaddleOCR

bread.jpg: 53.69 seconds
carrots.jpg: 15.89 seconds
cheese.jpg: 15.18 seconds
cocomilk.jpg: 10.18 seconds
cookie.jpg: 18.98 seconds
metat.jpg: 9.56 seconds
milk.jpg: 17.76 seconds
nutsandseeds.jpg: 11.56 seconds
pesto.jpg: 8.11 seconds
redbull.jpg: 25.49 seconds
sausages.jpg: 7.58 seconds
softcheese.jpg: 6.63 seconds
test.jpg: 7.03 seconds
waffle.jpg: 8.26 seconds

Average runtime: **15.42** sec
Total runtime: **215.88** sec

# Model timing: gpt-5

bread.jpg: 32.65 seconds, input tokens: 1498, output tokens: 2576, total tokens: 4074
carrots.jpg: 17.01 seconds, input tokens: 1778, output tokens: 1665, total tokens: 3443
cheese.jpg: 17.98 seconds, input tokens: 1778, output tokens: 1779, total tokens: 3557
cocomilk.jpg: 21.71 seconds, input tokens: 1498, output tokens: 2424, total tokens: 3922
cookie.jpg: 25.68 seconds, input tokens: 1498, output tokens: 2449, total tokens: 3947
metat.jpg: 28.24 seconds, input tokens: 1498, output tokens: 2700, total tokens: 4198
milk.jpg: 34.33 seconds, input tokens: 1498, output tokens: 2945, total tokens: 4443
nutsandseeds.jpg: 21.52 seconds, input tokens: 1498, output tokens: 2352, total tokens: 3850
pesto.jpg: 26.32 seconds, input tokens: 1498, output tokens: 2893, total tokens: 4391
redbull.jpg: 34.88 seconds, input tokens: 1498, output tokens: 3107, total tokens: 4605
sausages.jpg: 26.92 seconds, input tokens: 1498, output tokens: 2386, total tokens: 3884
softcheese.jpg: 31.60 seconds, input tokens: 1498, output tokens: 2654, total tokens: 4152
test.jpg: 27.08 seconds, input tokens: 1778, output tokens: 2836, total tokens: 4614
waffle.jpg: 33.17 seconds, input tokens: 1498, output tokens: 3225, total tokens: 4723

Average runtime: **27.08** sec
Total runtime: **379.09** sec

# Model timing: gemma3:27b-it-q4_K_M

bread.jpg: 151.89 seconds, prompt tokens: 1015, output tokens: 636
carrots.jpg: 91.05 seconds, prompt tokens: 1015, output tokens: 468
cheese.jpg: 39.61 seconds, prompt tokens: 1015, output tokens: 187
cocomilk.jpg: 80.05 seconds, prompt tokens: 1015, output tokens: 407
cookie.jpg: 59.72 seconds, prompt tokens: 1015, output tokens: 301
metat.jpg: 176.92 seconds, prompt tokens: 1015, output tokens: 922
milk.jpg: 183.08 seconds, prompt tokens: 1015, output tokens: 958
nutsandseeds.jpg: 140.98 seconds, prompt tokens: 1015, output tokens: 728
pesto.jpg: 110.54 seconds, prompt tokens: 1015, output tokens: 574
redbull.jpg: 88.60 seconds, prompt tokens: 1015, output tokens: 456
sausages.jpg: 139.06 seconds, prompt tokens: 1015, output tokens: 722
softcheese.jpg: 66.62 seconds, prompt tokens: 1015, output tokens: 339
test.jpg: 90.18 seconds, prompt tokens: 1015, output tokens: 463
waffle.jpg: 130.65 seconds, prompt tokens: 1015, output tokens: 680

Average runtime: **110.64** sec
Total runtime: **1548.94** sec

# Model timing: gemma3:12b-it-q8_0

bread.jpg: 45.46 seconds, prompt tokens: 1015, output tokens: 643
carrots.jpg: 20.06 seconds, prompt tokens: 1015, output tokens: 518
cheese.jpg: 10.68 seconds, prompt tokens: 1015, output tokens: 252
cocomilk.jpg: 17.82 seconds, prompt tokens: 1015, output tokens: 460
cookie.jpg: 21.18 seconds, prompt tokens: 1015, output tokens: 546
metat.jpg: 35.62 seconds, prompt tokens: 1015, output tokens: 969
milk.jpg: 31.23 seconds, prompt tokens: 1015, output tokens: 835
nutsandseeds.jpg: 24.20 seconds, prompt tokens: 1015, output tokens: 640
pesto.jpg: 21.68 seconds, prompt tokens: 1015, output tokens: 570
redbull.jpg: 19.83 seconds, prompt tokens: 1015, output tokens: 510
sausages.jpg: 30.45 seconds, prompt tokens: 1015, output tokens: 822
softcheese.jpg: 19.52 seconds, prompt tokens: 1015, output tokens: 507
test.jpg: 19.01 seconds, prompt tokens: 1015, output tokens: 493
waffle.jpg: 26.57 seconds, prompt tokens: 1015, output tokens: 709

Average runtime: **24.52** sec
Total runtime: **343.31** sec

# Model timing: paddleocr+gpt-5-jsonifier

bread.jpg: 127.62 seconds
carrots.jpg: 31.53 seconds
cheese.jpg: 47.43 seconds
cocomilk.jpg: 39.17 seconds
cookie.jpg: 54.55 seconds
metat.jpg: 38.13 seconds
milk.jpg: 60.11 seconds
nutsandseeds.jpg: 34.92 seconds
pesto.jpg: 46.85 seconds
redbull.jpg: 61.27 seconds
sausages.jpg: 60.85 seconds
softcheese.jpg: 11.31 seconds
test.jpg: 42.06 seconds
waffle.jpg: 38.95 seconds

Average runtime: **49.62** sec
Total runtime: **694.75** sec

# Model timing: paddleocr+gpt-5-jsonifier

bread.jpg: 106.70 seconds
carrots.jpg: 30.33 seconds
cheese.jpg: 26.22 seconds
cocomilk.jpg: 33.21 seconds
cookie.jpg: 83.06 seconds
metat.jpg: 68.47 seconds
milk.jpg: 65.65 seconds
nutsandseeds.jpg: 37.75 seconds
pesto.jpg: 31.28 seconds
redbull.jpg: 53.72 seconds
sausages.jpg: 54.88 seconds
softcheese.jpg: 11.02 seconds
test.jpg: 39.72 seconds
waffle.jpg: 35.33 seconds

Average runtime: **48.38** sec
Total runtime: **677.34** sec