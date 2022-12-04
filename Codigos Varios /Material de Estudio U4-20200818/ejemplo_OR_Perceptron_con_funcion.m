%Entrenamiento Perceptron funcion OR (O)
clear all
x1=[0 0 1 1]';x2=[0 1 0 1]';d=[0 1 1 1]';

%x1 | x2 | d=or=o logico |      %x1 | x2 | d=and=y logico |
%0  |  0 |   0  |               %0  |  0 |   0  |
%0  |  1 |   1  |               %0  |  1 |   0  |
%1  |  0 |   1  |               %1  |  0 |   0  |
%1  |  1 |   1  |               %1  |  1 |   1  |

x0=ones(size(x1,1),1);
gamma=0.9;
%Regla de Ajuste de los pesos sinapticos wi (equivalente a los 
%coeficientes que acopañan a los regresores en una curva
%de Regresion Lineal)
X=[x0 x1 x2];% (MatrizX), además, el vector W0=[w0 w1 w2]
W0=[1.5 0.5 1.5]';
w=W0;
% Algoritmo: SI encontramos un error distinto de 0, los pesos wi se 
%modifican segun la regla: wi(k+1)=wi(k)+gamma*e(k)*Xi(k)
%es decir: wi(k+1)=wi(k)+gamma*(d(k)-y(k))*Xi(k)
n=size(x2,1);%n=4 en este caso
e=100;%Esta variable nos sirve para inciar el ciclo WHILE
j=0;

while any(e)~=0 %Verdadero si cualquier elemnto del vector e es distinto de 0
 j=j+1  %Esta variable nos sirve para saber cuantas veces se entra al ciclo 
        %o loop FOR
for k=1:n %n es el largo de la data (=4 patrones o ejemplos o muestras)

Net=X(k,:)*W0;

y=escalon(Net);

e(k)=d(k)-y;
  if e(k)~=0 %Modificar wi
    w=w+gamma*e(k)*X(k,:)';
    W0=w;
  end
     
end
  
end



