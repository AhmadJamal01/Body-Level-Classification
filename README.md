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
| Feature            | Description                                            |
|--------------------|--------------------------------------------------------|
| Gender             | Male or female.                                        |
| Age                | Numeric value.                                         |
| Height             | Numeric value (in meters).                              |
| Weight             | Numeric value (in kilograms).                           |
| Fam_Hist           | Does the family have a history with obesity?           |
| H_Cal_Consump      | High caloric food consumption.                          |
| Veg_Consump        | Frequency of vegetables consumption.                   |
| Meal_Count         | Average number of meals per day.                        |
| Food_Between_Meals | Frequency of eating between meals.                      |
| Smoking            | Is the person smoking?                                  |
| Water_Consump      | Frequency of water consumption.                         |
| H_Cal_Burn         | Does the body have high calories burn rate?             |
| Phys_Act           | How often does the person do physical activities?       |
| Time_E_Dev         | How much time does person spend on electronic devices.  |
| Alcohol_Consump    | Frequency of alcohols consumption.                      |
| Transport          | Which transports does the person usually use?           |
| Body_Level         | Class of human body level.                              |

### Basic Analysis & Visualization:
- Basic Data Analysis was performed in `analyze.ipynb`. Also, detected some outliers and used a baseline measure: ZeroR which resulted in 47.297% accuracy and macro F1 of 0.1605.
- Used multiple ways to visualize the data in `visualize_data.ipynb` as bar charts, histograms, scatter, boxplots and a heatmap.

### Class Imbalance Analysis
- Analyzed the class imbalance and found that Body Levels 1 -> 4 are `0.137464`, `0.130687`, `0.274927`, and `0.456922`.
- Analyzed the features & their correlation/connection to the `Body_Level` and found that all the features are at least statistically related to `Body_Level` and after further investigation, the `Weight` feature the most correlated (0.85) to the `Body_Level`, followed by `Fam_Hist`, and `Age`.
- Attempted to solve the class Imbalance by both over-sampling & under-sampling.
- Attempted to solve the class Imbalance using synthetic data generation once without using the relationship between features & once while taking them into account. 
### Preprocssing:
- Converted all the categorical data to numerical data by converting them to one hot encoding vectors manually in `all_numerical_data.ipynb`.
- To use it, simply write `%run "../all_numerical_data.ipynb"` at the beginning of your notebook and then directly use x_train, y_train, x_val and y_val afterwards.
## Models Trained:
### SVM 
| Model | Accuracy | Weighted F1-Score |
|-------|----------|--------------------|
| Linear SVM | 69.90 % | 63.00% |
| Linear SVM with C=0.1 | 76.35% | 74.00% |
| Linear SVM with C=0.03 | 80.00% | 80.00% |
| Linear SVM with C=0.04 | 80.00% | 80.00% |
| Linear SVM with C=0.03 , tol=0.001 | 80.04% | 78.00% |
| Non Linear SVM with kernel =rbf | 76.35% | 75.00% |
| Non Linear SVM with kernel =rbf, gamma= 0.008 | 80.07% | 79.00% |
| Non Linear SVM with kernel =rbf, gamma= 0.05 | 90.08% | 90.00% |
| Non Linear SVM with kernel =rbf, gamma= 0.001 | 77.02% | 76.00% |
| Non Linear SVM with kernel =rbf, gamma= 0.05 , C=2 | 92.22% | 92.00% |
| Non Linear SVM with kernel =rbf, gamma= 0.05 , C=3 | 93.24% | 93.00% |
| Non Linear SVM with kernel =linear |91.89% |92.00% |
| Non Linear SVM with kernel =linear with C=2 |93.58% |93.00% |
| Non Linear SVM with kernel =linear with C=2, gamma=0.05 |93.58% |93.00% |
| Non Linear SVM with kernel = Sigmoid |25.33% |19.00% |
| Non Linear SVM with kernel = Poly |72.97% |72.00% |
| Non Linear SVM with kernel = Poly, gamma=0.05 |97.29% |97.00% |
| Non Linear SVM with kernel = Poly, gamma=0.05, C=2 |97.29% |97.00%
### Logistic Regression
| Penalty | Solver | C | Accuracy | Macro F1-Score |
|---------|--------|---|----------|----------------|
| 'l2' | 'liblinear' | 1.0 (default) | 84.79% | 78.34% |
| 'l2' | 'lbfgs' | 1.0 (default) | 83.78% | 77.44% |
| 'l2' | 'newton-cg' | 1.0 (default) | 84.12% | 77.71% |
| 'l2' | 'sag' | 1.0 (default) | 83.11% | 77.17% |
| 'l2' | 'saga' | 1.0 (default) | 81.76% | 74.96% |
| 'l1' | 'liblinear' | 1.0 (default) | 88.51% | 83.16% |
| 'l1' | 'liblinear' | 100000.0 | 90.54% | 86.10% |
| 'l2' | 'liblinear' | 0.0001 | 51.01% | 24.12% |
| 'l2' | 'liblinear' | 100000.0 | 90.54% | 86.24% |

### Gaussian Mixture 
| n_components | covariance_type | reg_covar | n_init | Accuracy | F1-Score |
|--------------|-----------------|-----------|--------|----------|----------|
| 1            | 'full’          | 0.0001    | 1      | 86.00%   | 86.00%   |
| 1            | ‘full’          | 0.0001    | 4      | 86.00%   | 86.00%   |
| 7            | ‘full’          | 0.0001    | 1      | 72.00%   | 69.00%   |
| 2            | ‘full’          | 0.0001    | 1      | 72.00%   | 67.00%   |
| 3            | ‘full’          | 0.0001    | 1      | 75.00%   | 71.00%   |
| 1            | 'full’          | 0.0001    | 10     | 86.00%   | 86.00%   |
| 1            | ‘tied’          | 0.0001    | 1      | 86.00%   | 86.00%   |
| 1            | ‘diag’          | 0.0001    | 1      | 67.00%   | 62.00%   |
| 1            | ‘spherical’     | 0.0001    | 1      |47.00%    |30.00%    |

### Multi-class Random Forest
| n_estimators | max_features | criterion | Accuracy | Weighted F1-Score |
|--------------|--------------|-----------|----------|------------------|
| 100          | ‘sqrt’       | ‘gini’    | 94.59%   | 95.00%           |
| 1000         | None         | ‘gini’    | 96.95%   | 97.00%           |
| 1000         | None         | "entropy" | 97.29%   | 97.00%           |

### Multinomial Naïve Bayes
| Data Type | Accuracy | Weighted F1-Score |
|--------------------------------------|----------|------------------|
| Numerical Data to Categorical in 10 bins | 63.17%   | 62.00%           |
| Numerical Data to Categorical in 16 bins | 64.52%   | 65.00%           |
| Numerical Data to Categorical in 30 bins | 64.18%   | 65.00%           |
| All numerical data (1 hot coded vectors) | 70.61%   | 70.00%           |
| All data as is                        | 70.95%   | 70.00%           |
### K Nearest Neighbors
| Dataset Type        | Accuracy |
|---------------------|----------|
| Original Dataset    | 77%      |
| Undersampled        | 74%      |
| Oversampled         | 77%      |
| Smote               | 77%      |
| Smote with Importance | 77%      |



