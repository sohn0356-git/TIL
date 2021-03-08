//Compatible with the Arduino IDE 1.0
//Library version:1.1
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

DHT mydht11(A1, DHT11);
LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x20 for a 16 chars and 2 line display
 
void setup()
{
  Serial.begin(9600);
  mydht11.begin();
  lcd.init();                      // initialize the lcd 
  // Print a message to the LCD.
  lcd.backlight();
  lcd.print("Hello, world!");
}
 
void loop()
{
  lcd.setCursor(0,0); 
  int h = mydht11.readHumidity();
  int t = mydht11.readTemperature();
  int photoresistorVal = analogRead(A0);
  Serial.println("H : "+String(h)+" T : "+String(t));
  Serial.println(photoresistorVal);
  if(photoresistorVal>500)
  {
    lcd.print("H : "+String(h)+" T : "+String(t));
  }
  else
  {
    lcd.print("Hello, world!");
  }  
  delay(1000);
}
