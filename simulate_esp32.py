# simulate_esp32.py
import serial
import time
import json

# Change to same port as your serial_listener.py (use loopback if needed)
SERIAL_PORT = 'COM3'  # Must match your actual COM port
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)

print("Sending fake sensor data to simulate ESP32...\n")

test_data = [
    {"HeartRate": 96, "SpO2": 98, "Temperature": 36.7, "ECG": 511},
    {"HeartRate": 101, "SpO2": 94, "Temperature": 38.5, "ECG": 530},
    {"HeartRate": 89, "SpO2": 90, "Temperature": 36.1, "ECG": 505}
]

for sample in test_data:
    ser.write((json.dumps(sample) + "\n").encode())
    print(f"Sent: {sample}")
    time.sleep(2)
