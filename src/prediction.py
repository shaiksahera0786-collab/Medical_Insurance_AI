import joblib
import pandas as pd
import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
MODEL_PATH = os.path.join(BASE_DIR, "models", "insurance_model.pkl")

# Load trained model
model = joblib.load(MODEL_PATH)


def predict_insurance(age, sex, bmi, children, smoker, region):

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    prediction = model.predict(input_data)

    return round(float(prediction[0]), 2)