import pandas as pd

def extract_features(log_file):
    df = pd.read_csv(log_file)

    # Extract features such as count of each EventID
    event_counts = df['EventID'].value_counts().to_dict()
    features = {"EventID_" + str(k): v for k, v in event_counts.items()}

    return features

if __name__ == "__main__":
    # Extract features
    features = extract_features("../event_log_collector/security_logs.csv")
    print(features)

    # Convert features dictionary to a DataFrame and save to CSV
    features_df = pd.DataFrame([features])
    features_df.to_csv("../anomaly_detection/features.csv", index=False)
