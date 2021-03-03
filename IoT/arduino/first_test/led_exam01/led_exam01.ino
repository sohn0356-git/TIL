int inputdata = 0;
int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available())
  {
    inputdata = Serial.read();
    Serial.println(inputdata);
    if(inputdata=='1')
    {
      digitalWrite(led,HIGH);
    }
  }
  delay(1000);
  digitalWrite(led,LOW);
}
