import streamlit as st
import pandas as pd
import joblib

from pathlib import Path

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Live Prediction",
    page_icon="",
    layout="wide"
)

# ---------------------------------------------------
# Load CSS
# ---------------------------------------------------

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

# ---------------------------------------------------
# Hero Banner
# ---------------------------------------------------

st.markdown("""
<div class="hero-banner">

<h1 class="hero-title">
Live Anomaly Prediction
</h1>

<p style="font-size:18px;">

Predict suspicious login behaviour using
Machine Learning, Behavioral Profiling,
Risk Scoring and Explainable AI.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

model = joblib.load(
    "models/random_forest_model.pkl"
)

label_encoders = joblib.load(
    "models/label_encoders.pkl"
)

df = pd.read_csv(
    "data/processed/features.csv"
)

# ---------------------------------------------------
# Select a Default Normal Login
# ---------------------------------------------------

normal_label = list(label_encoders["label"].classes_).index("Normal")

default_row = df[
    df["label"] == normal_label
].iloc[0]

# ---------------------------------------------------
# Decode Default Values
# ---------------------------------------------------

default_entity_type = label_encoders["entity_type"].inverse_transform(
    [default_row["entity_type"]]
)[0]

default_country = label_encoders["geo_location"].inverse_transform(
    [default_row["geo_location"]]
)[0]

default_resource = label_encoders["resource_accessed"].inverse_transform(
    [default_row["resource_accessed"]]
)[0]

default_auth = label_encoders["auth_method"].inverse_transform(
    [default_row["auth_method"]]
)[0]

default_login_status = label_encoders["login_status"].inverse_transform(
    [default_row["login_status"]]
)[0]

default_protocol = label_encoders["protocol"].inverse_transform(
    [default_row["protocol"]]
)[0]

default_device = label_encoders["device_fingerprint"].inverse_transform(
    [default_row["device_fingerprint"]]
)[0]

st.markdown("---")

# ---------------------------------------------------
# Layout
# ---------------------------------------------------

left, right = st.columns(2)

# ---------------------------------------------------
# Input Form
# ---------------------------------------------------

with left:

    st.markdown("""
    <div class="section-title">
    User Information
    </div>
    """, unsafe_allow_html=True)

    entity_id = st.number_input(
        "Entity ID",
        min_value=int(df["entity_id"].min()),
        max_value=int(df["entity_id"].max()),
        value=int(default_row["entity_id"])
    )

    entity_type = st.selectbox(
        "Entity Type",
        label_encoders["entity_type"].classes_,
        index=list(label_encoders["entity_type"].classes_).index(default_entity_type)
    )

    geo_location = st.selectbox(
        "Geo Location",
        label_encoders["geo_location"].classes_,
        index=list(label_encoders["geo_location"].classes_).index(default_country)
    )

    auth_method = st.selectbox(
        "Authentication Method",
        label_encoders["auth_method"].classes_,
        index=list(label_encoders["auth_method"].classes_).index(default_auth)
    )

    login_status = st.selectbox(
        "Login Status",
        label_encoders["login_status"].classes_,
        index=list(label_encoders["login_status"].classes_).index(default_login_status)
    )

with right:

    st.markdown("""
    <div class="section-title">
    ⚙ Session Information
    </div>
    """, unsafe_allow_html=True)

    resource_accessed = st.selectbox(
        "Resource Accessed",
        label_encoders["resource_accessed"].classes_,
        index=list(label_encoders["resource_accessed"].classes_).index(default_resource)
    )

    protocol = st.selectbox(
        "Protocol",
        label_encoders["protocol"].classes_,
        index=list(label_encoders["protocol"].classes_).index(default_protocol)
    )

    device_fingerprint = st.selectbox(
        "Device Fingerprint",
        label_encoders["device_fingerprint"].classes_,
        index=list(label_encoders["device_fingerprint"].classes_).index(default_device)
    )

    session_duration = st.slider(
        "Session Duration (seconds)",
        min_value=30,
        max_value=15000,
        value=int(default_row["session_duration"]),
        step=10
    )

    hour = st.slider(
        "Login Hour",
        0,
        23,
        int(default_row["hour"])
    )

    day = st.slider(
        "Day",
        1,
        31,
        int(default_row["day"])
    )

    month = st.slider(
        "Month",
        1,
        12,
        int(default_row["month"])
    )

    weekday = st.slider(
        "Weekday",
        0,
        6,
        int(default_row["weekday"])
    )

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🔍 Predict Login",
    use_container_width=True
)

if predict:

    # ---------------------------------------------------
    # Create Sample
    # ---------------------------------------------------

    sample = pd.DataFrame([{
        "entity_id": entity_id,
        "entity_type": label_encoders["entity_type"].transform([entity_type])[0],
        "geo_location": label_encoders["geo_location"].transform([geo_location])[0],
        "resource_accessed": label_encoders["resource_accessed"].transform([resource_accessed])[0],
        "auth_method": label_encoders["auth_method"].transform([auth_method])[0],
        "session_duration": session_duration,
        "login_status": label_encoders["login_status"].transform([login_status])[0],
        "device_fingerprint": label_encoders["device_fingerprint"].transform([device_fingerprint])[0],
        "protocol": label_encoders["protocol"].transform([protocol])[0],
        "hour": hour,
        "day": day,
        "month": month,
        "weekday": weekday
    }])

    # ---------------------------------------------------
    # Prediction
    # ---------------------------------------------------

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0]
    confidence = float(max(probability))

    st.markdown("---")

    # ---------------------------------------------------
    # Prediction Card
    # ---------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        if prediction == 1:
            st.success("Normal Login")
        else:
            st.error("Anomaly Detected")

    with col2:

        st.metric(
            "Confidence",
            f"{confidence*100:.2f}%"
        )

    with col3:

        if confidence >= 0.95:
            risk = "🔴 Critical"
        elif confidence >= 0.85:
            risk = "🟠 High"
        elif confidence >= 0.70:
            risk = "🟡 Medium"
        else:
            risk = "🟢 Low"

        st.metric("Risk Level", risk)

    st.progress(confidence)

    # ---------------------------------------------------
    # AI Explanation
    # ---------------------------------------------------

    st.markdown("## AI Explanation")

    reasons = []

    if session_duration > 5000:
        reasons.append(
            "Long session duration compared to normal user behaviour."
        )

    if login_status == "Failed":
        reasons.append(
            "Failed authentication attempt detected."
        )

    if hour < 6 or hour > 22:
        reasons.append(
            "Login occurred outside normal working hours."
        )

    if protocol.upper() == "FTP":
        reasons.append(
            "FTP protocol is less secure than encrypted protocols."
        )

    if resource_accessed.lower() in [
        "admindashboard",
        "adminpanel",
        "database",
        "sensitivedatabase",
        "payroll"
    ]:
        reasons.append(
            "High privilege resource was accessed."
        )

    if auth_method.lower() == "password":
        reasons.append(
            "Password authentication is less secure than MFA."
        )

    if prediction == 1:

        st.success(
            "The login matches expected behavioural patterns."
        )

        st.write("Login behaviour is consistent.")

        st.write("Authentication method appears normal.")

        st.write("No unusual activity detected.")

        st.write("Risk score is within acceptable limits.")

    else:

        st.error(
            "The AI model identified suspicious behavioural characteristics."
        )

        if len(reasons) == 0:

            st.write(
                "The model detected abnormal feature combinations that differ from historical login behaviour."
            )

        else:

            for reason in reasons:
                st.write("• " + reason)

    # ---------------------------------------------------
    # Recommendation
    # ---------------------------------------------------

    st.markdown("## Security Recommendation")

    if prediction == 1:

        st.info(
            """
Continue monitoring.

No immediate action is required because the login appears legitimate.
"""
        )

    else:

        st.warning(
            """
Recommended Actions

• Verify user identity

• Review login history

• Check IP reputation

• Review accessed resources

• Consider forcing MFA

• Monitor future sessions
"""
        )

        # ---------------------------------------------------
    # Input Summary
    # ---------------------------------------------------

    st.markdown("---")
    st.markdown("## Login Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Entity ID",
            "Entity Type",
            "Geo Location",
            "Authentication",
            "Resource Accessed",
            "Session Duration",
            "Login Status",
            "Protocol",
            "Hour",
            "Day",
            "Month",
            "Weekday"
        ],
        "Value": [
            entity_id,
            entity_type,
            geo_location,
            auth_method,
            resource_accessed,
            session_duration,
            login_status,
            protocol,
            hour,
            day,
            month,
            weekday
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    # ---------------------------------------------------
    # Feature Risk Analysis
    # ---------------------------------------------------

    st.markdown("## Feature Risk Analysis")

    feature_scores = {
        "Session Duration": 0,
        "Authentication": 0,
        "Protocol": 0,
        "Login Time": 0,
        "Resource": 0
    }

    if session_duration > 5000:
        feature_scores["Session Duration"] = 5
    elif session_duration > 2500:
        feature_scores["Session Duration"] = 3
    else:
        feature_scores["Session Duration"] = 1

    if auth_method.lower() == "password":
        feature_scores["Authentication"] = 4
    else:
        feature_scores["Authentication"] = 1

    if protocol.upper() == "FTP":
        feature_scores["Protocol"] = 5
    elif protocol.upper() == "HTTP":
        feature_scores["Protocol"] = 3
    else:
        feature_scores["Protocol"] = 1

    if hour < 6 or hour > 22:
        feature_scores["Login Time"] = 5
    else:
        feature_scores["Login Time"] = 1

    if resource_accessed.lower() in [
        "database",
        "admindashboard",
        "adminpanel",
        "sensitivedatabase",
        "payroll"
    ]:
        feature_scores["Resource"] = 5
    else:
        feature_scores["Resource"] = 1

    chart = pd.DataFrame(
        feature_scores.items(),
        columns=["Feature", "Risk Score"]
    )

    st.bar_chart(
        chart.set_index("Feature")
    )

    # ---------------------------------------------------
    # Top Factors
    # ---------------------------------------------------

    st.markdown("## 🔍 Top Influencing Factors")

    sorted_scores = sorted(
        feature_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for feature, score in sorted_scores:

        if score >= 4:
            emoji = "🔴"

        elif score == 3:
            emoji = "🟠"

        else:
            emoji = "🟢"

        st.write(f"{emoji} **{feature}** : Risk Score {score}/5")

    # ---------------------------------------------------
    # Footer
    # ---------------------------------------------------

    st.markdown("---")

    st.caption(
        "Developed using Random Forest • Behavioral Profiling • Risk Scoring • Explainable AI • Streamlit Dashboard"
    )