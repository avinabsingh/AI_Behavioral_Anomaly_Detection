import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="AI Behavioral Anomaly Detection",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🛡️ AI Behavioral Anomaly Detection")

st.sidebar.markdown("---")

st.sidebar.success("Dashboard Navigation")

st.sidebar.info("""
📌 Modules

• Home

• Risk Analysis

• Explainability

• Live Prediction
""")

st.sidebar.markdown("---")

st.sidebar.write("### Project Information")

st.sidebar.write("**Dataset:** Synthetic Login Events")

st.sidebar.write("**Models:**")

st.sidebar.write("- Random Forest")

st.sidebar.write("- XGBoost")

st.sidebar.write("- LSTM")

st.sidebar.markdown("---")

st.sidebar.write("Version 1.0")

st.title("AI Behavioral Anomaly Detection System")

st.markdown("---")

st.header("Project Overview")

st.write("""
This project detects abnormal user behavior using Machine Learning.

### Models Used
- Random Forest
- XGBoost
- LSTM

### Explainable AI
- SHAP
- LIME

### Features
- Behavioral Profiling
- Risk Scoring
- Anomaly Detection
- Explainable AI
""")

st.markdown("---")

st.header("📊 Dataset Statistics")

df = pd.read_csv("data/processed/features.csv")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Events", len(df))

with col2:
    st.metric("Normal Events", (df["label"] == 1).sum())

with col3:
    st.metric("Anomalies", (df["label"] == 0).sum())

st.markdown("---")

st.header("📈 Data Visualizations")

col1, col2 = st.columns(2)

# -----------------------------
# Pie Chart
# -----------------------------
with col1:

    label_counts = df["label"].value_counts()

    fig = px.pie(
        values=label_counts.values,
        names=["Normal", "Anomaly"],
        title="Normal vs Anomaly"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Bar Chart
# -----------------------------
with col2:

    attack_counts = df["anomaly_type"].value_counts()

    fig = px.bar(
        x=attack_counts.index,
        y=attack_counts.values,
        title="Attack Distribution"
    )

    fig.update_layout(
        xaxis_title="Attack Type",
        yaxis_title="Count"
    )

    st.plotly_chart(fig, use_container_width=True)



st.markdown("---")

st.header("🤖 Model Performance Comparison")

performance = pd.DataFrame({
    "Model": ["Random Forest", "XGBoost", "LSTM"],
    "Accuracy": [0.9895, 0.9905, 0.9000],
    "Precision": [0.9893, 0.9918, 0.9888],
    "Recall": [1.0000, 0.9985, 0.9072],
    "F1 Score": [0.9946, 0.9951, 0.9462],
    "ROC AUC": [0.9715, 0.9522, 0.8636]
})

st.dataframe(
    performance,
    use_container_width=True
)

fig = px.bar(
    performance,
    x="Model",
    y="Accuracy",
    color="Model",
    title="Model Accuracy Comparison"
)

st.plotly_chart(fig, use_container_width=True)

st.success("Dashboard Loaded Successfully!")

st.markdown("---")

st.caption(
    "AI Behavioral Anomaly Detection System | Developed using Streamlit, Scikit-learn, TensorFlow, XGBoost, SHAP, and LIME"
)