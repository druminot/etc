clear all;clc;
load data_vinos_2clases

X=data_vinos_2clases(:,1:2);
t=data_vinos_2clases(:,14);

x1=X(:,1);
x2=X(:,2);

figure(1)
gscatter(x1,x2,t,'br','o^');%  gscatter(...,grupo,'colores','figuras') %Color y luego tipo de figura
xlabel('x1')
ylabel('x2')

%El centro del cluster depende bastante de los cluster que se escojan 
%al inicio del algoritmo
%Buenos centros de clusters:
%C1=[12.4  2] C2=[13.7 1.9]
k=2;
[id,C] = kmeans(X,k,'MaxIter',1000);%id indica a que grupo fueron asignadsos
%los centros de los cluster C

figure(2)
gscatter(x1,x2,t,'br','o^') %Color y luego tipo de figura
xlabel('x1')
ylabel('x2')

hold on
plot(C(1,1),C(1,2),'^c',C(2,1),C(2,2),'oc')
hold off



% [idx,C,sumd,D] = kmeans(X,k);
% [idx,C,sumd,D] = kmeans(X,k,Name,Value)