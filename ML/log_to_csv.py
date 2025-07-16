import serial
import csv
from datetime import datetime

ser = serial.Serial('COM3', 115200)  # Change COM port if needed
filename = f"sensor_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "HeartRate", "SpO2", "Temperature", "ECG"])
    
    while True:
        line = ser.readline().decode('utf-8').strip()
        parts = line.split(',')
        if len(parts) == 4:
            writer.writerow([datetime.now().strftime("%H:%M:%S")] + parts)
            print("Logged:", parts)
