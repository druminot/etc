def simulacion(lineas):
    x=input("¿Desea que corra de manera automatica desde ya? (s/n):")

    linea0=lineas[0][0]
    
    cajas=linea0.split(",")
    
    Cantcaj_gen=int(cajas[0])
    
    Cantcaj_tit=int(cajas[1])
    
    Cantcaj_emp=int(cajas[2])
    
    lineas.pop(0)
    
    col_gen = []
    
    caj_gen =[0]*Cantcaj_gen
    
    cola_emp = []
    
    caj_emp = [0]*Cantcaj_emp
    
    col_tit = []
    
    caj_tit = [0]*Cantcaj_tit
    
    tiempo = 0
    
    despachados = []
    
    cantidad_clientes=len(lineas)
    
    entradas_=[]
    
    texto=""
    
    while len(despachados) < cantidad_clientes:
        
       
        for cliente in cola_emp:
            cliente[2]=cliente[2]+1
        for cliente in col_tit:
            cliente[2]=cliente[2]+1
        for cliente in col_gen:
            cliente[2]=cliente[2]+1
            
        
        i=0
              
        for caja in caj_tit:
            if caja!=0:
                caj_tit[i][3]=int(caj_tit[i][3])+1
                if int(caja[1])<=int(caja[3]):
                    despachados.append(caja)

                    if len(col_tit)!=0:
                        caj_tit[i]=col_tit[0]+["t"]
                        col_tit.pop(0)
                    
                    elif len(cola_emp)!=0: 
                        caj_tit[i]=cola_emp[0]+["e"]
                        cola_emp.pop(0) 
                    
                    elif len(col_gen)!=0:
                        caj_tit[i]=col_gen[0]+["g"]
                        col_gen.pop(0)
                    else:
                        caj_tit[i]=0
            i=i+1
        i=0
        for caja in caj_emp:
            if caja!=0:
                caj_emp[i][3]=int(caj_emp[i][3])+1
                if int(caja[1])<=int(caja[3]): 
                    despachados.append(caja) 
                    
                    
                    if len(cola_emp)!=0: 
                        caj_emp[i]=cola_emp[0]+["e"]
                        cola_emp.pop(0)
                    elif len(col_tit)!=0:
                        caj_emp[i]=col_tit[0]+["t"]
                        col_tit.pop(0)
                    elif len(col_gen)!=0:
                        caj_emp[i]=col_gen[0]+["g"]
                        col_gen.pop(0)
                    else:
                        caj_emp[i]=0
            i=i+1        
        i=0  
        for caja in caj_gen:
            if caja!=0:
                caj_gen[i][3]= int(caj_gen[i][3])+1
                
                if int(caja[1])<=int(caja[3]):
                    
                    despachados.append(caja)
                    
                    if len(col_gen)!=0:
                        caj_gen[i]=col_gen[0]+["g"]
                        col_gen.pop(0)
                    
                    elif len(cola_emp)!=0: 
                        caj_gen[i]=cola_emp[0]+["e"] 
                        cola_emp.pop(0)
                        
                    elif len(col_tit)!=0:
                        caj_gen[i]=col_tit[0]+["t"]
                        col_tit.pop(0)
                    else:
                        caj_gen[i]=0
            i=i+1

        clientesEntrantes=[]

        for cliente in lineas:
            cliente=cliente[0].split(",")
            if cliente[2]=="0" and int(cliente[3])==tiempo:
                 clientesEntrantes.append(cliente)
      
        for cliente in lineas:
            cliente=cliente[0].split(",")
            if cliente[2]=="1" and int(cliente[3])==tiempo:
                clientesEntrantes.append(cliente)
               

        

                 
        for cliente in clientesEntrantes:
            Numero=cliente[0]
            tipo = cliente[1]
            pref = cliente[2]
            llegada =int(cliente[3])
            salida = int(cliente[4])
            atendido = False 
           
            if tipo=="e":
                i=0
                for caja in caj_emp:
                    if caja==0:
                           
                        caj_emp[i]=[Numero,salida,0,0,"e"]
                        atendido=True
                        break
                    i=i+1
           
            elif tipo=="t":
                i=0
                for caja in caj_tit:
                    if caja==0:
                        caj_tit[i]=[Numero,salida,0,0,"t"]
                        atendido=True
                        break
                    i=i+1
           
            else:
                i=0
                for caja in caj_gen:
                    if caja==0:
                        caj_gen[i]=[Numero,salida,0,0,"g"]
                        atendido=True
                        break
                    i=i+1
           
            if atendido==False:
                
              
                i=0
                for caja in caj_emp:
                    if caja==0:
                        
                        caj_emp[i]=[Numero,salida,0,0,"e"]
                        atendido=True
                        break
                    i=i+1
                
                if atendido==False:
                    i=0
                    for caja in caj_tit:
                        if caja==0:
                            
                            caj_tit[i]=[Numero,salida,0,0,"t"]
                            atendido=True
                            break
                        i=i+1
                   
                    if atendido==False:
                        i=0
                        for caja in caj_gen:
                            if caja==0:
                                
                                caj_gen[i]=[Numero,salida,0,0,"g"]
                                atendido=True
                                break
                            i=i+1
    
                       
                    if atendido==False:
                        
                        if tipo=="e":
                            if pref=="1":
                                cola_emp.insert(0,[Numero,salida,0,0])
                            else:    
                                cola_emp.append([Numero,salida,0,0])
                        elif tipo=="t":
                            if pref=="1":
                                col_tit.insert(0,[Numero,salida,0,0])
                            else:    
                                col_tit.append([Numero,salida,0,0])
                        else:
                            if pref=="1":
                                col_gen.insert(0,[Numero,salida,0,0])
                            else:
                                col_gen.append([Numero,salida,0,0])

        print ("Tiempo:",str(tiempo))
        texto=texto+("Tiempo: "+str(tiempo))+"\n"
        print ("-------")
        texto=texto+("-------")+"\n"
      
        linea_colgen=""
        for cliente in col_gen:
            linea_colgen=linea_colgen+cliente[0]+" "
        if linea_colgen=="":
            print ("Cola de clientes general: -")
            texto=texto+("Cola de clientes general: -")+"\n"
        else:
            print ("Cola de clientes general:",linea_colgen)
            texto=texto+("Cola de clientes general: "+linea_colgen)+"\n"

        print ("Cajas de clientes general")
        texto=texto+("Cajas de clientes general")+"\n"

        i=0
        for caja in caj_gen:
            if caja ==0:
                print ("Caja"+str(i)+": 0")
                texto=texto+("Caja"+str(i)+": 0")+"\n"
            else:
                print ("Caja"+str(i)+": "+caja[0])
                texto=texto+("Caja"+str(i)+": "+caja[0])+"\n"
            i=i+1
        linea_coltit=""
        for cliente in col_tit:
            linea_coltit=linea_coltit+cliente[0]+" "
        if linea_coltit=="":
            print ("Cola de clientes titulares: -")
            texto=texto+("Cola de clientes titulares: -")+"\n"
        else:
            print ("Cola de clientes titulares:",linea_coltit)
            texto=texto+("Cola de clientes titulares: "+linea_coltit)+"\n"

        print ("Cajas de clientes titulares")
        texto=texto+("Cajas de clientes titulares")+"\n"

        i=0
        for caja in caj_tit:
            if caja ==0:
                print ("Caja"+str(i)+": 0")
                texto=texto+("Caja"+str(i)+": 0")+"\n"
            else:
                print ("Caja"+str(i)+": "+caja[0])
                texto=texto+("Caja"+str(i)+": "+caja[0])+"\n"
            i=i+1
                
     
        linea_colemp=""
        for cliente in cola_emp:
            linea_colemp=linea_colemp+cliente[0]+" "
        if linea_colemp=="":
            print ("Cola de clientes empresa: -")
            texto=texto+("Cola de clientes empresa: -")+"\n"
        else:
            print ("Cola de clientes empresa:",linea_colemp)
            texto=texto+("Cola de clientes empresa: "+linea_colemp)+"\n"

        print ("Cajas de clientes empresa")
        texto=texto+("Cajas de clientes empresa")+"\n"

        i=0
        for caja in caj_emp:
            if caja ==0:
                print ("Caja"+str(i)+": 0")
                texto=texto+("Caja"+str(i)+": 0")+"\n"
            else:
                print ("Caja"+str(i)+": "+caja[0])
                texto=texto+("Caja"+str(i)+": "+caja[0])+"\n"
            i=i+1
    
        linea_desp=""

        for cliente in despachados:
            linea_desp=linea_desp+cliente[0]+" "
        if linea_desp=="":
            print ("los clientes despachados: -")
            texto=texto+("los clientes despachados: -")+"\n"
        else:
            print ("los clientes despachados:"+linea_desp)
            texto=texto+("los clientes despachados:"+linea_desp)+"\n"
        tiempo=tiempo+1

        if x!="s":
            seguir=input("Enter para seguir:")
        
    for cliente in despachados:
        if cliente[4]=="g": 
            Tcaja="General"
        elif cliente[4]=="t":
            Tcaja="Titulares"
        else:
            Tcaja="Empresas"
        print ("El cliente N°"+cliente[0]+" se atendió en la caja "+Tcaja+", el tiempo total de atención fue de "+str(cliente[2]+cliente[3])+" min ("+str(cliente[2])+" min en cola y "+str(cliente[3])+" min en caja)")
        texto=texto+("El cliente N°"+cliente[0]+" se atendió en la caja "+Tcaja+", el tiempo total de atención fue de "+str(cliente[2]+cliente[3])+" min ("+str(cliente[2])+" min en cola y "+str(cliente[3])+" min en caja)")
    
    return texto



def crearte(texto):
    archivo=open("SB.txt","w")
    archivo.write(texto)
    archivo.close()


def validacion(l):
   
    c=l[0][0].split(",")
    if int(c[0])<=0 or int(c[1])<=0 or int(c[2])<=0:
        print ("Error con el registro de cajas")
    else:
        for lin in l:
            lista=lin[0].split(",")
            for string in lista:
                for caracter in string:
                    if caracter not in "1234567890egt":
                        l.remove(lin)
        t=simulacion(l)
    return t



def AbrirDB(nombre_Archivo):
    info=open(nombre_Archivo,encoding='utf-8')
    l=[]
    for lin in info:
        l.append(lin.strip().split("\t"))
    info.close()
    return l

    

                
l=AbrirDB("banco_ej3.dat") #abre .dat y guarda en un cadena

t=validacion(l) #valida

crearte(t) #crea archivo 



