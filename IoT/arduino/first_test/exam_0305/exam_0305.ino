#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pir = 7;
int btn = 8;
int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(pir, INPUT);
  pinMode(btn, INPUT);
  
}

void loop() {
  int input = digitalRead(pir);
  if(digitalRead(btn)==1)
  {
    Serial.println("open btn clicked");
    pos = (pos + 90)%180;
  }
  if(input==1)
  {
    pos = 90;
    Serial.println("출입문이 열립니다.");
  }
  myservo.write(pos);
  Serial.println(String(pos));
  delay(1000);
}
