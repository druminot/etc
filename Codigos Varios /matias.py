s= 1
t= 6
T= 14
nodos1=[k+1 for k in range(6)]
nodos2=[k for k in nodos1 if k!=s if k!=t]
from docplex.mp.model import Model
mdl=Model('ruta_mascorta 2.0')
arcos=[(1,2),(1,3),(3,2),(3,4),(2,4),(2,5),(3,5),(4,5),(4,6),(5,6)]
costos={(1,2):1,(1,3):10,(3,2):1,(3,4):5,(2,4):1,(2,5):2,(3,5):12,(4,5):10,(4,6):1,(5,6):2}
#Nuevo ****************************************************************************************
tiempo={(1,2):10,(1,3):3,(3,2):2,(3,4):7,(2,4):1,(2,5):3,(3,5):3,(4,5):1,(4,6):7,(5,6):2}
x=mdl.integer_var_dict(arcos,name='x')
mdl.minimize(mdl.sum(x[i,j]*costos[i,j] for i,j in arcos))
mdl.add_constraint(mdl.sum(x[i,j] for i,j in arcos if i==s)==1)
mdl.add_constraint(mdl.sum(x[j,i] for j,i in arcos if i==t)==1)
for k in nodos2:
    mdl.add_constraint(mdl.sum(x[i,j] for i,j in arcos if i==k)-mdl.sum(x[j,i] for j,i in arcos if i==k)==0)

#Restriccion de tiempo total******************************************************************
mdl.add_constraint(mdl.sum(x[i,j]*tiempo[i,j] for i,j in arcos)<=T)

solucion=mdl.solve(log_output=True)

solucion.display()
