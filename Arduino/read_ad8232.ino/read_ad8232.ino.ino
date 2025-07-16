const int ecgPin = 34; // Must be an ADC-capable pin on ESP32

void setup() {
  Serial.begin(115200);
  pinMode(ecgPin, INPUT);
}

void loop() {
  int ecgValue = analogRead(ecgPin);
  Serial.println(ecgValue);
  delay(5); // High frequency sampling
}
