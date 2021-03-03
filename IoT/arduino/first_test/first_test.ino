void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  for(int i=9;i<=13;i++)
  {
    pinMode(i, OUTPUT);
  }
}

// the loop function runs over and over again forever
void loop() {
  for(int i=9;i<=13;i++)
  {
    digitalWrite(i, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
  }
  for(int i=13;i>=9;i--)
  {
    digitalWrite(i, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);                           // wait for a second
  }
}
