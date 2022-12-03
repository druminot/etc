from time import sleep
import datetime
#from firebase import firebase
import pyfirmata


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

board = pyfirmata.Arduino('/dev/cu.wchusbserial1410')
it = pyfirmata.util.Iterator(board)
it.start()
print("Stargin!!")

firebase = pyrebase.initialize_app(config)
db=firebase.database()


users = db.child("Luz_Principal").get()
print(users.val())
while True :
    if users.val() == "0" :
        board.digital[13].write(1)
        users = db.child("Luz_Principal").get()
        print(users.val())
    if users.val() == "1" :
        board.digital[13].write(0)
        users = db.child("Luz_Principal").get()
        print(users.val())
