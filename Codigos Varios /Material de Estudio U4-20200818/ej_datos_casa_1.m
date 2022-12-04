clear all;clc;
%***Probelma de Prediccion***
load datos_casa;
x = datos_casa(1:13,:);%Los regresores de x debe estar dispuesto en Filas
t=  datos_casa(14,:);%Al igual que la salida
net = fitnet(10);%20 neuronas en la capa oculta
 %Se usaba net=newff(t,x,10);
net_entrena = train(net,x,t); %x_entrena=x(:,1:350);
 %net = train(net,x,t);
 %view(net_entrena)
y = net_entrena(x); % x_test=(:,351:560)
 %y_est=net_entrena(x_test);
 %y = sim(net, p);
 rmse=sum((y-t).^2)/length(t)
 
 k=1:1:length(t);
 figure(1)
 plot(k,t,k,y)
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 ylabel('Valor Promedio Casa en USA en miles de dolares')
 legend('Valor promedio Casa','Valor promedio predicho Casa por la Red Neuronal')
 
 %**Comandos antiguos
 [x,t] = house_dataset;%Los regresores de x debe estar dispuesto en Filas
                      %al igual que la salida
                      
  net=newff(x,t,10);%10 neuronas en la capa oculta
  net = train(net,x,t);
  y_old = sim(net, x);
 
 k=1:1:length(t);
 figure(2)
 plot(k,t,k,y_old)
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 ylabel('Valor Promedio Casa en USA en miles de dolares')
 legend('Valor promedio Casa','Valor promedio predicho Casa por la Red Neuronal')
 
 %**********Datos Vino*************
 load data_vinos_2clases
 x=data_vinos_2clases(:,1:2)'
 t=data_vinos_2clases(:,14)'
 
 net=newff(x,t,20);%20 neuronas en la capa oculta
 net = train(net,x,t);
 y_old = sim(net, x);
 
 k=1:1:length(t);
 figure(3)
 plot(k,t,k,y_old)
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')

 