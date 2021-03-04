int push_btn = 12;
int led_pin = 11;
int btn_state = 0;
int led_state = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(push_btn,INPUT);
  pinMode(led_pin,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  btn_state = digitalRead(push_btn);
  Serial.println(btn_state);
  if(btn_state==1)
  {
    if(led_state==0)
    {
      led_state = 1;
      digitalWrite(led_pin, HIGH);
      Serial.println("led_on : "+(String)led_state);
    }
    else
    {
      led_state = 0;
      digitalWrite(led_pin, LOW);
      Serial.println("led_off : " + (String)led_state);
    }
  }
  delay(1000);
}
