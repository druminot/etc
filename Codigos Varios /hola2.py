
from statistics import mode
ciudades = []
permisos = []

print("para finalizar en cualquier momento ingrese fin ")
while(1):
    print("ingrese nombre Ciudad:")
    ciudad=input()

    if ciudad=="fin":
        break
    print("ingrese Tipo de Permiso:")
    permiso=input()
    if permiso=="fin":
        break

    print("desea guardar (si)/(no):")
    condicion=input()
    if condicion=="si":
        #file.write(ciudad)
        #//file.write(",")
        #file.write(permiso)
        #file.write("\n")
        ciudades.append(ciudad)
        permisos.append(permiso)
print(" 3. Porcentaje de solicitudes por cada ciudad, respecto al total nacional ")
print("total 100% es:")
total=len(ciudades)
ciudades2 = set(ciudades)
print("    \n")

for x in ciudades2:
    print(x)
    p=ciudades.count(x)
    print((p/total)*100)




print(" 1. ciudad con mas permisos ")
print(mode(ciudades))
print(" 2. Tipos de permiso que fueron solicitados más veces que el promedio ")
print(mode(permisos))
print(" 3. Porcentaje de solicitudes por cada ciudad, respecto al total nacional ")




print(ciudades)
print(permisos)
