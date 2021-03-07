void setup() {
  // put your setup code here, to run once:
  pinMode(7, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int input = digitalRead(7);
  Serial.println(input);
  delay(100);
}
