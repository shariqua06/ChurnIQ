import streamlit as st

from src.utils import load_css
from src.security import check_login
from src.predict import predict_churn

load_css()
check_login()

st.title("🔮 Customer Churn Prediction")

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        [0, 1]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        [0, 1]
    )

    dependents = st.selectbox(
        "Dependents",
        [0, 1]
    )

    tenure = st.number_input(
        "Tenure",
        0,
        100,
        12
    )

with col2:

    monthly_charges = st.number_input(
        "Monthly Charges",
        0.0,
        1000.0,
        70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        0.0,
        100000.0,
        1000.0
    )

if st.button("Predict Churn Risk"):

    customer_data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": 1,
        "MultipleLines": 0,
        "InternetService": 1,
        "OnlineSecurity": 0,
        "OnlineBackup": 0,
        "DeviceProtection": 0,
        "TechSupport": 0,
        "StreamingTV": 0,
        "StreamingMovies": 0,
        "Contract": 0,
        "PaperlessBilling": 1,
        "PaymentMethod": 0,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    prediction, probability = predict_churn(
        customer_data
    )

    st.divider()

    if prediction == 1:

        st.error(
            f"⚠️ High Churn Risk ({probability}%)"
        )

        st.warning("""
Recommended Actions

• Offer loyalty discount

• Upgrade contract plan

• Provide retention benefits
""")

    else:

        st.success(
            f"✅ Customer Likely to Stay ({probability}%)"
        )