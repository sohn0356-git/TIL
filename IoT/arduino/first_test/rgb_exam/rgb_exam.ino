
int btn_state =0;
int btn = 8;
int led_r = 11;
int led_g = 10;
int led_b = 9;
int echoPin = 12;
int trigPin = 13;
int brights[3] = {0,0,0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(btn, INPUT);
  pinMode(led_r, OUTPUT);
  pinMode(led_g, OUTPUT);
  pinMode(led_b, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int rand_r = random(255);
  int rand_g = random(255);
  int rand_b = random(255);
  digitalWrite(trigPin, HIGH);
  delay(10);
  digitalWrite(trigPin, LOW);
  
  double duration = pulseIn(echoPin, HIGH); 
// HIGH 였을 때 시간(초음파가 보냈다가 다시 들어온 시간)을 가지고 거리를 계산 한다.
  double distance = ((double)(340 * duration) / 10000) / 2;  
  if(distance<20)
  {
    analogWrite(led_r,rand_r);
    analogWrite(led_g,0);
    analogWrite(led_b,0);
  }
  else if(distance<60)
  {
    analogWrite(led_g,rand_g);
    analogWrite(led_r,0);
    analogWrite(led_b,0);
  }
  else
  {
    analogWrite(led_b,rand_b);
    analogWrite(led_r,0);
    analogWrite(led_g,0);
  }
  Serial.print(distance);
  Serial.println("cm");
// 수정한 값을 출력
  delay(500);
  
}
