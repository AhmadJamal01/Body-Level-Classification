# Body Level Classification

## Data Set:
### Quick Statistics:
-   1477 data samples.
-   16 attributes (+1 for classes) [8 categorical and 8 numerical].
-   4 output classes.
### Split:
-   The data was split into `70% Training, 20% Validation & 10% Test.` (1033, 296 & 148 data samples respectively).
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

### Basic Analysis & Visualization:
- Basic Data Analysis was performed in `analyze.ipynb`. Also, detected some outliers and used a baseline measure: ZeroR which resulted in 47.297% accuracy and macro F1 of 0.1605.
- Used multiple ways to visualize the data in `visualize_data.ipynb` as bar charts, histograms, scatter, boxplots and a heatmap.
### Preprocssing:
- Converted all the categorical data to numerical data by converting them to one hot encoding vectors manually in `all_numerical_data.ipynb`.
- To use it, simply write `%run "../all_numerical_data.ipynb"` at the beginning of your notebook and then directly use x_train, y_train, x_val and y_val afterwards.
## Models Trained:
### 1. Multinomial Logistic Regression:
-   Achieved an accuracy of `84.79%` Accuracy, Macro Precision: 0.8397, Macro Recall: 0.78297 & Macro F1-score: `0.78337` on the validation data set.
-   Used 10000 as the maximum number of iterations since it seems enough for it to converge since the data is small. Also, tried manually smaller values as 500 which are sometimes also enough for it to converge.
### 2. Multi-class Decision Tree:
-   Achieved an accuracy of `95.608%` Accuracy, Macro Precision: 0.9324, Macro Recall: 0.93246 & Macro F1-score: `0.93196` on the validation data set.
- Used criterion as `"entropy"` instead of the default "gini".
### 3. Multi-class Random Forest:
-   Achieved an accuracy of `97.297%` Accuracy, Macro Precision: 0.95739, Macro Recall: 0.9524 & Macro F1-score: `0.95473` on the validation data set. This result was achieved with `1000 estimators`.
- Used criterion as `"entropy"` instead of the default "gini".
### 4. Multinomial Naïve Bayes:
- Achieved an accuracy of `64.189%` Accuracy, Macro Precision: 0.59559, Macro Recall: 0.60417 & Macro F1-score: `0.598796` on the validation data set.
- Had to convert all numerical data to ranges/bins. Tried 10, 16 & 30 bins with `30 bins` resulting in the highest accuracy.