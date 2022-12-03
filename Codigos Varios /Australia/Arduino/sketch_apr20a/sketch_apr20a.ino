#include <Servo.h>
 
Servo myservo;  // crea el objeto servo
 
int pos = 0;    // posicion del servo
 int pinLDR = A5;
void setup() {
   myservo.attach(3);  // vincula el servo al pin digital 9

Serial.begin(9600);
}
 
void loop() {

int valorLDR = analogRead(pinLDR);
Serial.println(valorLDR);
  
  if(valorLDR < 90   )
  {
   //varia la posicion de 0 a 180, con esperas de 15ms
   for (pos = 0; pos <= 40; pos +=4) 
   {
      myservo.write(pos);              
      delay(15);                       
   }
 
   //varia la posicion de 0 a 180, con esperas de 15ms
   for (pos = 40; pos >= 0; pos -= 4) 
   {
      myservo.write(pos);              
      delay(15);                       
   }}
}
