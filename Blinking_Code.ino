int IRsensor = 13;
int sensorpin=0;
int blinking_time=0;
const int buzzer = 8;

void setup()
{
  Serial.begin(9600);// Making serial monitor ready to be used by python3
  pinMode( LED_BUILTIN, OUTPUT);
  pinMode(13, INPUT); // 
  pinMode(buzzer, OUTPUT);
}

void loop()
{ 
  blinking_time=analogRead(sensorpin);
  Serial.println(blinking_time);
  delay(2000);
  long state=digitalRead(IRsensor);
  if(state==HIGH)
  {
    digitalWrite(LED_BUILTIN ,LOW );
    Serial.println("The timing is greater than 100 sec sleeping wakeup!!");
    delay(2000);
    tone(buzzer, 100); // Send 1KHz sound signal...
    delay(1000);  
  }
  else
  {
     digitalWrite(LED_BUILTIN ,HIGH ); 
     Serial.println("The timing is less than 100 sec...so safe driving");
     delay(2000);
     noTone(buzzer);     // Stop sound...
     delay(1000); }}
  
