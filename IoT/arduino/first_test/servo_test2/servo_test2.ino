#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int btn_left=7;
int btn_right=8;
int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(btn_left, INPUT);
  pinMode(btn_right, INPUT);
}

void loop() {
  if(digitalRead(btn_left)==0)
  {
    Serial.println("left");
    if(pos-20>=0)
    {
      pos=pos-20;
    }
  }
  if(digitalRead(btn_right)==1)
  {
    Serial.println("right");
    if(pos+20<=180)
    {
      pos=pos+20;
    }
  }
  myservo.write(pos);
  Serial.println(String(pos));
  delay(1000);
}
