<h1>Windows Event Log + ART Detection</h1>

**Overview**
Windows Event Log + ART Detection is an advanced project that leverages machine learning to detect anomalies in Windows event logs, combining the power of Windows event monitoring with the Atomic Red Team (ART) techniques to emulate threat behaviors. This project aims to provide a comprehensive solution for analyzing Windows system activities and identifying potential threats through anomaly detection models, specifically tailored for cybersecurity enthusiasts and professionals.

<h3>Key Features</h3>

- **Event Log Collection**: Collects and parses Windows Event Logs, focusing on security-relevant events.
- **Atomic Red Team Integration**: Uses Atomic Red Team techniques to simulate real-world attacks and generate data for training the anomaly detection models.
- **Anomaly Detection**: Implements machine learning models like Isolation Forest and One-Class SVM to detect suspicious patterns or outlier events.
- **Feature Extraction and Engineering**: Extracts meaningful features from raw event logs, including event counts, temporal aggregations, and derived metrics to improve anomaly detection.
- **Real-World Simulation**: Provides a robust simulation environment to validate detection models with realistic attack scenarios.
- **Adaptive Ensemble Approach**: Utilizes multiple detection models in combination to enhance detection accuracy while reducing false positives.

<h3>Getting Started</h3>

**Prerequisites**
- **Python 3.8+**: Ensure Python is installed on your machine.
- **PowerShell**: PowerShell for executing Atomic Red Team scripts.
- **Dependencies**: Install the required Python libraries using:

_"pip install -r requirements.txt"_

**Installation and Usage**
**Clone the Repository**:

_"git clone https://github.com/your-username/windows-event-log-art-detection.git"_
_"cd windows-event-log-art-detection"_

**Run the Feature Extraction:**

_"python utils/feature_extraction.py"_

**Train Anomaly Detection Models:**

_"python anomaly_detection/train_model.py"_

**Detect Anomalies:**

_"python anomaly_detection/detect_anomalies.py"_

<h3>Technologies Used</h3>

**Python**: Main language for processing, model training, and anomaly detection.
**Scikit-Learn**: Machine learning library used for training and evaluating models.
**PowerShell**: Used for Atomic Red Team simulations and Windows event log collection.

<h3>Challenges and Future Work</h3>

**Parameter Tuning**: Finding the right balance between sensitivity and specificity in the detection models.
**Feature Enhancement**: Exploring new features to improve anomaly detection accuracy.
**Additional Models**: Adding more models like Autoencoders or Elliptic Envelope to diversify the detection techniques.
**Integration with ELK Stack**: Visualizing detected anomalies using Elasticsearch, Logstash, and Kibana.

**Contributing**
Contributions are welcome! Feel free to fork this repository and submit pull requests for new features, bug fixes, or improvements.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.
