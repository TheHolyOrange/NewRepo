int enA=9;
int in1=8;
int in2=7;
int in3=6;
int in4=5;
int enB=3;
int in=12;

void setup()
{
  pinMode(enA,OUTPUT);
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  pinMode(enB,OUTPUT);
  pinMode(in,INPUT);
}
void loop()
{
  if (digitalRead(in)==0)
  {
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    analogWrite(enA, 255);
    digitalWrite(in3,HIGH);
    digitalWrite(in4, LOW);
    analogWrite(enB,255);
  }
  else 
  {
      digitalWrite(in1,LOW);
      digitalWrite(in2,HIGH);
      analogWrite(enA, 255);
      digitalWrite(in3,LOW);
      digitalWrite(in4, HIGH);
      analogWrite(enB,255);
      delay(1000);
      digitalWrite(in1,LOW);
      digitalWrite(in2,HIGH);
      analogWrite(enA, 255);
      digitalWrite(in3,LOW);
      digitalWrite(in4, HIGH);
      analogWrite(enB,10);
      delay(1000);
  }
}
