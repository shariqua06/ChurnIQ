import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "churn_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_churn(input_data):

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0].max()

    return prediction, round(probability * 100, 2)