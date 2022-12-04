clear all;clc;
%***Probelma de Prediccion***
load datos_casa;
x_v = datos_casa(1:13,1:253);%Los regresores de x debe estar dispuesto en Filas
t_v=  datos_casa(14,1:253);%Al igual que la salida
%***Data de validacion***
x_e = datos_casa(1:13,254:506);%Los regresores de x debe estar dispuesto en Filas
t_e=  datos_casa(14,254:506);%Al igual que la salida

net_e = fitnet(10);%20 neuronas en la capa oculta
 %Se usaba net=newff(t,x,10);
net_entrena = train(net_e,x_e,t_e); %x_entrena=x(:,1:350);
 %net = train(net,x,t);
 %view(net_entrena)
y_e = net_entrena(x_e); % x_test=(:,351:560)
y_v = net_entrena(x_v);
 %y_est=net_entrena(x_test);
 %y = sim(net, p);
 rmse_e=sum((y_e-t_e).^2)/length(t_e)
 rmse_v=sum((y_v-t_v).^2)/length(t_v)
 
 k_e=1:1:length(t_e);
 figure(1)
 plot(k_e,t_e,k_e,y_e)
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 ylabel('Valor Promedio Casa en USA en miles de dolares')
 legend('Valor promedio Casa','Valor promedio predicho Casa por la Red Neuronal')
 
 k_v=1:1:length(t_v);
 figure(2)
 plot(k_v,t_v,k_v,y_v)
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
 x=data_vinos_2clases(:,1:2)';
 t=data_vinos_2clases(:,14)';
 
 net=newff(x,t,20);%20 neuronas en la capa oculta
 net = train(net,x,t);
 y_old = sim(net, x);
 
 k=1:1:length(t);
 figure(3)
 plot(k,t,k,y_old)
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')

 