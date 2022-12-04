

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
    print(diccionario)
    f.close()

procesar_archivo_dosis("vacunados_dosis1.txt")
