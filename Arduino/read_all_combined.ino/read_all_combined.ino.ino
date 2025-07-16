#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"
#include <OneWire.h>
#include <DallasTemperature.h>

MAX30105 particleSensor;
OneWire oneWire(4); // GPIO 4 for DS18B20
DallasTemperature tempSensor(&oneWire);
const int ecgPin = 34;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  // MAX30102
  if (!particleSensor.begin(Wire, I2C_SPEED_STANDARD)) {
    Serial.println("MAX30102 not found");
    while (1);
  }
  particleSensor.setup();
  particleSensor.setPulseAmplitudeRed(0x0A);
  particleSensor.setPulseAmplitudeIR(0x0A);

  // DS18B20
  tempSensor.begin();
}

void loop() {
  // Heart rate and SpO2
  long irValue = particleSensor.getIR();
  float bpm = 0, spo2 = 0;
  if (checkForBeat(irValue)) {
    bpm = particleSensor.getHeartRate();
    spo2 = particleSensor.getSpO2();
  }

  // Temperature
  tempSensor.requestTemperatures();
  float tempC = tempSensor.getTempCByIndex(0);

  // ECG
  int ecgValue = analogRead(ecgPin);

  // Print CSV-style line
  Serial.print(bpm); Serial.print(",");
  Serial.print(spo2); Serial.print(",");
  Serial.print(tempC); Serial.print(",");
  Serial.println(ecgValue);

  delay(100); // Tune for performance
}
