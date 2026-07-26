import pandas as pd
import os

# Load data
events = pd.read_csv("data/synthetic/login_events.csv")
profiles = pd.read_csv("models/behavior_profiles.csv")

# Merge login events with user profiles
df = events.merge(
    profiles,
    on="entity_id",
    how="left"
)

risk_scores = []
reasons = []

for _, row in df.iterrows():

    score = 0
    reason = []

    # Country mismatch
    if row["geo_location"] != row["most_common_country"]:
        score += 30
        reason.append("Unusual Country")

    # Authentication mismatch
    if row["auth_method"] != row["most_common_auth"]:
        score += 15
        reason.append("Different Authentication")

    # Protocol mismatch
    if row["protocol"] != row["most_common_protocol"]:
        score += 10
        reason.append("Different Protocol")

    # Resource mismatch
    if row["resource_accessed"] != row["most_common_resource"]:
        score += 15
        reason.append("Different Resource")

    # Device mismatch
    if row["device_fingerprint"] != row["most_common_device"]:
        score += 25
        reason.append("Unknown Device")

    # Session duration anomaly
    upper_limit = (
        row["avg_session_duration"]
        + 2 * row["std_session_duration"]
    )

    if row["session_duration"] > upper_limit:
        score += 20
        reason.append("Long Session")

    risk_scores.append(score)

    if reason:
        reasons.append(", ".join(reason))
    else:
        reasons.append("Normal")

df["risk_score"] = risk_scores
df["risk_reason"] = reasons

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/risk_scored_events.csv",
    index=False
)

print(df[
    [
        "entity_id",
        "label",
        "anomaly_type",
        "risk_score",
        "risk_reason"
    ]
].head(20))


print("\nRisk Score Distribution")
print(df["risk_score"].value_counts().sort_index())

print("\nTop 20 Highest Risk Events")
print(
    df[
        [
            "entity_id",
            "label",
            "anomaly_type",
            "risk_score",
            "risk_reason"
        ]
    ]
    .sort_values("risk_score", ascending=False)
    .head(20)
)   

print(df[df["label"] == "Anomaly"].head(20))