import streamlit as st
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import numpy as np

from src.utils import load_css
from src.security import check_login
from src.data_loader import load_data
from src.ui import page_header

load_css()
check_login()

df = load_data()
page_header("📊 Explainability Dashboard", "Model insights per customer")

# =========================
# LOAD MODEL + ENCODERS
# =========================
model = joblib.load("models/churn_model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

# =========================
# PREP DATA (IMPORTANT FIX)
# =========================
X_raw = df.drop(columns=["Churn", "customerID"], errors="ignore").copy()

# numeric conversion fix
if "TotalCharges" in X_raw.columns:
    X_raw["TotalCharges"] = pd.to_numeric(X_raw["TotalCharges"], errors="coerce")

X_raw.fillna(0, inplace=True)

# encode same as training
X = X_raw.copy()

for col, le in label_encoders.items():
    if col in X.columns:
        X[col] = X[col].astype(str).str.strip()
        X[col] = le.transform(X[col])

# =========================
# CUSTOMER SELECT
# =========================
st.markdown("## 🔍 Customer Analysis Panel")

index = st.slider("Select Customer Index", 0, len(X) - 1, 0)

customer = X.iloc[[index]]
customer_raw = X_raw.iloc[[index]]

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Raw Data")
    st.dataframe(customer_raw)

with col2:
    pred = model.predict(customer)[0]
    prob = model.predict_proba(customer)[0].max()

    if pred == 1:
        st.error(f"⚠️ High Churn Risk ({round(prob*100,2)}%)")
    else:
        st.success(f"✅ Likely to Stay ({round(prob*100,2)}%)")

# =========================
# FEATURE IMPORTANCE (SAFE)
# =========================
st.markdown("## 📊 Feature Importance")

if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    features = X.columns

    idx = np.argsort(importances)[::-1]

    fig, ax = plt.subplots()
    ax.bar(range(len(importances)), importances[idx])
    ax.set_xticks(range(len(importances)))
    ax.set_xticklabels(features[idx], rotation=90)
    ax.set_title("Feature Importance")

    st.pyplot(fig)
else:
    st.warning("No feature importance available for this model.")