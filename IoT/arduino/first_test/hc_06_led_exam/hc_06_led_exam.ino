#include <SoftwareSerial.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#define rxPin 2
#define txPin 3
//swSerial(rxPin,txPin)
LiquidCrystal_I2C lcd(0x27,16,2);
SoftwareSerial swSerial(rxPin,txPin);//(2,3)
String data = "";
void setup() {
  Serial.begin(9600);
  swSerial.begin(9600);
  Serial.println("ready...");
  lcd.init();                      // initialize the lcd 
  // Print a message to the LCD.
  
}
void loop() {
  //시리얼 버퍼를 비우는 작업
  data = "";
  //HC-06(블루투스모듈)이 명령어를 받아서 처리할 시간
  lcd.clear();
  lcd.setCursor(0,0);
  //+++++HC-06으로 부터 전송된 데이터를 화면에 출력++++++
  while(swSerial.available()){
    data = data + (char)swSerial.read();
    if(data==-1){
      break;
    }
    Serial.print(data);
    delay(1);
  }
  if(data=="on")
  {
    lcd.backlight();
    lcd.print(data);   
  }
  else if(data=="off")
  {
    lcd.noBacklight();
  }
 
  Serial.print("\n");
   delay(1000);
}
