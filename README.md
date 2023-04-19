# Body Level Classification

## Data Set:
### Quick Statistics:
-   1477 data samples.
-   16 attributes (+1 for classes).
-   4 output classes.
### Split:
-   The data was split into 70% Training, 20% Validation & 10% Test. (1033, 296 & 148 data samples respectively).
-   They are available in the data directory in the train.csv, val.csv and test.csv files respectively.

### Attributes Description:
-   Gender: Male or female.
-   Age: Numeric value.
-   Height: Numeric value (in meters).
-   Weight: Numeric value (in kilograms).
-   Fam_Hist: Does the family have a history with obesity?
-   H_Cal_Consump: High caloric food consumption.
-   Veg_Consump: Frequency of vegetables consumption.
-   Meal_Count: Average number of meals per day.
-   Food_Between_Meals: Frequency of eating between meals.
-   Smoking: Is the person smoking?
-   Water_Consump: Frequency of water consumption.
-   H_Cal_Burn: Does the body have high calories burn rate?
-   Phys_Act: How often does the person do physical activities?
-   Time_E_Dev: How much time does person spend on electronic devices.
-   Alcohol_Consump: Frequency of alcohols consumption.
-   Transport: Which transports does the person usually use?
-   Body_Level: Class of human body level.

## Models Trained:
### 1. Multinomial Logistic Regression:
-   Achieved an accuracy of 84.79% Accuracy, Macro Precision: 0.8397, Macro Recall: 0.78297 & Macro F1-score: 0.78337 on the validation data set.
-   Used 500 as the maximum number of iterations and it seems enough for it to converge since the data is small. Also, tried manually larger values as 5000 but no noticeable change.