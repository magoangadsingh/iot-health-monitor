import serial
import time
import joblib
import pandas as pd
from health_predictor import predict_condition

# === CONFIGURATION ===
SERIAL_PORT = "COM3"        # 🛠️ Replace with your actual ESP32 port (like "COM4" or "COM5")
BAUD_RATE = 9600            # Match the baud rate in your Arduino sketch
MODEL_PATH = "ML/health_model.pkl"


# === LOAD THE MODEL ===
rf_model = joblib.load(MODEL_PATH)

def parse_sensor_data(line):
    try:
        parts = line.strip().split(',')
        if len(parts) != 4:
            raise ValueError("Expected 4 values")
        hr = float(parts[0])
        spo2 = float(parts[1])
        temp = float(parts[2])
        ecg = float(parts[3])
        return {
            "HeartRate": hr,
            "SpO2": spo2,
            "Temperature": temp,
            "ECG": ecg
        }
    except Exception as e:
        print(f"[Parse Error] {e} → Raw line: {line}")
        return None

def main():
    print("🔌 Listening for data from ESP32...\n")
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
        time.sleep(2)  # Wait for serial connection
    except Exception as e:
        print(f"❌ Could not open serial port {SERIAL_PORT}: {e}")
        return

    while True:
        try:
            if ser.in_waiting:
                line = ser.readline().decode("utf-8").strip()
                data = parse_sensor_data(line)
                if data:
                    # Wrap data in DataFrame with correct column names
                    input_df = pd.DataFrame([data])
                    prediction = rf_model.predict(input_df)[0]

                    # Decode label (reverse map if needed)
                    label_map = {0: "Healthy", 1: "Fever", 2: "Hypoxia", 3: "Unwell"}
                    condition = label_map.get(prediction, "Unknown")

                    print(f"📟 HR={data['HeartRate']}, SpO₂={data['SpO2']}, Temp={data['Temperature']}, ECG={data['ECG']} → Condition: {condition}")
        except KeyboardInterrupt:
            print("\n🛑 Stopped by user.")
            break
        except Exception as e:
            print(f"[Runtime Error] {e}")

if __name__ == "__main__":
    main()
