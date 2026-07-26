import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# Constants
# -----------------------------

COUNTRIES = [
    "India",
    "USA",
    "Germany",
    "Japan",
    "Singapore"
]

AUTH_METHODS = [
    "Password",
    "Token",
    "Biometric",
    "Certificate"
]

PROTOCOLS = [
    "HTTP",
    "HTTPS",
    "SSH",
    "FTP"
]

RESOURCES = [
    "Email",
    "HR",
    "Finance",
    "Payroll",
    "CRM",
    "Database",
    "SourceCode",
    "CloudServer"
]

ENTITY_TYPES = [
    "User",
    "Service",
    "Device"
]

LOGIN_STATUS = [
    "Success",
    "Failed"
]

COMMANDS = [
    "login",
    "open_file",
    "read_database",
    "download_report",
    "logout",
    "update_record",
    "query_data"
]

IP_RANGES = {
    "India": "103.25.",
    "USA": "192.168.",
    "Germany": "145.10.",
    "Japan": "172.20.",
    "Singapore": "10.50."
}

ANOMALY_TYPES = [
    "Brute Force",
    "Impossible Travel",
    "Credential Stuffing",
    "Device Spoofing",
    "Lateral Movement",
    "Data Exfiltration"
]

OTHER_COUNTRIES = [
    "Russia",
    "China",
    "Brazil",
    "France",
    "Australia"
]

def generate_users(num_users=100):

    users = []

    for i in range(1, num_users + 1):

        user = {
            "entity_id": f"U{i:03}",
            "entity_type": random.choice(ENTITY_TYPES),
            "home_country": random.choice(COUNTRIES),
            "preferred_auth": random.choice(AUTH_METHODS),
            "preferred_protocol": random.choice(PROTOCOLS),
            "preferred_resource": random.choice(RESOURCES),
            "device_fingerprint": fake.uuid4(),
            "work_start": random.randint(8, 10),
            "work_end": random.randint(17, 20)
        }

        users.append(user)

    return pd.DataFrame(users)

def generate_login_events(users_df, num_events=10000):

    events = []

    start_date = datetime(2026, 1, 1)

    for _ in range(num_events):

        user = users_df.sample(1).iloc[0]

        hour = int(
            random.gauss(
                (user["work_start"] + user["work_end"]) / 2,
                2
            )
        )

        hour = max(0, min(23, hour))

        timestamp = start_date + timedelta(
            days=random.randint(0, 180),
            hours=hour,
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        )

        country = user["home_country"]

        ip = (
            IP_RANGES[country]
            + str(random.randint(0, 255))
            + "."
            + str(random.randint(1, 254))
        )

        command_sequence = " -> ".join(
            random.sample(COMMANDS, random.randint(3, 5))
        )

        # -----------------------------
        # Natural variations
        # -----------------------------

        # Resource (90% preferred, 10% different)
        resource = user["preferred_resource"]
        if random.random() < 0.10:
            resource = random.choice(RESOURCES)

        # Authentication (95% preferred)
        auth = user["preferred_auth"]
        if random.random() < 0.05:
            auth = random.choice(AUTH_METHODS)

        # Protocol (92% preferred)
        protocol = user["preferred_protocol"]
        if random.random() < 0.08:
            protocol = random.choice(PROTOCOLS)

        # Session duration
        session = max(
            30,
            int(random.gauss(900, 300))
        )

        event = {

            "entity_id": user["entity_id"],

            "entity_type": user["entity_type"],

            "timestamp": timestamp,

            "source_ip": ip,

            "geo_location": country,

            "resource_accessed": resource,

            "auth_method": auth,

            "session_duration": session,

            "login_status": random.choices(
                LOGIN_STATUS,
                weights=[95, 5]
            )[0],

            "command_sequence": command_sequence,

            "device_fingerprint": user["device_fingerprint"],

            "protocol": protocol,

            "label": "Normal",

            "anomaly_type": "Normal"

        }

        events.append(event)

    return pd.DataFrame(events)

def inject_anomalies(events_df, anomaly_ratio=0.03):

    events = events_df.copy()

    total_rows = len(events)

    anomaly_count = int(total_rows * anomaly_ratio)

    anomaly_indices = random.sample(range(total_rows), anomaly_count)

    for idx in anomaly_indices:

        attack = random.choice(ANOMALY_TYPES)

        events.loc[idx, "label"] = "Anomaly"

        events.loc[idx, "anomaly_type"] = attack

        if attack == "Brute Force":

            events.loc[idx, "login_status"] = "Failed"
            events.loc[idx, "session_duration"] = random.randint(5, 20)
            events.loc[idx, "auth_method"] = "Password"

        elif attack == "Impossible Travel":

            events.loc[idx, "geo_location"] = random.choice(OTHER_COUNTRIES)

            events.loc[idx, "source_ip"] = (
                f"{random.randint(20,220)}."
                f"{random.randint(0,255)}."
                f"{random.randint(0,255)}."
                f"{random.randint(1,254)}"
            )

            events.loc[idx, "device_fingerprint"] = fake.uuid4()
            events.loc[idx, "timestamp"] = (
                pd.to_datetime(events.loc[idx, "timestamp"])
                .replace(hour=random.choice([1, 2, 3, 4, 23]))
            )

        elif attack == "Credential Stuffing":

            events.loc[idx, "login_status"] = "Failed"
            events.loc[idx, "auth_method"] = "Password"
            events.loc[idx, "session_duration"] = random.randint(5, 30)

        elif attack == "Device Spoofing":

            events.loc[idx, "device_fingerprint"] = fake.uuid4()
            events.loc[idx, "protocol"] = "SSH"
            events.loc[idx, "timestamp"] = (
            pd.to_datetime(events.loc[idx, "timestamp"])
            .replace(hour=random.choice([0, 1, 2, 3]))
)

        elif attack == "Lateral Movement":

            events.loc[idx, "resource_accessed"] = "AdminPanel"
            events.loc[idx, "protocol"] = "SSH"
            events.loc[idx, "session_duration"] = random.randint(1800, 3600)

        elif attack == "Data Exfiltration":

            events.loc[idx, "session_duration"] = random.randint(9000, 15000)
            events.loc[idx, "resource_accessed"] = "SensitiveDatabase"
            events.loc[idx, "protocol"] = "FTP"

    return events

if __name__ == "__main__":

    users = generate_users(100)

    users.to_csv(
        "data/synthetic/users.csv",
        index=False
    )

    login_events = generate_login_events(
        users,
        num_events=10000
    )

    login_events = inject_anomalies(
        login_events,
        anomaly_ratio=0.03
    )

    login_events.to_csv(
        "data/synthetic/login_events.csv",
        index=False
    )

    print(users.head())

    print()

    print(login_events.head())

    print()

    print("Users Generated :", len(users))

    print("Login Events Generated :", len(login_events))

    print("\nLabel Distribution")
    print(login_events["label"].value_counts())

    print("\nAttack Distribution")
    print(login_events["anomaly_type"].value_counts())