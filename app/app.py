import streamlit as st
import pandas as pd

from src.prediction import predict_insurance
from src.dashboard import show_dashboard

from src.utils import (
    get_bmi_category,
    get_risk_level,
    get_health_recommendation
)

from src.charts import (
    plot_age_distribution,
    plot_bmi_distribution,
    plot_charges_distribution,
    plot_smoker_distribution,
    plot_region_distribution
)

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Medical Insurance AI",
    page_icon="🏥",
    layout="wide"
)

# ==========================================
# Load CSS
# ==========================================

with open("app/static/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/insurance.csv")

# ==========================================
# Sidebar
# ==========================================

st.sidebar.image(
    "https://img.icons8.com/color/96/hospital-3.png",
    width=90
)

st.sidebar.title("Medical Insurance AI")

st.sidebar.markdown("---")

st.sidebar.write("### 🤖 AI Model")
st.sidebar.success("Gradient Boosting Regressor")

st.sidebar.markdown("---")

st.sidebar.write("### 📊 Dataset")

st.sidebar.write(f"Records : {len(df)}")
st.sidebar.write(f"Features : {len(df.columns)-1}")

st.sidebar.markdown("---")

st.sidebar.info(
    """
This AI application predicts Medical Insurance Charges using Machine Learning.
"""
)

st.sidebar.markdown("---")

st.sidebar.success("Developed by Shaik Sahera")

# ==========================================
# Main Title
# ==========================================

st.title("🏥 Medical Insurance Cost Prediction")

st.write(
"""
Predict Medical Insurance Charges using Artificial Intelligence and Machine Learning.
"""
)

st.markdown("---")

# ==========================================
# Dashboard
# ==========================================

show_dashboard(df)

st.markdown("---")
# ==========================================
# Customer Information
# ==========================================

st.header("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0,
        step=0.1
    )

    children = st.selectbox(
        "Number of Children",
        [0,1,2,3,4,5]
    )

with col2:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    smoker = st.selectbox(
        "Smoker",
        ["No", "Yes"]
    )

    region = st.selectbox(
        "Region",
        [
            "northeast",
            "northwest",
            "southeast",
            "southwest"
        ]
    )

st.markdown("---")

# ==========================================
# Encode Inputs
# ==========================================

# Gender Encoding
sex = 1 if gender == "Male" else 0

# Smoker Encoding
smoker_value = 1 if smoker == "Yes" else 0

# Region Encoding
region_mapping = {
    "northeast": 0,
    "northwest": 1,
    "southeast": 2,
    "southwest": 3
}

region_value = region_mapping[region]

# ==========================================
# Prediction Button
# ==========================================

predict_button = st.button("🔍 Predict Insurance Charges")
# ==========================================
# Prediction
# ==========================================

if predict_button:

    prediction = predict_insurance(
        age=age,
        sex=sex,
        bmi=bmi,
        children=children,
        smoker=smoker_value,
        region=region_value
    )

    bmi_category = get_bmi_category(bmi)
    risk_level = get_risk_level(prediction)
    recommendations = get_health_recommendation(
        bmi,
        smoker_value
    )

    st.markdown("---")

    st.success("✅ Prediction Completed Successfully")

    st.subheader("💰 Predicted Insurance Charges")

    st.metric(
        label="Estimated Insurance Cost",
        value=f"₹ {prediction:,.2f}"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"⚖️ BMI Category : **{bmi_category}**")

    with col2:
        st.warning(f"📊 Risk Level : **{risk_level}**")

    st.markdown("---")

    st.subheader("💡 Health Recommendations")

    for recommendation in recommendations:
        st.write(recommendation)

    st.markdown("---")
    # ==========================================
# Dataset Visualizations
# ==========================================

st.header("📊 Dataset Analytics")

col1, col2 = st.columns(2)

with col1:
    st.pyplot(plot_age_distribution(df))

with col2:
    st.pyplot(plot_bmi_distribution(df))

col3, col4 = st.columns(2)

with col3:
    st.pyplot(plot_charges_distribution(df))

with col4:
    st.pyplot(plot_smoker_distribution(df))

st.pyplot(plot_region_distribution(df))

st.markdown("---")

# ==========================================
# Dataset Preview
# ==========================================

st.header("📋 Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

# ==========================================
# Footer
# ==========================================

st.markdown(
    """
    <div style='text-align:center; padding:20px;'>
        <h4>🏥 Medical Insurance Cost Prediction using Machine Learning</h4>
        <p>Model : <b>Gradient Boosting Regressor</b></p>
        <p>Developed by <b>Shaik Sahera</b></p>
        <p>© 2026 All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True
)