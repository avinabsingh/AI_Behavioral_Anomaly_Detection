import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Live Prediction", page_icon="🤖")

st.title("🤖 Live Anomaly Prediction")

st.write("Enter login details below and predict whether the login is Normal or Anomalous.")

# Load model
model = joblib.load("models/random_forest_model.pkl")

# Load dataset (used to get valid ranges/default values)
df = pd.read_csv("data/processed/features.csv")

st.markdown("---")

entity_id = st.number_input(
    "Entity ID",
    min_value=int(df["entity_id"].min()),
    max_value=int(df["entity_id"].max()),
    value=int(df["entity_id"].min())
)

entity_type = st.number_input(
    "Entity Type",
    value=int(df["entity_type"].iloc[0])
)

geo_location = st.number_input(
    "Geo Location",
    value=int(df["geo_location"].iloc[0])
)

resource_accessed = st.number_input(
    "Resource Accessed",
    value=int(df["resource_accessed"].iloc[0])
)

auth_method = st.number_input(
    "Authentication Method",
    value=int(df["auth_method"].iloc[0])
)

session_duration = st.number_input(
    "Session Duration",
    value=float(df["session_duration"].mean())
)

login_status = st.number_input(
    "Login Status",
    value=int(df["login_status"].iloc[0])
)

device_fingerprint = st.number_input(
    "Device Fingerprint",
    value=int(df["device_fingerprint"].iloc[0])
)

protocol = st.number_input(
    "Protocol",
    value=int(df["protocol"].iloc[0])
)

hour = st.number_input(
    "Hour",
    min_value=0,
    max_value=23,
    value=12
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=1
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=1
)

weekday = st.number_input(
    "Weekday",
    min_value=0,
    max_value=6,
    value=0
)

if st.button("Predict"):

    sample = pd.DataFrame([{
        "entity_id": entity_id,
        "entity_type": entity_type,
        "geo_location": geo_location,
        "resource_accessed": resource_accessed,
        "auth_method": auth_method,
        "session_duration": session_duration,
        "login_status": login_status,
        "device_fingerprint": device_fingerprint,
        "protocol": protocol,
        "hour": hour,
        "day": day,
        "month": month,
        "weekday": weekday
    }])

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0]

    st.markdown("---")

    if prediction == 1:
        st.success("✅ Prediction: Normal Login")
    else:
        st.error("🚨 Prediction: Anomaly Detected")

    st.write(f"**Confidence:** {max(probability) * 100:.2f}%")