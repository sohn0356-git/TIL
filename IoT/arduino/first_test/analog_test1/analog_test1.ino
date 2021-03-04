void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0;i<255;i++)
  {
    analogWrite(11,i);
    delay(10);
  }
  for(int i=254;i>0;i--)
  {
    analogWrite(11,i);
    delay(10);
  }  
}
