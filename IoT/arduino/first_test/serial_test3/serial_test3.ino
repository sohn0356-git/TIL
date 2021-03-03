void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available())
  {
    char data = Serial.read();
    Serial.println(data);
//    String stringdata = Serial.readString();
    String test = Serial.readStringUntil('\n');
    Serial.println(test);
    if(test=="end")
    {
      Serial.println("OK"); 
    }
    else
    {
      Serial.println("Fail"); 
    }
  }
  delay(1000);
}
