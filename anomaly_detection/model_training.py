from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
import os

def train_model(training_data):
    try:
        # Load the training data
        df = pd.read_csv(training_data)

        # Define the feature columns used during training
        feature_columns = ['EventID_5379', 'EventID_4798', 'EventID_4624', 'EventID_4672', 
                           'EventID_4907', 'EventID_4799', 'EventID_6416', 'EventID_4688', 
                           'EventID_4648', 'EventID_4634', 'EventID_5382', 'EventID_5058',
                           'EventID_5061', 'EventID_5059', 'EventID_4797', 'EventID_4616',
                           'EventID_4647', 'EventID_6281', 'EventID_5033', 'EventID_5024',
                           'EventID_4826', 'EventID_4696', 'EventID_4608', 'EventID_4902',
                           'EventID_1101', 'EventID_1100', 'EventID_4733', 'EventID_4717']

        # Ensure all necessary columns are present, and fill missing ones with default value 0
        for column in feature_columns:
            if column not in df.columns:
                df[column] = 0

        # Split data into training and testing sets
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

        # Extract feature values and apply robust scaling for handling outliers
        X_train = train_df[feature_columns].fillna(0).values
        scaler = RobustScaler()
        X_train_scaled = scaler.fit_transform(X_train)

        # Train Isolation Forest model with lower contamination
        isolation_forest = IsolationForest(n_estimators=500, contamination=0.005, random_state=42)
        isolation_forest.fit(X_train_scaled)

        # Train One-Class SVM model with a lower nu parameter
        one_class_svm = OneClassSVM(kernel='rbf', gamma='scale', nu=0.001)
        one_class_svm.fit(X_train_scaled)

        # Save the trained models and scaler
        joblib.dump(isolation_forest, '../anomaly_detection/isolation_forest_model.pkl')
        joblib.dump(one_class_svm, '../anomaly_detection/one_class_svm_model.pkl')
        joblib.dump(scaler, '../anomaly_detection/scaler.pkl')

        # Save feature columns for use during anomaly detection
        features_output_path = '../anomaly_detection/feature_columns.txt'
        with open(features_output_path, 'w') as f:
            for column in feature_columns:
                f.write(f"{column}\n")

        print("Models trained and saved.")

    except Exception as e:
        print(f"Error during model training: {e}")

if __name__ == "__main__":
    if not os.path.exists('../event_log_collector/security_logs.csv'):
        print("Error: Log file '../event_log_collector/security_logs.csv' not found.")
    else:
        train_model('../event_log_collector/security_logs.csv')
