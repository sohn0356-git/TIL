
int btn_state =0;
int btn = 8;
int led_r = 11;
int led_g = 10;
int led_b = 9;
int brights[3] = {0,0,0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(btn, INPUT);
  pinMode(led_r, OUTPUT);
  pinMode(led_g, OUTPUT);
  pinMode(led_b, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
//  int rand_r = random(255);
//  int rand_g = random(255);
//  int rand_b = random(255);
//  
//  analogWrite(led_r,rand_r);
//  analogWrite(led_g,rand_g);
//  analogWrite(led_b,rand_b);
//  Serial.print(String(rand_r)+" "+String(rand_g)+" "+String(rand_b)+"\n");
//  delay(1000);
    int btn_input = digitalRead(btn);
    if(btn_input==1)
    {
      btn_state = (btn_state + 1)%3;
    }
    int bright = analogRead(A0)/4;
    brights[btn_state] = bright;
    analogWrite(led_r,brights[0]);
    analogWrite(led_g,brights[1]);
    analogWrite(led_b,brights[2]);
    Serial.println(String(btn_state)+" "+String(brights[0])+" "+String(brights[1])+" "+String(brights[2]));
    delay(1000);
}
