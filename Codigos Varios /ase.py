def cargar_info_pasajero(nombre_arch):
    f = open(nombre_arch, "r")
    secuencia = ('nombre', 'apellido', 'tipo','numero','pais','edad','equipaje')
    
    versiones = dict.fromkeys(secuencia)
    lista=[]
    i=0
    j=0
    while(True):
        
        linea = f.readline()
        if not linea:
            break
        
        if i==0:
            versiones['nombre'] = linea.replace('\n',"")
            
        if i==1:
            versiones['apellido'] = linea.replace('\n',"")
        if i==2:
            versiones['numero'] = linea.replace('\n',"")
        if i==3:
            versiones['pais'] = linea.replace('\n',"")
        if i==4:
            versiones['tipo'] = linea.replace('\n',"")
        if i==5:
            versiones['edad'] = linea.replace('\n',"")
        if i==6:
            versiones['equipaje'] = linea.replace('\n',"")
            
            

        i=i+1

        

        if i==7:
            
            
            lista.append(versiones)
            secuencia = ('nombre', 'apellido', 'tipo','numero','pais','edad','equipaje')
    
            versiones = dict.fromkeys(secuencia)
            
            i=0
            j=j+1
        

            
          
    
    
    f.close()
    return lista
    



def estadisticas_pasajeros(pasajeros):
    tam=len(pasajeros)
    menor=9999
    mayor=-1
    i=0
    promedio=0
    while(i<tam):
       if(menor>int(pasajeros[i]['edad'])):
           menor=int(pasajeros[i]['edad'])
       if(mayor<int(pasajeros[i]['edad'])):
           mayor=int(pasajeros[i]['edad'])
           
       promedio=promedio+int(pasajeros[i]['edad'])
       i=i+1
    promedio=promedio/tam
    return menor,mayor,promedio

def seleccionar_pasajeros(pasajeros, peso_max):
    tam=len(pasajeros)
    lista=[]
    i=0
    while(i<tam):
       
       if(peso_max<float(pasajeros[i]['equipaje'])):
           
           lista.append(pasajeros[i]['nombre'])
           
       
       i=i+1
    
    return lista

def registrar_seleccionados(lista_seleccion):
    print(lista_seleccion)
    f = open("lista_selecionados.txt", "w")
    f.write(str(lista_seleccion))
    f.close()
    return "archivo creado"
    
    
    

print(registrar_seleccionados(seleccionar_pasajeros(cargar_info_pasajero('pasajeros.txt'),2)))
