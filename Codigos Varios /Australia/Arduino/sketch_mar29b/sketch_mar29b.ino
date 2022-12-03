#include <FirebaseCloudMessaging.h>
#include <Firebase.h>
#include <FirebaseHttpClient.h>
#include <FirebaseArduino.h>
#include <FirebaseError.h>
#include <FirebaseObject.h>




#include <ESP8266WiFi.h>


#define FIREBASE_HOST "sweethome8266.firebaseio.com"
#define FIREBASE_AUTH "HNHrBc8D6oIvwa4vpd2hk03k1d28WSyQP46HhkiG"
#define WIFI_SSID "VTR-8130691"
#define WIFI_PASSWORD "gcQtby8H4jvw"


void setup() {
  Serial.begin(9600);

  // connect to wifi.
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

  pinMode(16, OUTPUT);
  pinMode(5, OUTPUT);

    pinMode(14, OUTPUT);
      pinMode(12, OUTPUT);
        pinMode(13, OUTPUT);
          pinMode(15, OUTPUT);

pinMode(A0, OUTPUT);
 
}


void loop() {

 // set string value
  Firebase.setString("message", "Alex7 Tutoriales");
  

   // get value 

    
    if(Firebase.getFloat("Luz_Principal"))
        {digitalWrite(16, HIGH);
        digitalWrite(A0, HIGH);
        Serial.print(Firebase.getFloat("Luz_Principal"));
        }

    else{
      digitalWrite(16, LOW);
      Serial.print(Firebase.getFloat("Luz_Principal"));
    digitalWrite(A0, LOW);
    
    }
  
   if(Firebase.getFloat("Estufa"))
  {
    digitalWrite(5, LOW);
  }
  else{
    digitalWrite(5, HIGH);
  }

    if(Firebase.getFloat("EnchufeG"))
  {
    digitalWrite(14, LOW);
  }
  else{
    digitalWrite(14, HIGH);
  }

  if(Firebase.getFloat("Enchufe1"))
  {
    digitalWrite(12, LOW);
  }
  else{
    digitalWrite(12, HIGH);
  }

 if(Firebase.getFloat("Enchufe2"))
  {
    digitalWrite(13, LOW);
  }
  else{
    digitalWrite(13, HIGH);
  }

   if(Firebase.getFloat("Enchufe3"))
  {
    digitalWrite(15, LOW);
  }
  else{
    digitalWrite(15, HIGH);
  }
delay(500); 





 /* // set value
  Firebase.setFloat("number", 7);
  // handle error
  if (Firebase.failed()) {
      Serial.print("setting /number failed:");
      Serial.println(Firebase.error());  
      return;
  }
  delay(500);
  
  // update value
  Firebase.setFloat("number", 27.0);
  // handle error
  if (Firebase.failed()) {
      Serial.print("setting /number failed:");
      Serial.println(Firebase.error());  
      return;
  }
  delay(500);

 
  // remove value
  Firebase.remove("number");
  delay(100);

  // set string value
  Firebase.setString("message", "Alex7 Tutoriales");
  // handle error
  if (Firebase.failed()) {
      Serial.print("setting /message failed:");
      Serial.println(Firebase.error());  
      return;
  }
  delay(500);

  
  // set string value
  Firebase.setString("message", "Suscribete");
  // handle error
  if (Firebase.failed()) {
      Serial.print("setting /message failed:");
      Serial.println(Firebase.error());  
      return;
  }
  delay(500);
  
  // set bool value
  Firebase.setBool("truth", false);
  // handle error
  if (Firebase.failed()) {
      Serial.print("setting /truth failed:");
      Serial.println(Firebase.error());  
      return;
  }
  delay(1000);

  // append a new value to /logs
 // String name = Firebase.pushInt("logs", n++);
  // handle error
  //if (Firebase.failed()) {
   //   Serial.print("pushing /logs failed:");
   //   Serial.println(Firebase.error());  
  //    return;
 // }
 // Serial.print("pushed: /logs/");
//  Serial.println(name);
 // delay(1000);
  */
}
