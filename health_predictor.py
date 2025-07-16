# health_predictor.py
import joblib
import numpy as np

# Load trained model from the 'ML' subfolder
model = joblib.load("ML/health_model.pkl")

# Function to predict condition
def predict_condition(heartrate, spo2, temp, ecg):
    data = np.array([[heartrate, spo2, temp, ecg]])
    pred = model.predict(data)[0]

    labels = {0: "Healthy", 1: "Fever", 2: "Hypoxia", 3: "Unwell"}
    return labels.get(pred, "Unknown")
