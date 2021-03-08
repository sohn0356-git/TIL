#include <SoftwareSerial.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);

#define rxPin 3
#define txPin 2

SoftwareSerial swSerial(rxPin, txPin);
char data;
void setup() {
  Serial.begin(9600);
  swSerial.begin(9600);
  Serial.println("준비완료...");
   lcd.init();                      // initialize the lcd 
  // Print a message to the LCD.
  lcd.backlight();
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.flush();
  Serial.println("command : ");
  while(!Serial.available());
  while(Serial.available())
  {
    data = Serial.read();
    Serial.print(data);
    swSerial.println(data);
    delay(1);
  }
  if(swSerial.available())
  {
    Serial.println("H");
    Serial.println(swSerial.read());
  }
  
  Serial.println();
  delay(1000);
//    lcd.setCursor(0,0);
//    swSerial.print("t");
//    if(swSerial.available())
//    {
//      data = swSerial.read();
//      Serial.print(data);
//      lcd.print(data);
//    }
//    delay(1000);
  
}
