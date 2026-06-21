import streamlit as st
from src.utils import load_css
from src.security import check_login
from src.data_loader import load_data
from src.ui import page_header

load_css()
check_login()

df = load_data()

page_header("📊 Customer Segmentation", "Group customers by behavior")

st.markdown("### Segment by Contract Type")

st.dataframe(df.groupby("Contract").size().reset_index(name="Count"))