void setup() {
  // put your setup code here, to run once:
  pinMode(11,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(11,1);
  delay(1); //10%
  digitalWrite(11,0); 
  delay(9);
}
