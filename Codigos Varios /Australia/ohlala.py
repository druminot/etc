from time import sleep
import datetime
#from firebase import firebase
#import serial
import time

#firebase = firebase.FirebaseApplication('https://jepeuxlefaire-ff46f.firebaseio.com/')
import pyrebase



config = {
    'apiKey': "AIzaSyDG8mcVMAgN0wOwGYFDBWA06gpc7FVtpus",
    'authDomain': "sweethome8266.firebaseapp.com",
    'databaseURL': "https://sweethome8266.firebaseio.com",
    'projectId': "sweethome8266",
    'storageBucket': "sweethome8266.appspot.com",
    'messagingSenderId': "753170103654"
  }




print("Stargin!!")

firebase = pyrebase.initialize_app(config)
db=firebase.database()


users = db.child("Luz_Principal").get()
print(users.val())

if users.val() == "0" :
    texto ="1"
    db.child("Luz_Principal").set(texto)
if users.val() == "1" :
    texto ="0"
    db.child("Luz_Principal").set(texto)
