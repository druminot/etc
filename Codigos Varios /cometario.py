#Parte de la 3
def sin_dosis2(dosis1,dosis2):
    datos=list(dosis1)
    for datos in dosis2:
        dosis1.pop(datos)
    return list(dosis1)

#Parte de la 4
def guardar_sujetos_sin_dosis2(listado_sin_dosis2):
    f = open("personas_sin_dosis2.txt", "a")
    for k in listado_sin_dosis2:
        f.write(k + '\n')
    f.close()
    
    
#Parte de la 1
def procesar_archivo_dosis(archivo_dosis):

    f = open(archivo_dosis, "r")
    diccionario={" ":""}
    while(True):
        linea = f.readline()
        if not linea:
            break
        
        datos_linea=linea.replace('\n',"")
        datos_linea2=datos_linea.split(',')
       
        diccionario.update({datos_linea2[0]:datos_linea2[1]})
        
        if not linea:
            
            
            break
    diccionario.pop(' ')
    
    f.close()
    return diccionario


#Parte de la 2
dosis_1=procesar_archivo_dosis("vacunados_dosis1.txt")
dosis_2=procesar_archivo_dosis("vacunados_dosis2.txt")


