#include <DHT.h>

DHT mydht11(A1, DHT11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  mydht11.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  int h = mydht11.readHumidity();
  int t = mydht11.readTemperature();
  Serial.println("H : "+String(h)+" T : "+String(t));
  delay(1000);
}
