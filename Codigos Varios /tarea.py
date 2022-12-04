import pandas as pd
import numpy as np

from datetime import date

#version sin suposiciones 


maestra=pd.read_csv('https://raw.githubusercontent.com/globosc/maestra/master/maestra.csv')

datos = pd.read_csv('http://bit.ly/2ZNXHTQ')

print("muestra datos de la base de datos")
print(maestra)
print(datos)

# pregunta 2
datos['cantidad']=datos['cantidad'].astype('int')
print("dataframe pregunta 2")
print(datos)

# pregunta 3 
data1 = pd.DataFrame(columns=( 'año', 'mes', 'dia','cantidad','venta'))
data2 = pd.DataFrame(columns=( 'año', 'mes', 'dia','cantidad','venta'))
data3 = pd.DataFrame(columns=( 'año', 'mes', 'dia','cantidad','venta'))


i = 0
print("metodo a ingresar (diario/semanal/mensual) si no desea ingresar solo aprete enter")

opcion = input()


if opcion == 'diario':

    print("ingrese: año/enter mes/enter dia/enter cantidad/enter venta/enter")

    data1.loc[len(data1)]=[input(),input(),input(),input(),input()]
    print("dataframe pregunta 3")
    print(data1)





if opcion == 'semanal':
    print("ingrese año:")
    año= input()
    print("ingrese mes:")
    mes= input()
    while i<7:
        print(f"ingrese:dia {i+1}(fecha)/enter  cantidad/enter venta/enter")
        data2.loc[len(data2)]=[año,mes,input(),input(),input()]
        i += 1
    print("dataframe pregunta 3")
    print(data2)

if opcion == 'mensual':
    while i<32:
        print(f"ingrese:dia {i+1}(fecha)/enter cantidad/enter venta/enter")
        data3.loc[len(data3)]=[input(),input(),input(),input(),input()]
    print("dataframe pregunta 3")
    print(data3)


# pregunta 4

#se queda con los datos superior al 2018 del link
datos = datos[(datos.año>=2018)]

print("dataframe pregunta 4")
print(datos)

# pregunta 5


# primero ordena por año los datos del link creando la variable oxa con los datos ordenados por año (oxa)
oxa = datos.sort_values(['año'])


#luego toma las 3 columnas para juntarlas en 1
oxa['fecha'] = oxa[['dia','mes','año']].apply(lambda x :'{}-{}-{}'.format(x[0],x[1],x[2]), axis=1)
oxa=oxa[['fecha','cantidad','venta']]

# a esa nueva columna se le da formato fecha
oxa['fecha']=pd.to_datetime(oxa['fecha'])
# y se ordena como deseamos 
oxa['fecha']=oxa['fecha'].dt.strftime('%d-%m-%Y')


print("dataframe pregunta 5")
print(oxa)
# pregunta 6

# crea la columna y el primer dato es "mani con sal 200gr"
oxa['productos'] = 'mani con sal 200 gr'

#segundo dato no especifica la condicion de como se ingresa 

oxa['productos'] = 'mani sin sal 200 gr'


print("dataframe pregunta 6")
print(oxa)

#pregunta 7


momentanea = pd.DataFrame(columns=('sku','codigo'))
maestra['productos']=maestra['descripcion']
datos = pd.read_csv('http://bit.ly/2ZNXHTQ')
datos['productos'] = 'mani sin sal 200 gr'
transacciones2=pd.merge(datos,maestra,on='productos')
momentanea2=transacciones2['sku'].str.split('-', 1, expand=True)
datos['codigo'] =momentanea2[0]
datos = datos[(datos.año>=2018)]
oxa = datos.sort_values(['año'])
oxa['fecha'] = oxa[['dia','mes','año']].apply(lambda x :'{}-{}-{}'.format(x[0],x[1],x[2]), axis=1)
oxa=oxa[['fecha','cantidad','venta','productos','codigo']]
oxa['fecha']=pd.to_datetime(oxa['fecha'])
oxa['fecha']=oxa['fecha'].dt.strftime('%d-%m-%Y')
print("dataframe pregunta 7")
print(oxa)




#pregunta 8

#ordena primero por producto y fecha 
oxa = oxa.sort_values(['productos','fecha'])


print("dataframe pregunta 8")
print(oxa)

#pregunta 9

#crea la columna y para cada producto 

oxa['ultima fecha']="0"

#segundo dato no especifica la condicion de como se ingresa , no esta claro 

print("dataframe pregunta 9")
print(oxa)


#pregunta 10

#la pregunta no es clara pero podria ser algo asi 
#se crea la de precio
oxa['precio']=oxa.venta/oxa.cantidad
print(oxa.precio.describe())


#se crea la filas con None

oxa.loc[-1]=['0','None','None','None','None','2','b']




#luego no se entiende

print("dataframe pregunta 10")
print(oxa)


