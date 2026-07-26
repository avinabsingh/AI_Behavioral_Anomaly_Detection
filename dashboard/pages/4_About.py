import streamlit as st
from pathlib import Path

def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"

    if not css_path.exists():
        css_path = Path(__file__).parent.parent / "assets" / "style.css"

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(page_title="About", page_icon="ℹ")

st.title("ℹAbout This Project")

st.markdown("""
## AI Behavioral Anomaly Detection System

This project detects suspicious login behavior using Machine Learning and Explainable AI.

### Objectives

- Detect abnormal user login behavior
- Calculate risk scores
- Compare multiple ML models
- Explain predictions using SHAP & LIME
- Provide an interactive dashboard

---

## Technologies Used

### Programming
- Python

### Machine Learning
- Random Forest
- XGBoost
- LSTM

### Explainable AI
- SHAP
- LIME

### Dashboard
- Streamlit
- Plotly

### Libraries
- Pandas
- NumPy
- Scikit-learn
- TensorFlow
- Joblib

---

## Workflow

1. Generate Synthetic Login Data
2. Validate Data
3. Feature Engineering
4. Behavioral Profiling
5. Risk Scoring
6. Train ML Models
7. Explain Predictions
8. Visualize Results

---

## Project Features

Synthetic Cybersecurity Dataset

Behavioral Profiling

Risk Scoring

Random Forest Model

XGBoost Model

LSTM Model

SHAP Explainability

LIME Explainability

Live Prediction Dashboard

---

### Developed for AI Behavioral Anomaly Detection Hackathon
""")


st.markdown("---")

st.subheader("Download Reports")

with open("reports/explainability/lime_explanation.html", "rb") as f:
    st.download_button(
        "Download LIME Report",
        data=f,
        file_name="lime_explanation.html"
    )

with open("reports/explainability/shap_summary.png", "rb") as f:
    st.download_button(
        "Download SHAP Summary",
        data=f,
        file_name="shap_summary.png"
    )

with open("reports/explainability/shap_bar.png", "rb") as f:
    st.download_button(
        "Download SHAP Bar Plot",
        data=f,
        file_name="shap_bar.png"
    )