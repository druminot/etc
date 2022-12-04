clear all;clc;
%***Problema de Clasificación***

 %**********Datos Vino*************
 load data_vinos_2clases
 x=data_vinos_2clases(:,1:13)';
 t=data_vinos_2clases(:,14)';
 
%***Entrenamiento con Algoritmo Gradiente Descendente
 net=newff(x,t,[5,10],{'tansig','logsig'},'traingd');%20 neuronas en la capa oculta
%Por default la capa de salida tiene funcion de activacion "purelin"
 net = train(net,x,t);
 y_est = sim(net, x);
 
 k=1:1:length(t);
 figure(1)
 plot(k,t,k,y_est)
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')

 umbral=0.5;
 for i=1:1:length(t)
    if y_est(i)>=0.5
        y_est(i)=1;
    else
        y_est(i)=0;   
    end
 end
 e_bin_porcentual=sum(abs(t-y_est))/length(t)*100
 
 k=1:1:length(t);
 figure(2)
 plot(k,t,k,y_est,'o')
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')

 %***Entrenamiento con Algoritmo Gradiente Descendente Adaptivo (varía el
 %***coeficiente de aprendizaje en cada iteración
 net=newff(x,t,[5,10],{'tansig','logsig','purelin'},'traingda');%20 neuronas en la capa oculta
 net = train(net,x,t);
 y_est = sim(net, x);
 
 k=1:1:length(t);
 figure(3)
 plot(k,t,k,y_est)
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')
 
 umbral=0.5;
 for i=1:1:length(t)
    if y_est(i)>=0.5
        y_est(i)=1;
    else
        y_est(i)=0;   
    end
 end
 e_bin_porcentual=sum(abs(t-y_est))/length(t)*100
 %Se logra 100% de correcta clasificación
 figure(4)
 plot(k,t,k,y_est,'o')
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')
 
 %***Entrenamiento con Algoritmo Levenberg Marquardt
 net=newff(x,t,[5,10],{'tansig','logsig'},'trainlm');%20 neuronas en la capa oculta
 net = train(net,x,t);
 y_est = sim(net, x);
 
 k=1:1:length(t);
 figure(5)
 plot(k,t,k,y_est)
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')

 umbral=0.5;
 for i=1:1:length(t)
    if y_est(i)>=0.5
        y_est(i)=1;
    else
        y_est(i)=0;   
    end
 end
 e_bin_porcentual=sum(abs(t-y_est))/length(t)*100
 
 k=1:1:length(t);
 figure(6)
 plot(k,t,k,y_est,'^')
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')

 %***Entrenamiento con Algoritmo "correccion de error" para Perceptron
 %***El Perceptron tiene solo 1 Neuron****
 net_p=newp(x,t);%Default is hardlim (1 y 0)
 net_p = train(net_p,x,t);
 y_est = sim(net_p, x);
 
 perform(net_p,t,y_est)

 e_mae=sum(abs(t-y_est))/length(t)*100

 k=1:1:length(t);
 figure(7)
 plot(k,t,k,y_est,'^')
 xlabel('N° de la muestra o patrón presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1 y 0)','Clasificación tipos de Vino (Clase 1 o 0)')

 
