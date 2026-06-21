import pandas as pd
from src.config import DATA_PATH

def load_data():
    df = pd.read_csv(DATA_PATH)

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    return df