int Green = 6;
int Yellow = 4;
int Red = 3;
int Blue = 7;
int What = 8;

void setup() {
  Serial.begin(9600);
  pinMode(Green,OUTPUT);
  pinMode(Yellow,OUTPUT);
  pinMode(Red,OUTPUT);
  pinMode(Blue,OUTPUT);
  

}


char c;
String voice;

void loop() {
  if (Serial.available()>0)
  {
    voice="";
    voice=Serial.readString();
    Serial.print(voice+'\n');
  }

  if(voice=="green")
  {
    digitalWrite(Green,HIGH);
  } else if(voice=="cut")
  {
    digitalWrite(Green,LOW);
  }

    if(voice=="yellow")
  {
    digitalWrite(Yellow,HIGH);
  } else if(voice=="cut")
  {
    digitalWrite(Yellow,LOW);
  }

  
  if(voice=="red")
  {
    digitalWrite(Red,HIGH);
  } else if(voice=="cut")
  {
    digitalWrite(Red,LOW);
  }


    if(voice=="blue")
  {
    digitalWrite(Blue,HIGH);
  } else if(voice=="cut")
  {
    digitalWrite(Blue,LOW);
  }


    if(voice=="on")
  {
    digitalWrite(Blue,HIGH);
    digitalWrite(Red,HIGH);
    digitalWrite(Green,HIGH);
    digitalWrite(Yellow,HIGH);
    digitalWrite(What,HIGH);
  } else if(voice=="stop")
  {
    digitalWrite(Blue,LOW);
    digitalWrite(Red,LOW);
    digitalWrite(Green,LOW);
    digitalWrite(Yellow,LOW);
    digitalWrite(What,LOW);
  }


    if(voice=="DJ")
  {
     digitalWrite(Blue, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(100);              // wait for a second
  digitalWrite(Blue, LOW);   // turn the LED off by making the voltage LOW
  delay(100);
  digitalWrite(Green, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(100);              // wait for a second
  digitalWrite(Green, LOW);   // turn the LED off by making the voltage LOW
  delay(100);
  digitalWrite(Yellow, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(100);              // wait for a second
  digitalWrite(Yellow, LOW);   // turn the LED off by making the voltage LOW
  delay(100);
  digitalWrite(Red, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(100);              // wait for a second
  digitalWrite(Red, LOW);   // turn the LED off by making the voltage LOW
  delay(100);
  } else if(voice=="stop")
  {
    digitalWrite(Blue,LOW);
    digitalWrite(Red,LOW);
    digitalWrite(Green,LOW);
    digitalWrite(Yellow,LOW);
  }

}
