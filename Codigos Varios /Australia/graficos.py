
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import socket
import struct
import time 
import datetime
import matplotlib.pyplot as plt

# Use a service account
cred = credentials.Certificate('/Users/druminot/Downloads/rasberrypi-druminot.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref0 = db.collection(u'Funcionamiento').document(u'Registro_Estufa').collection(u'Date').document(u'100519')
doc_ref1 = db.collection(u'Funcionamiento').document(u'Registro_Estufa').collection(u'Date').document(u'090519')
doc_ref2 = db.collection(u'Funcionamiento').document(u'Registro_Estufa').collection(u'Date').document(u'080519')
doc_ref3 = db.collection(u'Funcionamiento').document(u'Registro_Estufa').collection(u'Date').document(u'070519')
doc_ref4 = db.collection(u'Funcionamiento').document(u'Registro_Estufa').collection(u'Date').document(u'060519')
doc_ref5 = db.collection(u'Funcionamiento').document(u'Registro_Estufa').collection(u'Date').document(u'050519')
doc_ref6 = db.collection(u'Funcionamiento').document(u'Registro_Estufa').collection(u'Date').document(u'040519')

try:
    doc = doc_ref0.get()
    dic = doc.to_dict()
    i0=0
    k0=0
    for t, v in dic.items():
        if v == "Encendida":
            i0=i0+1
        if v == "Apagada":
            k0=k0+1
    print(i0)
    print(k0)
    
    doc = doc_ref1.get()
    dic = doc.to_dict()
    i1=0
    k1=0
    for t, v in dic.items():
        if v == "Encendida":
            i1=i1+1
        if v == "Apagada":
            k1=k1+1
    print(i1)
    print(k1)

    doc = doc_ref2.get()
    dic = doc.to_dict()
    i2=0
    k2=0
    for t, v in dic.items():
        if v == "Encendida":
            i2=i2+1
        if v == "Apagada":
            k2=k2+1
    print(i2)
    print(k2)

    doc = doc_ref3.get()
    dic = doc.to_dict()
    i3=0
    k3=0
    for t, v in dic.items():
        if v == "Encendida":
            i3=i3+1
        if v == "Apagada":
            k3=k3+1
    print(i3)
    print(k3)

    doc = doc_ref4.get()
    dic = doc.to_dict()
    i4=0
    k4=0
    for t, v in dic.items():
        if v == "Encendida":
            i4=i4+1
        if v == "Apagada":
            k4=k4+1
    print(i4)
    print(k4)

    doc = doc_ref5.get()
    dic = doc.to_dict()
    i5=0
    k5=0
    for t, v in dic.items():
        if v == "Encendida":
            i5=i5+1
        if v == "Apagada":
            k5=k5+1
    print(i5)
    print(k5)

    doc = doc_ref6.get()
    dic = doc.to_dict()
    i6=0
    k6=0
    for t, v in dic.items():
        if v == "Encendida":
            i6=i6+1
        if v == "Apagada":
            k6=k6+1
    print(i6)
    print(k6) 

    
except google.cloud.exceptions.NotFound:
    print(u'No such document!')




fig = plt.figure(u'Luz') # Figure
ax = fig.add_subplot(111) # Axes

nombres = ['100519','090519','080519','070519','060519','050519','040519']
datos = [i0/60,i1/60,i2/60,i3/60,i4/60,i5/60,i6/60]
xx = range(len(datos))

ax.bar(xx, datos, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(nombres)

plt.show()
