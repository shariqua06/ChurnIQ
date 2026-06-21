import pandas as pd

def load_data():
    df = pd.read_csv("data/churn.csv")

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

    return df