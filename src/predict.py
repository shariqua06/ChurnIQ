import joblib
import pandas as pd

model = joblib.load("models/churn_model.pkl")

def predict_churn(input_data):

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0].max()

    return prediction, round(probability * 100, 2)