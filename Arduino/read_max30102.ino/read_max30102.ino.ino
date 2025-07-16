#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"

MAX30105 particleSensor;

void setup() {
  Serial.begin(115200);
  while (!Serial);
  
  if (!particleSensor.begin(Wire, I2C_SPEED_STANDARD)) {
    Serial.println("MAX30102 not found. Please check wiring.");
    while (1);
  }

  particleSensor.setup(); // Default config
  particleSensor.setPulseAmplitudeRed(0x0A); // Low power mode
  particleSensor.setPulseAmplitudeIR(0x0A);
}

void loop() {
  long irValue = particleSensor.getIR();

  if (checkForBeat(irValue)) {
    float bpm = particleSensor.getHeartRate();
    float spo2 = particleSensor.getSpO2();
    
    Serial.print("Heart Rate (BPM): ");
    Serial.print(bpm);
    Serial.print("\tSpO2 (%): ");
    Serial.println(spo2);
  }

  delay(100);
}
