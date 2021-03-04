
int led_r = 11;
int led_g = 10;
int led_b = 9;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led_r, OUTPUT);
  pinMode(led_g, OUTPUT);
  pinMode(led_b, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int rand_r = random(255);
  int rand_g = random(255);
  int rand_b = random(255);
  
  analogWrite(led_r,rand_r);
  analogWrite(led_g,rand_g);
  analogWrite(led_b,rand_b);
  Serial.print(String(rand_r)+" "+String(rand_g)+" "+String(rand_b)+"\n");
  delay(1000);
}
