IoT Health Monitor using ESP32 + ML

This project is a smart health monitoring system that uses the ESP32 microcontroller to collect real-time health data, stores it, and uses Machine Learning to predict health conditions like Fever, Hypoxia, and general Unwellness.

---

## 📦 Features

- Collects data from sensors:
  - **MAX30102** – Heart Rate & SpO₂
  - **DS18B20** – Body Temperature
  - **AD8232** – ECG Monitoring
- Sends sensor data to laptop via **Serial**
- Uses **Random Forest Classifier** to predict health condition
- Logs real-time sensor values and predictions to CSV
- Can later be extended with **Blynk, OLED Display, or emergency alerts**

---

## 🛠 Folder Structure

IoT Health Monitor/
│
├── Arduino/
│ ├── read_ad8232.ino
│ ├── read_ds18b20.ino
│ ├── read_max30102.ino
│ └── read_all_combined.ino
│
├── ML/
│ ├── health_data.csv ← Sample training data
│ ├── health_model.pkl ← Trained model (Decision Tree)
│ ├── health_rf_model.pkl ← Trained model (Random Forest)
│ ├── health_model_training.ipynb ← Jupyter Notebook to train model
│ ├── train_health_model.py ← Train model using script
│ └── log_to_csv.py ← Save real-time data to CSV
│
├── simulate_esp32.py ← Sends fake serial data (for testing)
├── serial_listener.py ← Receives real or fake serial data & predicts
├── health_predictor.py ← Model loading & prediction utility
└── requirements.txt ← Python dependencies


---

## 🚀 Getting Started

### 1. Setup Python environment

```bash
pip install -r ML/requirements.txt

2. Train your model (if needed)
Run the notebook ML/health_model_training.ipynb or script:

bash
Copy
Edit
python ML/train_health_model.py

3. Simulate data (without ESP32)
python simulate_esp32.py

Or use:

bash
Copy
Edit
python serial_listener.py
for real data via USB/Serial.

Hardware Components

- ESP32 microcontroller
- MAX30102 (Heart Rate + SpO₂)
- DS18B20 (Temperature sensor)
- AD8232 (ECG sensor)
- Jumper wires, breadboard
- OLED display (optional)
- Power supply or USB cable


You can clone, fork, or contribute to this project using GitHub:
git clone https://github.com/MrStrange7/iot-health-monitor.git

This project is licensed under the [MIT License](LICENSE).

