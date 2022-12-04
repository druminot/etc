f = open ('1920-2020_final.csv','r')
f2 = open ('1920-2020_resumen.csv','w')
x=1
x2=1
xm=1
for h in f:
       fx=h.strip().split(';')
       print(fx)
       if fx[1]=='Brian' and fx[0]=='1996' :
          print(fx[3])

      
             
	




mensaje = f.read()

f2.write(mensaje)
print(x)
f.close()



f2.close()
        
