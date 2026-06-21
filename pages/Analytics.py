import streamlit as st
import plotly.express as px

from src.utils import load_css
from src.security import check_login
from src.data_loader import load_data
from src.ui import page_header

st.set_page_config(layout="wide")

load_css()
check_login()

df = load_data()

page_header("📈 Analytics", "Customer churn insights and patterns")

# =========================
# PIE CHART
# =========================
st.markdown("### Customer Churn Distribution")

fig1 = px.pie(df, names="Churn", hole=0.6)

fig1.update_traces(
    marker=dict(line=dict(color="black", width=2)),
    textfont_size=16,
    textposition="inside",
    textinfo="percent+label"
)

fig1.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white",
    height=450,   # 🔥 slightly reduced
    margin=dict(t=60, b=30, l=30, r=30),
    legend=dict(font=dict(size=14))
)

st.plotly_chart(fig1, use_container_width=True)

st.divider()

# =========================
# BAR CHART
# =========================
st.markdown("### Contract Type vs Churn")

fig2 = px.histogram(
    df,
    x="Contract",
    color="Churn",
    barmode="group",
    text_auto=True
)

fig2.update_traces(
    marker_line_color="black",
    marker_line_width=2,
    textfont_size=14
)

fig2.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white",
    height=500,   # 🔥 slightly reduced
    margin=dict(t=60, b=40, l=40, r=40),
    xaxis=dict(tickfont=dict(size=14)),
    yaxis=dict(tickfont=dict(size=14)),
    legend=dict(font=dict(size=14))
)

st.plotly_chart(fig2, use_container_width=True)