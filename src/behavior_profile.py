import pandas as pd
import os

# Load synthetic login data
df = pd.read_csv("data/synthetic/login_events.csv")

# Use only normal behavior to learn the baseline
normal_df = df[df["label"] == "Normal"]

profiles = []

for user_id, group in normal_df.groupby("entity_id"):

    profile = {
        "entity_id": user_id,

        "most_common_country":
            group["geo_location"].mode()[0],

        "most_common_auth":
            group["auth_method"].mode()[0],

        "most_common_protocol":
            group["protocol"].mode()[0],

        "most_common_resource":
            group["resource_accessed"].mode()[0],

        "most_common_device":
            group["device_fingerprint"].mode()[0],

        "avg_session_duration":
            round(group["session_duration"].mean(), 2),

        "std_session_duration":
            round(group["session_duration"].std(), 2),

        "avg_login_hour":
            pd.to_datetime(group["timestamp"]).dt.hour.mean()
    }

    profiles.append(profile)

profiles = pd.DataFrame(profiles)

os.makedirs("models", exist_ok=True)

profiles.to_csv(
    "models/behavior_profiles.csv",
    index=False
)

print(profiles.head())

print("\nProfiles Created:", len(profiles))