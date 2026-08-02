
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

# Model timing: paddleocr+gpt-5-jsonifier

bread.jpg: 69.28 seconds
carrots.jpg: 26.96 seconds
cheese.jpg: 25.18 seconds
cocomilk.jpg: 18.84 seconds
cookie.jpg: 39.63 seconds
metat.jpg: 32.10 seconds
milk.jpg: 42.06 seconds
nutsandseeds.jpg: 31.87 seconds
pesto.jpg: 19.57 seconds
redbull.jpg: 40.94 seconds
sausages.jpg: 31.71 seconds
softcheese.jpg: 7.75 seconds
test.jpg: 26.17 seconds
waffle.jpg: 22.65 seconds

Average runtime: **31.05** sec
Total runtime: **434.71** sec

# Model timing: gpt-5

bread.jpg: 30.44 seconds, input tokens: 1498, output tokens: 2880, total tokens: 4378
carrots.jpg: 20.47 seconds, input tokens: 1778, output tokens: 2601, total tokens: 4379
cheese.jpg: 14.51 seconds, input tokens: 1778, output tokens: 1470, total tokens: 3248
cocomilk.jpg: 17.27 seconds, input tokens: 1498, output tokens: 2200, total tokens: 3698
cookie.jpg: 17.13 seconds, input tokens: 1498, output tokens: 1587, total tokens: 3085
metat.jpg: 23.87 seconds, input tokens: 1498, output tokens: 3222, total tokens: 4720
milk.jpg: 24.59 seconds, input tokens: 1498, output tokens: 3299, total tokens: 4797
nutsandseeds.jpg: 20.87 seconds, input tokens: 1498, output tokens: 3096, total tokens: 4594
pesto.jpg: 19.48 seconds, input tokens: 1498, output tokens: 2594, total tokens: 4092
redbull.jpg: 25.86 seconds, input tokens: 1498, output tokens: 2871, total tokens: 4369
sausages.jpg: 16.64 seconds, input tokens: 1498, output tokens: 2136, total tokens: 3634
softcheese.jpg: 24.46 seconds, input tokens: 1498, output tokens: 2824, total tokens: 4322
test.jpg: 16.84 seconds, input tokens: 1778, output tokens: 2246, total tokens: 4024
waffle.jpg: 18.00 seconds, input tokens: 1498, output tokens: 2137, total tokens: 3635

Average runtime: **20.75** sec
Total runtime: **290.44** sec

# Model timing: gemma3:12b-it-q8_0

bread.jpg: 52.84 seconds, prompt tokens: 1015, output tokens: 502
carrots.jpg: 19.49 seconds, prompt tokens: 1015, output tokens: 510
cheese.jpg: 10.73 seconds, prompt tokens: 1015, output tokens: 255
cocomilk.jpg: 17.78 seconds, prompt tokens: 1015, output tokens: 466
cookie.jpg: 19.75 seconds, prompt tokens: 1015, output tokens: 515
metat.jpg: 37.92 seconds, prompt tokens: 1015, output tokens: 1049
milk.jpg: 30.88 seconds, prompt tokens: 1015, output tokens: 839
nutsandseeds.jpg: 24.68 seconds, prompt tokens: 1015, output tokens: 664
pesto.jpg: 19.97 seconds, prompt tokens: 1015, output tokens: 528
redbull.jpg: 25.49 seconds, prompt tokens: 1015, output tokens: 682
sausages.jpg: 38.74 seconds, prompt tokens: 1015, output tokens: 1072
softcheese.jpg: 17.16 seconds, prompt tokens: 1015, output tokens: 448
test.jpg: 18.91 seconds, prompt tokens: 1015, output tokens: 493
waffle.jpg: 28.44 seconds, prompt tokens: 1015, output tokens: 770

Average runtime: **25.91** sec
Total runtime: **362.80** sec

# Model timing: gemma4:12b

bread.jpg: 91.28 seconds, prompt tokens: 2506, output tokens: 259
cheese.jpg: 30.71 seconds, prompt tokens: 2136, output tokens: 177
cocomilk.jpg: 36.05 seconds, prompt tokens: 2156, output tokens: 401
cookie.jpg: 43.21 seconds, prompt tokens: 2646, output tokens: 224
metat.jpg: 66.43 seconds, prompt tokens: 3313, output tokens: 543
milk.jpg: 38.92 seconds, prompt tokens: 2317, output tokens: 331
nutsandseeds.jpg: 61.19 seconds, prompt tokens: 3339, output tokens: 281
pesto.jpg: 39.81 seconds, prompt tokens: 2256, output tokens: 476
redbull.jpg: 30.28 seconds, prompt tokens: 2087, output tokens: 174
sausages.jpg: 65.57 seconds, prompt tokens: 3539, output tokens: 279
test.jpg: 66.60 seconds, prompt tokens: 3460, output tokens: 478
waffle.jpg: 53.14 seconds, prompt tokens: 3029, output tokens: 246

Average runtime: **51.93** sec
Total runtime: **623.18** sec

# Model timing: gemma4:e4b

bread.jpg: 59.44 seconds, prompt tokens: 2028, output tokens: 302
carrots.jpg: 16.17 seconds, prompt tokens: 2200, output tokens: 182
cheese.jpg: 14.30 seconds, prompt tokens: 1968, output tokens: 180
cocomilk.jpg: 13.12 seconds, prompt tokens: 1982, output tokens: 149
cookie.jpg: 15.74 seconds, prompt tokens: 2138, output tokens: 150
metat.jpg: 16.80 seconds, prompt tokens: 2206, output tokens: 179
milk.jpg: 16.35 seconds, prompt tokens: 2185, output tokens: 187
nutsandseeds.jpg: 13.80 seconds, prompt tokens: 2085, output tokens: 120
pesto.jpg: 15.39 seconds, prompt tokens: 2094, output tokens: 247
redbull.jpg: 16.45 seconds, prompt tokens: 2170, output tokens: 260
sausages.jpg: 16.37 seconds, prompt tokens: 2212, output tokens: 222
softcheese.jpg: 16.04 seconds, prompt tokens: 2242, output tokens: 172
test.jpg: 14.89 seconds, prompt tokens: 2112, output tokens: 174
waffle.jpg: 15.46 seconds, prompt tokens: 2241, output tokens: 109

Average runtime: **18.59** sec
Total runtime: **260.31** sec

# Model timing: gemma3:27b-it-q4_K_M

bread.jpg: 131.22 seconds, prompt tokens: 1015, output tokens: 568
carrots.jpg: 86.76 seconds, prompt tokens: 1015, output tokens: 468
cheese.jpg: 39.80 seconds, prompt tokens: 1015, output tokens: 202
cocomilk.jpg: 75.80 seconds, prompt tokens: 1015, output tokens: 406
cookie.jpg: 117.51 seconds, prompt tokens: 1015, output tokens: 643
metat.jpg: 232.28 seconds, prompt tokens: 1015, output tokens: 1285
milk.jpg: 176.55 seconds, prompt tokens: 1015, output tokens: 973
nutsandseeds.jpg: 134.71 seconds, prompt tokens: 1015, output tokens: 739
pesto.jpg: 106.72 seconds, prompt tokens: 1015, output tokens: 582
redbull.jpg: 161.36 seconds, prompt tokens: 1015, output tokens: 888
sausages.jpg: 134.58 seconds, prompt tokens: 1015, output tokens: 736
softcheese.jpg: 93.97 seconds, prompt tokens: 1015, output tokens: 510
test.jpg: 85.85 seconds, prompt tokens: 1015, output tokens: 463
waffle.jpg: 110.10 seconds, prompt tokens: 1015, output tokens: 602

Average runtime: **120.51** sec
Total runtime: **1687.20** sec

# Model timing: gemma4:26b-a4b-it-qat

bread.jpg: 87.55 seconds, prompt tokens: 3219, output tokens: 565
carrots.jpg: 24.78 seconds, prompt tokens: 2041, output tokens: 521
cheese.jpg: 23.89 seconds, prompt tokens: 2311, output tokens: 199
cocomilk.jpg: 19.21 seconds, prompt tokens: 1784, output tokens: 417
cookie.jpg: 38.18 seconds, prompt tokens: 2765, output tokens: 731
nutsandseeds.jpg: 22.90 seconds, prompt tokens: 1801, output tokens: 655
redbull.jpg: 28.95 seconds, prompt tokens: 2645, output tokens: 226
sausages.jpg: 35.40 seconds, prompt tokens: 2397, output tokens: 927
test.jpg: 38.09 seconds, prompt tokens: 3055, output tokens: 470
waffle.jpg: 37.46 seconds, prompt tokens: 3153, output tokens: 301

Average runtime: **35.64** sec
Total runtime: **356.42** sec

# Model timing: paddleocr+gpt-5-jsonifier

bread.jpg: 68.19 seconds
carrots.jpg: 36.67 seconds
cheese.jpg: 30.29 seconds
cocomilk.jpg: 30.48 seconds
cookie.jpg: 51.43 seconds
metat.jpg: 28.58 seconds
milk.jpg: 46.03 seconds
nutsandseeds.jpg: 42.39 seconds
pesto.jpg: 32.50 seconds
redbull.jpg: 56.22 seconds
sausages.jpg: 69.71 seconds
softcheese.jpg: 10.08 seconds
test.jpg: 34.10 seconds
waffle.jpg: 50.13 seconds

Average runtime: **41.91** sec
Total runtime: **586.81** sec

# Model timing: gpt-5

bread.jpg: 31.95 seconds, image preparation seconds: 8.678, model response seconds: 23.251, time to first event seconds: 2.215, time to first text seconds: 21.294, stream event count: 288, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_19a015ca5e0845bb8c526b9b2b5690b1, openai response id: resp_082e7e56c8776367006a6ec536ddfc81989f3ee17a10f571d2, input tokens: 1498, output tokens: 2191, total tokens: 3689
carrots.jpg: 15.75 seconds, image preparation seconds: 0.173, model response seconds: 15.577, time to first event seconds: 1.556, time to first text seconds: 13.51, stream event count: 329, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_8a22ad512d65438a800a4e0105c9a898, openai response id: resp_0708a3c4b15c772a006a6ec54e07cc819ba731e81e02c53b05, input tokens: 1778, output tokens: 1724, total tokens: 3502
cheese.jpg: 20.21 seconds, image preparation seconds: 0.151, model response seconds: 20.061, time to first event seconds: 2.001, time to first text seconds: 18.732, stream event count: 147, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_fff63c398c3042e1b997abe1567785ad, openai response id: resp_0921eb1f29aad287006a6ec55e3b1c819991b5c790b8976f2d, input tokens: 1778, output tokens: 1499, total tokens: 3277
cocomilk.jpg: 26.86 seconds, image preparation seconds: 0.041, model response seconds: 26.817, time to first event seconds: 0.747, time to first text seconds: 23.539, stream event count: 377, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_96fa6dcdf4b341d698d0395b6c0e3125, openai response id: resp_01212a32102dd399006a6ec5714e28819b9a94e03a0210595d, input tokens: 1498, output tokens: 2715, total tokens: 4213
cookie.jpg: 25.16 seconds, image preparation seconds: 0.206, model response seconds: 24.953, time to first event seconds: 1.192, time to first text seconds: 21.38, stream event count: 242, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_24117b82140f4d098661dc4d64ce8db9, openai response id: resp_0332b243e9cbb5a8006a6ec58cbd00819998a50af0c445f55a, input tokens: 1498, output tokens: 2180, total tokens: 3678
metat.jpg: 33.29 seconds, image preparation seconds: 0.075, model response seconds: 33.212, time to first event seconds: 0.884, time to first text seconds: 30.296, stream event count: 399, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_9819cb60101d441aa7bfa897d20310f0, openai response id: resp_09096a863333ca7c006a6ec5a583cc81999449a385da91aa1b, input tokens: 1498, output tokens: 3310, total tokens: 4808
milk.jpg: 29.70 seconds, image preparation seconds: 0.208, model response seconds: 29.491, time to first event seconds: 2.023, time to first text seconds: 27.129, stream event count: 336, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_1cf829246af5467bb6811ab903b1adbd, openai response id: resp_00b217efb3628e94006a6ec5c7ef608199acacb9e2a7be985b, input tokens: 1498, output tokens: 2635, total tokens: 4133
nutsandseeds.jpg: 30.45 seconds, image preparation seconds: 0.038, model response seconds: 30.413, time to first event seconds: 0.722, time to first text seconds: 27.186, stream event count: 387, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_94a885e210584a03a9e8bee32937b37c, openai response id: resp_04e060ec2b817aad006a6ec5e458d8819a8e2284d897880000, input tokens: 1498, output tokens: 2847, total tokens: 4345
pesto.jpg: 38.19 seconds, image preparation seconds: 0.031, model response seconds: 38.157, time to first event seconds: 0.801, time to first text seconds: 34.224, stream event count: 431, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_81e92dafe0134c17b5e7106965b75a31, openai response id: resp_024bb642f59523d0006a6ec602d34c819a8a18475ac284e963, input tokens: 1498, output tokens: 3145, total tokens: 4643
redbull.jpg: 28.72 seconds, image preparation seconds: 0.157, model response seconds: 28.564, time to first event seconds: 1.446, time to first text seconds: 25.936, stream event count: 116, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_b8e28a17890b426bb8331a6916757be7, openai response id: resp_0aaeecd401710ccd006a6ec629d2648198bba4062d30151008, input tokens: 1498, output tokens: 1858, total tokens: 3356
sausages.jpg: 21.70 seconds, image preparation seconds: 0.062, model response seconds: 21.64, time to first event seconds: 0.841, time to first text seconds: 19.526, stream event count: 205, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_1564734057e84746be8a56bccee2410e, openai response id: resp_0e45d8f90cd11220006a6ec645c29881989aadb96d1052a740, input tokens: 1498, output tokens: 1874, total tokens: 3372
softcheese.jpg: 24.90 seconds, image preparation seconds: 0.036, model response seconds: 24.859, time to first event seconds: 0.763, time to first text seconds: 23.638, stream event count: 146, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_4e6c9102429a4828a58a3a338e341864, openai response id: resp_04fadbbb379703ad006a6ec65b6344819aa09aa7c03cfabce7, input tokens: 1498, output tokens: 1960, total tokens: 3458
test.jpg: 36.73 seconds, image preparation seconds: 0.029, model response seconds: 36.7, time to first event seconds: 0.709, time to first text seconds: 32.987, stream event count: 363, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_3915c33b23624346bdc635c97d61e9d6, openai response id: resp_00aeaf026adacd5a006a6ec6743e18819a988e035699e75db9, input tokens: 1778, output tokens: 2776, total tokens: 4554
waffle.jpg: 32.28 seconds, image preparation seconds: 0.034, model response seconds: 32.243, time to first event seconds: 1.224, time to first text seconds: 30.232, stream event count: 276, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_7e046c1fde2847e0ae311e023b4a2cab, openai response id: resp_03188308c5b20e17006a6ec69939008199b3c4220533c1d879, input tokens: 1498, output tokens: 2543, total tokens: 4041

Average runtime: **28.28** sec
Total runtime: **395.89** sec

# Model timing: paddleocr+gpt-5-jsonifier

bread.jpg: 83.50 seconds
carrots.jpg: 31.93 seconds
cheese.jpg: 25.88 seconds
cocomilk.jpg: 33.24 seconds
cookie.jpg: 66.59 seconds
metat.jpg: 50.14 seconds
milk.jpg: 42.96 seconds
nutsandseeds.jpg: 45.87 seconds
pesto.jpg: 30.23 seconds
redbull.jpg: 58.46 seconds
sausages.jpg: 44.21 seconds
softcheese.jpg: 11.94 seconds
test.jpg: 47.90 seconds
waffle.jpg: 38.61 seconds

Average runtime: **43.68** sec
Total runtime: **611.46** sec

# Model timing: gpt-5

bread.jpg: 32.43 seconds, image preparation seconds: 3.96, model response seconds: 28.445, time to first event seconds: 1.955, time to first text seconds: 25.741, stream event count: 272, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_4a2f7ae6ebdd4c4c8969ee0d0aeec2fd, openai response id: resp_0ac07cd79b183070006a6ecc4e731c8199ab95c8b2ab9b7893, input tokens: 1498, output tokens: 2023, total tokens: 3521
carrots.jpg: 40.09 seconds, image preparation seconds: 0.143, model response seconds: 39.95, time to first event seconds: 1.053, time to first text seconds: 38.049, stream event count: 202, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_c81466cf86764d528da803c66a37554d, openai response id: resp_0eca9d6d1c187bde006a6ecc6a6034819891ecbd2a09f6ab58, input tokens: 1778, output tokens: 2387, total tokens: 4165
cheese.jpg: 25.27 seconds, image preparation seconds: 0.151, model response seconds: 25.114, time to first event seconds: 1.498, time to first text seconds: 23.567, stream event count: 164, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_96732ddf7b884617851b1bba2de2c2aa, openai response id: resp_0c49637b5658c829006a6ecc92e000819bb90a328e2d0d59ad, input tokens: 1778, output tokens: 1546, total tokens: 3324
cocomilk.jpg: 24.30 seconds, image preparation seconds: 0.037, model response seconds: 24.266, time to first event seconds: 0.663, time to first text seconds: 21.01, stream event count: 367, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_86a7a62ff1994437a2fb3529690e6f69, openai response id: resp_0042cb8b731d0cce006a6eccab5c5c8199b49e403c054cf956, input tokens: 1498, output tokens: 2105, total tokens: 3603
cookie.jpg: 33.45 seconds, image preparation seconds: 0.132, model response seconds: 33.321, time to first event seconds: 1.124, time to first text seconds: 30.924, stream event count: 235, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_6a477716606749c892e91fd07ac48c8a, openai response id: resp_008727b4ac5d1a2f006a6eccc41928819baf8692960cb335a4, input tokens: 1498, output tokens: 2050, total tokens: 3548
metat.jpg: 48.75 seconds, image preparation seconds: 0.051, model response seconds: 48.698, time to first event seconds: 2.861, time to first text seconds: 45.676, stream event count: 379, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_a0009a7cd4254a51a1718ce9c72bdb25, openai response id: resp_048121cc63730243006a6ecce55598819990019361bb38c1f3, input tokens: 1498, output tokens: 3187, total tokens: 4685
milk.jpg: 43.48 seconds, image preparation seconds: 0.154, model response seconds: 43.324, time to first event seconds: 1.803, time to first text seconds: 40.168, stream event count: 359, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_055d66d01fa149a3890594258cfc7800, openai response id: resp_06f7df34bc0712b0006a6ecd170d70819a9b36e98e13058432, input tokens: 1498, output tokens: 3310, total tokens: 4808
nutsandseeds.jpg: 26.20 seconds, image preparation seconds: 0.04, model response seconds: 26.163, time to first event seconds: 0.811, time to first text seconds: 23.545, stream event count: 357, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_cfef22ee9e2c4d17af61d5cbaec92a1b, openai response id: resp_0cad301887fbcb6b006a6ecd4177ac819ba7c8aa50f84a3967, input tokens: 1498, output tokens: 1995, total tokens: 3493
pesto.jpg: 49.67 seconds, image preparation seconds: 0.041, model response seconds: 49.631, time to first event seconds: 0.692, time to first text seconds: 45.45, stream event count: 437, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_2d7bcae6c21b4cc1b95bf8b32a9ac93b, openai response id: resp_0c7c3462768c19d8006a6ecd5ba294819aaae10cbe67b96ffc, input tokens: 1498, output tokens: 3213, total tokens: 4711
redbull.jpg: 85.82 seconds, image preparation seconds: 0.225, model response seconds: 85.592, time to first event seconds: 2.178, time to first text seconds: 84.205, stream event count: 116, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_3fbfb1ee469340178065e969dc9ebe58, openai response id: resp_0d99c5b26c26fec5006a6ecd8eaafc819babb3e470f7ccef4b, input tokens: 1498, output tokens: 4268, total tokens: 5766
sausages.jpg: 27.98 seconds, image preparation seconds: 0.045, model response seconds: 27.932, time to first event seconds: 1.111, time to first text seconds: 25.821, stream event count: 214, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_b10dbfa21b6d4845bc1e7b9317ea5c62, openai response id: resp_0283ac22b7352599006a6ecde36d988199afb99a3e9e01ce5c, input tokens: 1498, output tokens: 1597, total tokens: 3095
softcheese.jpg: 47.88 seconds, image preparation seconds: 0.051, model response seconds: 47.83, time to first event seconds: 1.61, time to first text seconds: 46.412, stream event count: 131, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_12a7f7e6a22142aaad771189700d6e80, openai response id: resp_0a33f77acb693b73006a6ecdff1214819b8fec4ed444a968b2, input tokens: 1498, output tokens: 2804, total tokens: 4302
test.jpg: 34.89 seconds, image preparation seconds: 0.03, model response seconds: 34.86, time to first event seconds: 0.939, time to first text seconds: 30.128, stream event count: 337, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_0679d1959689413b9517946d808c897a, openai response id: resp_097b4ef0dbd1a0b8006a6ece2f25788199bd5fe3ffc7ac55c9, input tokens: 1778, output tokens: 2319, total tokens: 4097
waffle.jpg: 40.90 seconds, image preparation seconds: 0.046, model response seconds: 40.849, time to first event seconds: 0.705, time to first text seconds: 38.64, stream event count: 277, stream last event: response.completed, json parsing seconds: 0.0, openai request id: req_18dfb73da1d8461197ebe5c46639ead6, openai response id: resp_0465e5dc4551d270006a6ece51ce78819890b57c344924fba3, input tokens: 1498, output tokens: 2547, total tokens: 4045

Average runtime: **40.08** sec
Total runtime: **561.11** sec

# Model timing: gemma3:12b-it-q8_0

bread.jpg: 37.27 seconds, prompt tokens: 1015, output tokens: 502
carrots.jpg: 19.70 seconds, prompt tokens: 1015, output tokens: 510
cheese.jpg: 10.82 seconds, prompt tokens: 1015, output tokens: 255
cocomilk.jpg: 17.92 seconds, prompt tokens: 1015, output tokens: 466
cookie.jpg: 19.78 seconds, prompt tokens: 1015, output tokens: 515
metat.jpg: 38.17 seconds, prompt tokens: 1015, output tokens: 1049
milk.jpg: 31.01 seconds, prompt tokens: 1015, output tokens: 839
nutsandseeds.jpg: 24.79 seconds, prompt tokens: 1015, output tokens: 664
pesto.jpg: 20.04 seconds, prompt tokens: 1015, output tokens: 528
redbull.jpg: 25.64 seconds, prompt tokens: 1015, output tokens: 682
sausages.jpg: 38.89 seconds, prompt tokens: 1015, output tokens: 1072
softcheese.jpg: 17.33 seconds, prompt tokens: 1015, output tokens: 448
test.jpg: 19.41 seconds, prompt tokens: 1015, output tokens: 493
waffle.jpg: 28.45 seconds, prompt tokens: 1015, output tokens: 770

Average runtime: **24.94** sec
Total runtime: **349.21** sec

# Model timing: gemma4:12b

bread.jpg: 54.14 seconds, prompt tokens: 2506, output tokens: 259
carrots.jpg: 134.74 seconds, status: failed, openai request id: None, error: ValueError: Ollama model gemma4:12b (done_received=True, done_reason='length', thinking_chars=8903) returned an empty response.
cheese.jpg: 30.79 seconds, prompt tokens: 2136, output tokens: 177
cocomilk.jpg: 35.97 seconds, prompt tokens: 2156, output tokens: 401
cookie.jpg: 43.29 seconds, prompt tokens: 2646, output tokens: 224
metat.jpg: 66.44 seconds, prompt tokens: 3313, output tokens: 543
milk.jpg: 39.02 seconds, prompt tokens: 2317, output tokens: 331
nutsandseeds.jpg: 61.23 seconds, prompt tokens: 3339, output tokens: 281
pesto.jpg: 40.03 seconds, prompt tokens: 2256, output tokens: 476
redbull.jpg: 30.41 seconds, prompt tokens: 2087, output tokens: 174
sausages.jpg: 65.75 seconds, prompt tokens: 3539, output tokens: 279
softcheese.jpg: 128.95 seconds, prompt tokens: 3435, output tokens: 165
test.jpg: 67.71 seconds, prompt tokens: 3460, output tokens: 478
waffle.jpg: 53.66 seconds, prompt tokens: 3029, output tokens: 246

Average runtime: **60.87** sec
Total runtime: **852.14** sec

# Model timing: gemma4:e4b

bread.jpg: 33.71 seconds, prompt tokens: 2028, output tokens: 302
carrots.jpg: 16.46 seconds, prompt tokens: 2200, output tokens: 182
cheese.jpg: 13.81 seconds, prompt tokens: 1968, output tokens: 180
cocomilk.jpg: 13.30 seconds, prompt tokens: 1982, output tokens: 149
cookie.jpg: 15.19 seconds, prompt tokens: 2138, output tokens: 150
metat.jpg: 16.11 seconds, prompt tokens: 2206, output tokens: 179
milk.jpg: 16.32 seconds, prompt tokens: 2185, output tokens: 187
nutsandseeds.jpg: 14.32 seconds, prompt tokens: 2085, output tokens: 120
pesto.jpg: 15.62 seconds, prompt tokens: 2094, output tokens: 247
redbull.jpg: 16.64 seconds, prompt tokens: 2170, output tokens: 260
sausages.jpg: 16.39 seconds, prompt tokens: 2212, output tokens: 222
softcheese.jpg: 16.31 seconds, prompt tokens: 2242, output tokens: 172
test.jpg: 14.72 seconds, prompt tokens: 2112, output tokens: 174
waffle.jpg: 15.63 seconds, prompt tokens: 2241, output tokens: 109

Average runtime: **16.75** sec
Total runtime: **234.55** sec

# Model timing: gemma3:27b-it-q4_K_M

bread.jpg: 126.90 seconds, prompt tokens: 1015, output tokens: 568
carrots.jpg: 85.65 seconds, prompt tokens: 1015, output tokens: 468
cheese.jpg: 39.20 seconds, prompt tokens: 1015, output tokens: 202
cocomilk.jpg: 76.13 seconds, prompt tokens: 1015, output tokens: 406
cookie.jpg: 116.47 seconds, prompt tokens: 1015, output tokens: 643
metat.jpg: 230.73 seconds, prompt tokens: 1015, output tokens: 1285
milk.jpg: 175.10 seconds, prompt tokens: 1015, output tokens: 973
nutsandseeds.jpg: 133.81 seconds, prompt tokens: 1015, output tokens: 739
pesto.jpg: 105.50 seconds, prompt tokens: 1015, output tokens: 582
redbull.jpg: 159.73 seconds, prompt tokens: 1015, output tokens: 888
sausages.jpg: 132.94 seconds, prompt tokens: 1015, output tokens: 736
softcheese.jpg: 96.53 seconds, prompt tokens: 1015, output tokens: 510
test.jpg: 88.63 seconds, prompt tokens: 1015, output tokens: 463
waffle.jpg: 114.40 seconds, prompt tokens: 1015, output tokens: 602

Average runtime: **120.12** sec
Total runtime: **1681.72** sec

# Model timing: gemma4:26b-a4b-it-qat

bread.jpg: 70.57 seconds, prompt tokens: 3219, output tokens: 565
carrots.jpg: 25.75 seconds, prompt tokens: 2041, output tokens: 521
cheese.jpg: 24.92 seconds, prompt tokens: 2311, output tokens: 199
cocomilk.jpg: 20.10 seconds, prompt tokens: 1784, output tokens: 417
cookie.jpg: 39.71 seconds, prompt tokens: 2765, output tokens: 731
metat.jpg: 90.66 seconds, status: failed, openai request id: None, error: RuntimeError: Ollama error: {"error":{"code":400,"message":"Failed to tokenize prompt","type":"invalid_request_error"}}
milk.jpg: 96.31 seconds, status: failed, openai request id: None, error: ValueError: Ollama model gemma4:26b-a4b-it-qat (done_received=True, done_reason='length', thinking_chars=11153) returned an empty response.
nutsandseeds.jpg: 23.66 seconds, prompt tokens: 1801, output tokens: 655
pesto.jpg: 76.84 seconds, prompt tokens: 2425, output tokens: 544
redbull.jpg: 29.94 seconds, prompt tokens: 2645, output tokens: 226
sausages.jpg: 36.45 seconds, prompt tokens: 2397, output tokens: 927
softcheese.jpg: 88.87 seconds, status: failed, openai request id: None, error: RuntimeError: Ollama error: {"error":{"code":400,"message":"Failed to tokenize prompt","type":"invalid_request_error"}}
test.jpg: 39.52 seconds, prompt tokens: 3055, output tokens: 470
waffle.jpg: 38.68 seconds, prompt tokens: 3153, output tokens: 301

Average runtime: **50.14** sec
Total runtime: **701.97** sec

# Model timing: gemma4:E4B

bread.jpg: 20.38 seconds, prompt tokens: 0, output tokens: 0
carrots.jpg: 14.45 seconds, prompt tokens: 0, output tokens: 0
cheese.jpg: 20.67 seconds, prompt tokens: 0, output tokens: 0
cocomilk.jpg: 21.16 seconds, status: failed, openai request id: None, error: RuntimeError: llama-server returned an invalid SSE event: '{"choices":[{"finish_reason":null,"index":0,"delta":{"content":" Ð²ÐµÑ\x80Ñ' <- JSONDecodeError: Unterminated string starting at: line 1 column 64 (char 63)
cookie.jpg: 14.54 seconds, prompt tokens: 0, output tokens: 0
metat.jpg: 21.17 seconds, prompt tokens: 0, output tokens: 0
milk.jpg: 12.20 seconds, status: failed, openai request id: None, error: RuntimeError: llama-server returned an invalid SSE event: '{"choices":[{"finish_reason":null,"index":0,"delta":{"reasoning_content":" Ñ\x81Ð°Ñ' <- JSONDecodeError: Unterminated string starting at: line 1 column 74 (char 73)
nutsandseeds.jpg: 9.48 seconds, status: failed, openai request id: None, error: RuntimeError: llama-server returned an invalid SSE event: '{"choices":[{"finish_reason":null,"index":0,"delta":{"reasoning_content":"Ñ' <- JSONDecodeError: Unterminated string starting at: line 1 column 74 (char 73)
pesto.jpg: 15.10 seconds, prompt tokens: 0, output tokens: 0
redbull.jpg: 15.80 seconds, prompt tokens: 0, output tokens: 0
sausages.jpg: 17.02 seconds, status: failed, openai request id: None, error: RuntimeError: llama-server returned an invalid SSE event: '{"choices":[{"finish_reason":null,"index":0,"delta":{"reasoning_content":"Ñ' <- JSONDecodeError: Unterminated string starting at: line 1 column 74 (char 73)
softcheese.jpg: 18.87 seconds, status: failed, openai request id: None, error: RuntimeError: llama-server returned an invalid SSE event: '{"choices":[{"finish_reason":null,"index":0,"delta":{"reasoning_content":"Ñ' <- JSONDecodeError: Unterminated string starting at: line 1 column 74 (char 73)
test.jpg: 13.87 seconds, prompt tokens: 0, output tokens: 0
waffle.jpg: 26.00 seconds, prompt tokens: 0, output tokens: 0

Average runtime: **17.19** sec
Total runtime: **240.72** sec

# Model timing: gemma4:E4B

bread.jpg: 17.47 seconds, prompt tokens: 0, output tokens: 0
carrots.jpg: 14.25 seconds, prompt tokens: 0, output tokens: 0
cheese.jpg: 12.07 seconds, prompt tokens: 0, output tokens: 0
cocomilk.jpg: 13.83 seconds, prompt tokens: 0, output tokens: 0
cookie.jpg: 14.35 seconds, prompt tokens: 0, output tokens: 0
metat.jpg: 20.92 seconds, prompt tokens: 0, output tokens: 0
milk.jpg: 13.89 seconds, prompt tokens: 0, output tokens: 0
nutsandseeds.jpg: 16.19 seconds, prompt tokens: 0, output tokens: 0
pesto.jpg: 14.12 seconds, prompt tokens: 0, output tokens: 0
redbull.jpg: 17.58 seconds, prompt tokens: 0, output tokens: 0
sausages.jpg: 21.83 seconds, prompt tokens: 0, output tokens: 0
softcheese.jpg: 16.51 seconds, prompt tokens: 0, output tokens: 0
test.jpg: 13.38 seconds, prompt tokens: 0, output tokens: 0
waffle.jpg: 178.16 seconds, prompt tokens: 0, output tokens: 0

Average runtime: **27.47** sec
Total runtime: **384.56** sec

# Model timing: gemma4:12b

bread.jpg: 24.16 seconds, prompt tokens: 1016, output tokens: 334
carrots.jpg: 12.21 seconds, prompt tokens: 1016, output tokens: 481
cheese.jpg: 6.12 seconds, prompt tokens: 1016, output tokens: 199
cocomilk.jpg: 10.90 seconds, prompt tokens: 1016, output tokens: 418
cookie.jpg: 6.60 seconds, prompt tokens: 1016, output tokens: 230
metat.jpg: 18.43 seconds, prompt tokens: 1016, output tokens: 746
milk.jpg: 359.37 seconds, prompt tokens: 1016, output tokens: 259
nutsandseeds.jpg: 10.85 seconds, prompt tokens: 1016, output tokens: 416
pesto.jpg: 18.13 seconds, prompt tokens: 1016, output tokens: 498
redbull.jpg: 703.82 seconds, status: failed, openai request id: None, error: ValueError: Ollama model gemma4:12b (done_received=True, done_reason='length', thinking_chars=0) returned invalid JSON at line 2, column 22: Unterminated string starting at. Response preview: '{\n  "recognized_text": "ALL\\n0.25l\\ne\\n4 917010 042006\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\nSüppejätke\\n' <- JSONDecodeError: Unterminated string starting at: line 2 column 22 (char 23)
sausages.jpg: 710.16 seconds, status: failed, openai request id: None, error: ValueError: Ollama model gemma4:12b (done_received=True, done_reason='length', thinking_chars=0) returned invalid JSON at line 2, column 22: Unterminated string starting at. Response preview: '{\n  "recognized_text": "НЕОБЕВОРЕННИЙ ПРОДУКТ. МОЛОЧНЕ КОНЦЕНТРАТIВНЕ БАВНЯНЕ\\nПИТТЯ. В СУМПІШІ, СУШИВОНЕ, МАСЦА НЕТТО 40 Г.\\n\\nОБЕРЕЖНО! ПРОДУКТ ВИРОБЛЕНИЙ ДЛЯ ВІДКОРЕННЯ.\\nОБЕРЕЖНО! ПРОДУКТ ВИРОБЛЕНИЙ ДЛЯ ВІДКОРЕННЯ.\\nОБЕРЕЖНО! ПРОДУКТ ВИРОБЛЕНИЙ ДЛЯ ВІДКОРЕННЯ.\\nОБЕРЕЖНО! ПРОДУКТ ВИРОБЛЕНИЙ ДЛЯ ВІДКОРЕННЯ.\\nОБЕРЕЖНО! ПРОДУКТ ВИРОБЛЕНИЙ ДЛЯ ВІДКОРЕННЯ.\\nОБЕРЕЖНО! ПРОДУКТ ВИРОБЛЕНИЙ ДЛЯ ВІДКОРЕННЯ.\\nОБЕРЕЖНО! ПРОДУКТ ВИРОБЛЕНИЙ ДЛЯ ВІДКОРЕННЯ.\\nОБЕРЕЖНО! ПРОДУКТ ВИРОБЛЕНИЙ ДЛЯ ВІДКОРЕННЯ.\\nОБЕР' <- JSONDecodeError: Unterminated string starting at: line 2 column 22 (char 23)
softcheese.jpg: 7.67 seconds, prompt tokens: 1016, output tokens: 260
test.jpg: 10.32 seconds, prompt tokens: 1016, output tokens: 395
waffle.jpg: 706.60 seconds, status: failed, openai request id: None, error: ValueError: Ollama model gemma4:12b (done_received=True, done_reason='length', thinking_chars=0) returned invalid JSON at line 1, column 21: Unterminated string starting at. Response preview: '{"recognized_text": "RU ВКОЛI С\\nСО ВКОМO\\n\\nСОСТАВ: \\u0432\\u043e\\u0434\\u0430, \\u043b\\u0435\\u0431\\u0438\\u0442\\u0438\\u043d, \\u043a\\u043e\\u043d\\u043e\\u0431\\u0435\\u0440, \\u043f\\u0438\\u0432\\u0430\\u043b\\u043a\\u0430, \\u043d\\u0430\\u0442\\u0440\\u0438\\u0439, \\u043f\\u043e\\u0434\\u0431\\u0438\\u043b\\u044f\\u0438\\u0442\\u0435\\u043b\\u044c, \\u043e\\u0431\\u043e\\u0431\\u0431\\u0430, \\u043a\\u0430\\u043b\\u0438\\u0443\\u043c, \\u0432\\u043e\\u0434\\u0430, \\u043f\\u043e\\u0431\\u0435\\u043b\\u0438\\u0442\\u0430, \\u043a\\u0430\\u043b\\u0438\\' <- JSONDecodeError: Unterminated string starting at: line 1 column 21 (char 20)

Average runtime: **186.10** sec
Total runtime: **2605.33** sec

# Model timing: gemma4:26b-a4b-it-qat

bread.jpg: 39.50 seconds, prompt tokens: 1016, output tokens: 536
carrots.jpg: 9.36 seconds, prompt tokens: 1016, output tokens: 485
cheese.jpg: 5.49 seconds, prompt tokens: 1016, output tokens: 220
cocomilk.jpg: 10.42 seconds, prompt tokens: 1016, output tokens: 579
cookie.jpg: 5.74 seconds, prompt tokens: 1016, output tokens: 249
metat.jpg: 12.07 seconds, prompt tokens: 1016, output tokens: 693
milk.jpg: 15.94 seconds, prompt tokens: 1016, output tokens: 945
nutsandseeds.jpg: 11.98 seconds, prompt tokens: 1016, output tokens: 695
pesto.jpg: 9.22 seconds, prompt tokens: 1016, output tokens: 497
redbull.jpg: 455.67 seconds, status: failed, openai request id: None, error: ValueError: Ollama model gemma4:26b-a4b-it-qat (done_received=True, done_reason='length', thinking_chars=0) returned invalid JSON at line 1, column 21: Unterminated string starting at. Response preview: '{"recognized_text": "0,25 л\\nEHL\\n9 002490\\"207434\\"\\nALU\\n505, тен. 8-800-5023.\\nул. Муртазаева, 180, Алматы,\\nКазахстан; Республика\\nКазахстан; Qaz\\nпредставитель: ТОО \\"Red Bull\\"\\nИмпортозаменитель:\\n(Бул Гиб) (Ай Барукан, 1,530, Фулл-эм-386, Астана,\\nНазарбаевтану, Район; Туран; по заказу Red Bull\\nRed Bull Sugarfree (Ред Булл без сахара)\\n(Бул Гиб) (Ай Барукан, 1,530, Фулл-эм-386, Астана,\\nНазарбаевтану, Район; Туран; по заказу Red Bull\\nRed Bull Sugarfree (Ред Булл без сахара)\\n(Бул Гиб) ' <- JSONDecodeError: Unterminated string starting at: line 1 column 21 (char 20)
sausages.jpg: 9.97 seconds, prompt tokens: 1016, output tokens: 535
softcheese.jpg: 5.86 seconds, prompt tokens: 1016, output tokens: 271
test.jpg: 8.31 seconds, prompt tokens: 1016, output tokens: 436
waffle.jpg: 12.17 seconds, prompt tokens: 1016, output tokens: 701

Average runtime: **43.69** sec
Total runtime: **611.70** sec

# Model timing: gemma4:31b-it-qat

bread.jpg: 147.51 seconds, prompt tokens: 1016, output tokens: 411
carrots.jpg: 141.02 seconds, prompt tokens: 1016, output tokens: 453
cheese.jpg: 82.03 seconds, prompt tokens: 1016, output tokens: 259
cocomilk.jpg: 137.76 seconds, prompt tokens: 1016, output tokens: 444
cookie.jpg: 84.80 seconds, prompt tokens: 1016, output tokens: 269
metat.jpg: 279.16 seconds, prompt tokens: 1016, output tokens: 900
milk.jpg: 286.03 seconds, prompt tokens: 1016, output tokens: 930
nutsandseeds.jpg: 236.15 seconds, prompt tokens: 1016, output tokens: 766
pesto.jpg: 156.79 seconds, prompt tokens: 1016, output tokens: 506
redbull.jpg: 286.29 seconds, prompt tokens: 1016, output tokens: 929
sausages.jpg: 324.02 seconds, prompt tokens: 1016, output tokens: 1049
softcheese.jpg: 57.79 seconds, prompt tokens: 1016, output tokens: 178
test.jpg: 140.26 seconds, prompt tokens: 1016, output tokens: 450
waffle.jpg: 221.29 seconds, prompt tokens: 1016, output tokens: 716

Average runtime: **184.35** sec
Total runtime: **2580.92** sec