import io
import numpy as np

salida = []
nombres=[]

with open('puntajesPSU.txt', 'r') as f:
    lineas = [linea.split(',') for linea in f]
for linea in lineas:

    promedio=(int(linea[2])+int(linea[1]))/2
    nombres=[linea[0],promedio]
    print(nombres)
i=0
j=0

print("                pregunta b              \n")
for linea in lineas:

    promedio=(int(linea[2])+int(linea[1]))/2
    nombres=[linea[0],promedio]
    j=j+1
    if(promedio>=600):
        print(nombres)
        i=i+1

print("se eliminaron")
print(j-i)

po=(i/j)*100


print("Porcentaje de alumnos que tienen un puntaje promedio PSU y puntaje NEM superior a 700   %")
print(po)
