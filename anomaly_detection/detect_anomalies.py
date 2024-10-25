import pandas as pd
import joblib
import os

def detect_anomalies(new_data):
    try:
        # Load the trained models and scaler
        if not os.path.exists('isolation_forest_model.pkl') or not os.path.exists('one_class_svm_model.pkl') or not os.path.exists('scaler.pkl'):
            print("Error: Required files ('isolation_forest_model.pkl', 'one_class_svm_model.pkl', or 'scaler.pkl') not found.")
            return
        
        isolation_forest_model = joblib.load('isolation_forest_model.pkl')
        one_class_svm_model = joblib.load('one_class_svm_model.pkl')
        scaler = joblib.load('scaler.pkl')

        # Load the feature columns
        if not os.path.exists('feature_columns.txt'):
            print("Error: Feature columns file 'feature_columns.txt' not found.")
            return

        with open('feature_columns.txt', 'r') as f:
            feature_columns = [line.strip() for line in f]

        # Load the new data to check for anomalies
        df = pd.read_csv(new_data)

        # Ensure the feature columns are present in the new data
        for column in feature_columns:
            if column not in df.columns:
                df[column] = 0

        # Extract the feature values and apply scaling
        X = df[feature_columns].fillna(0).values
        X_scaled = scaler.transform(X)

        # Predict anomalies using both models
        predictions_isolation_forest = isolation_forest_model.predict(X_scaled)
        predictions_one_class_svm = one_class_svm_model.predict(X_scaled)

        # Mark data points as anomalous if either model detects (-1 from either model) but assign different weights
        df['IsolationForest_Anomaly'] = predictions_isolation_forest
        df['OneClassSVM_Anomaly'] = predictions_one_class_svm

        # Weighted ensemble approach (give Isolation Forest higher weight)
        df['Final_Anomaly'] = ((df['IsolationForest_Anomaly'] == -1) | (df['OneClassSVM_Anomaly'] == -1)).astype(int)
        df['Weighted_Anomaly'] = ((df['IsolationForest_Anomaly'] == -1) * 2 + (df['OneClassSVM_Anomaly'] == -1)).astype(int)
        
        # Only consider anomalies if the weighted score is above a threshold
        anomalies = df[df['Weighted_Anomaly'] >= 2]

        # Save detected anomalies
        anomalies.to_csv('detected_anomalies_weighted.csv', index=False)
        print(f"Anomalies detected by weighted approach: {len(anomalies)}")
        print("Anomalies detected and saved to 'detected_anomalies_weighted.csv'")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if not os.path.exists('../event_log_collector/security_logs.csv'):
        print("Error: Log file '../event_log_collector/security_logs.csv' not found.")
    else:
        detect_anomalies('../event_log_collector/security_logs.csv')
