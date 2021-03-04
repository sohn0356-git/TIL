void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int inputVal = analogRead(A0);
  Serial.println(inputVal);
  if(inputVal>500)
  {
    analogWrite(11,inputVal);
  }
  else
  {
    analogWrite(11,0);
  }
  delay(500);
}
