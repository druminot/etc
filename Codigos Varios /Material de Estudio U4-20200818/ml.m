clear all;clc;

 load datos_vino
 x=datos_vino(:,1:13)';
 t=datos_vino(:,14)';
%***Entrenamiento con Algoritmo Gradiente Descendente 
 net=newff(x,t,20);
 net = traingd(net,x,t);
 y_est = sim(net, x);
 
 k=1:1:length(t);
 figure(1)
 plot(k,t,k,y_est)
 xlabel('N∞ de la muestra o patrÛn presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1, 2 ,3 )','ClasificaciÛn tipos de Vino (Clase 1 , 2 , 3)')

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
 xlabel('N∞ de la muestra o patrÛn presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1, 2 ,3 )','ClasificaciÛn tipos de Vino (Clase 1 , 2 , 3)')

 %***Entrenamiento con Algoritmo Gradiente Descendente Adaptivo (varÌa el
 %***coeficiente de aprendizaje en cada iteraciÛn
  net=newff(x,t,20);
 net = traingda(net,x,t);
 y_est = sim(net, x);
 
 k=1:1:length(t);
 figure(3)
 plot(k,t,k,y_est)
 xlabel('N∞ de la muestra o patrÛn presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1, 2 ,3 )','ClasificaciÛn tipos de Vino (Clase 1 , 2 , 3)')
 
 umbral=0.5;
 for i=1:1:length(t)
    if y_est(i)>=0.5
        y_est(i)=1;
    else
        y_est(i)=0;   
    end
 end
 e_bin_porcentual=sum(abs(t-y_est))/length(t)*100
 
 figure(4)
 plot(k,t,k,y_est,'o')
 xlabel('N∞ de la muestra o patrÛn presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1, 2 ,3 )','ClasificaciÛn tipos de Vino (Clase 1 , 2 , 3)')
 
 %***Entrenamiento con Algoritmo Levenberg Marquardt
  net=newff(x,t,20);
 net = trainlm(net,x,t);
 y_est = sim(net, x);
 
 k=1:1:length(t);
 figure(5)
 plot(k,t,k,y_est)
 xlabel('N∞ de la muestra o patrÛn presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1, 2 ,3 )','ClasificaciÛn tipos de Vino (Clase 1 , 2 , 3)')

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
 xlabel('N∞ de la muestra o patrÛn presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1, 2 ,3 )','ClasificaciÛn tipos de Vino (Clase 1 , 2 , 3)')

  %***Entrenamiento con Algoritmo backpropagation resiliente
  net=newff(x,t,20);
 net = trainrp(net,x,t);
 y_est = sim(net, x);
 
 k=1:1:length(t);
 figure(7)
 plot(k,t,k,y_est)
 xlabel('N∞ de la muestra o patrÛn presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1, 2 ,3 )','ClasificaciÛn tipos de Vino (Clase 1 , 2 , 3)')

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
 figure(8)
 plot(k,t,k,y_est,'^')
 xlabel('N∞ de la muestra o patrÛn presentado a la red neuronal')
 legend('Tipos de Vino (Clases 1, 2 ,3 )','ClasificaciÛn tipos de Vino (Clase 1 , 2 , 3)')

 
 
 
 
X=datos_vino(:,1:13);
t=datos_vino(:,14);

x1=X(:,1);
x2=X(:,2);

figure(9)
gscatter(x1,x2,t,'br','o^*');
xlabel('x1')
ylabel('x2')


k=3;
[id,C] = kmeans(X,k,'MaxIter',1000);%id indica a que grupo fueron asignadsos
%los centros de los cluster C

figure(10)
gscatter(x1,x2,t,'br','o^*') %Color y luego tipo de figura
xlabel('x1')
ylabel('x2')
hold on
plot(C(1,1),C(1,2),'^c',C(2,1),C(2,2),'oc',C(3,1),C(3,2),'*c')
hold off
