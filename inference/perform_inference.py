import pandas as pd
import pickle

def convert_to_numerical(df: pd.DataFrame):
    pass
    
def perform_inference():
    # Load the model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Load the test data
    df = pd.read_csv('test.csv')

    # df_test = convert_to_numerical(test_data)

    features = ['Age', 'Height', 'Weight', 'Veg_Consump', 'Water_Consump', 'Meal_Count',
       'Phys_Act', 'Time_E_Dev', 'Gender', 'H_Cal_Consump', 'Smoking',
       'Fam_Hist', 'H_Cal_Burn', 'Alcohol_Consump_Sometimes',
       'Alcohol_Consump_Frequently', 'Alcohol_Consump_Always',
       'Alcohol_Consump_no', 'Food_Between_Meals_Sometimes',
       'Food_Between_Meals_Frequently', 'Food_Between_Meals_no',
       'Food_Between_Meals_Always', 'Transport_Public_Transportation',
       'Transport_Motorbike', 'Transport_Bike', 'Transport_Automobile',
       'Transport_Walking']

    numerical_features = ['Age', 'Height', 'Weight', 'Veg_Consump', 'Water_Consump', 'Meal_Count', 'Phys_Act', 'Time_E_Dev']
    df_numerical = pd.DataFrame()
    df_numerical[numerical_features] = df[numerical_features]
    df_numerical['Gender'] = df['Gender'].map({"Female" : 0, "Male" : 1})
    binary_categorical_features = ['H_Cal_Consump', 'Smoking', 'Fam_Hist', 'H_Cal_Burn'] # Yes or no
    for feature in binary_categorical_features:
        df_numerical[feature] = df[feature].map({"no" : 0, "yes" : 1})
    multi_categorical_features = ['Alcohol_Consump', 'Food_Between_Meals', 'Transport']
    for feature in multi_categorical_features:
        values = sorted(list(set(df[feature])))
        for value in values:
            df_numerical[feature+"_"+value] = df[feature].map(lambda x: 1 if x==value else 0)


    # An extra step done for the validation set since it may not contain all the categories of a specific attribute due to its smaller size.
    for feature in features:
        if feature not in list(df_numerical.columns.array):
            df_numerical[feature] = 0

    df_numerical = df_numerical.reindex(sorted(df_numerical.columns), axis=1)
    features = sorted(features)
    

    x_test = df_numerical[features]
    # Make predictions
    preds = model.predict(x_test)

    # Save predictions to a text file
    with open('preds.txt', 'w') as f:
        for pred in preds:
            f.write(str(pred) + '\n')

if __name__ == '__main__':
    perform_inference()
