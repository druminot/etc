
def buscar_propiedades(caracteristicas,metrosMin,metrosMax):
    file = open("valor_propiedades.txt", "w")
    caracteristica =["1D","2D","3D","2D","4D","4D","2D","3D"]
    metros = [50, 70, 90, 90, 120, 140,  110, 100 ] #estos metros corresponden al total de la propiedad
    valor = [350, 370, 490, 590, 1020, 1140, 760, 1080] #estos corresponden al precio final en UF

    caracteristica_en_archivo =["1 Dormitoro","2 Dormitoro","3 Dormitoro","2 Dormitoro","4 Dormitoro","4 Dormitoro","2 Dormitoro","3 Dormitoro"]


    for i in range(len(metros)):
        if (metros[i]<=metrosMax and caracteristica[i]==caracteristicas and metros[i]>= metrosMin):
            info=str(valor[i])+" "+caracteristica_en_archivo[i]+"\n"
            file.write(info)

    file.close()



print("caracteristica")
caracteristica = input()
print("metrosMin")
metrosMin = int(input())
print("metrosMax")
metrosMax = int(input())

buscar_propiedades(caracteristica,metrosMin,metrosMax)
