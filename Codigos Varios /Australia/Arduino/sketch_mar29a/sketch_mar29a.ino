
#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

// Set these to run example.
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

  pinMode(2, OUTPUT);
  
}

int n = 0;

void loop() {

   // get value 
  if(Firebase.getFloat("led"))
  {
    digitalWrite(2, LOW);
  }
  else{
    digitalWrite(2, HIGH);
  }
  
  // set value
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
  String name = Firebase.pushInt("logs", n++);
  // handle error
  if (Firebase.failed()) {
      Serial.print("pushing /logs failed:");
      Serial.println(Firebase.error());  
      return;
  }
  Serial.print("pushed: /logs/");
  Serial.println(name);
  delay(1000);
  
}
