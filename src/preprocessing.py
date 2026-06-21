import pandas as pd

def preprocess_data(df):

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    df.fillna(0, inplace=True)

    return df