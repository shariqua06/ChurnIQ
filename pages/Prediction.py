import streamlit as st

from src.utils import load_css
from src.security import check_login
from src.predict import predict_churn

load_css()

# CSS override for neat white boxes, black text, and no extra black box
st.markdown("""
<style>
/* Remove nested borders/backgrounds */
div[data-baseweb="input"] div,
div[data-baseweb="select"] div {
    background: none !important;
    border: none !important;
}

/* Clean single neat white box */
div[data-baseweb="input"],
div[data-baseweb="select"] {
    background-color: #ffffff !important;
    border: 1px solid #cccccc !important;
    border-radius: 6px !important;
    padding: 6px !important;
}

/* Text inside inputs */
div[data-baseweb="input"] input {
    color: #000000 !important;
    font-size: 14px !important;
}

/* Selected option container */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: none !important;   /* remove extra black box */
    box-shadow: none !important;
    padding: 2px 6px !important;
}

/* Selected option text */
div[data-baseweb="select"] span {
    color: #000000 !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

/* Dropdown menu options */
ul[role="listbox"] {
    background-color: #ffffff !important;
    border: 1px solid #cccccc !important;
    border-radius: 6px !important;
}
ul[role="listbox"] li {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-size: 14px !important;
}
ul[role="listbox"] li:hover {
    background-color: #f0f0f0 !important;
    color: #000000 !important;
}
ul[role="listbox"] li[aria-selected="true"] {
    background-color: #e0e0e0 !important;
    color: #000000 !important;
}

/* Prevent yellow highlight or black box on focus */
div[data-baseweb="input"]:focus-within,
div[data-baseweb="select"]:focus-within {
    box-shadow: none !important;
    outline: none !important;   /* remove focus outline */
    border: 1px solid #666666 !important;
}
</style>
""", unsafe_allow_html=True)

check_login()

st.title("🔮 Customer Churn Prediction Dashboard")

st.markdown("### Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", [0, 1])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", [0, 1])
    dependents = st.selectbox("Dependents", [0, 1])
    tenure = st.number_input("Tenure", 0, 100, 12)

with col2:
    monthly = st.number_input("Monthly Charges", 0.0, 1000.0, 70.0)
    total = st.number_input("Total Charges", 0.0, 100000.0, 1000.0)

st.markdown("---")

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
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    pred, prob = predict_churn(customer_data)

    st.markdown("## Result")

    if pred == 1:
        st.error(f"⚠️ High Churn Risk ({prob}%)")
        st.warning("Offer discount / retention plan / upgrade contract")
    else:
        st.success(f"✅ Likely to Stay ({prob}%)")
        st.info("Customer is stable, maintain good service and engagement")