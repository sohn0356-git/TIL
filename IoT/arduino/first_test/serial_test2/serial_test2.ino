int indata = 65;
char chdata = 65;
float fldata = 65;
int inputdata = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
//  Serial.println(indata);
//  Serial.println(chdata);
//  Serial.println(fldata);
//  delay(1000);
  if(Serial.available()>0)
  {
    inputdata = Serial.read();
    Serial.write(inputdata);
    Serial.print(", ");
    Serial.println(inputdata);
  }
}
