clear all;clc;
%Regresion Logistica para p(y(x))=p(x1,x2)=1/(1+exp(-(b0*1+b1*x1+b2*x2))
load ('data_ej2');  
x1=data_ej2(:,1);
x2=data_ej2(:,2);
p=data_ej2(:,3);

figure(1)
plot(x1,x2,'ob')
xlabel('x1')
ylabel('x2')
%scatter(x1,x2)
xlabel('x1')
ylabel('x2')
%En forma más compacta y eficiente

b=[0 0 0]';gamma=0.3
x_reg=[ones(size(x1,1),1) x1 x2];

for j=1:3  % 3 pasadas por toda la data de entrenamiento=>30 iteraciones
    
for k=1:length(p)
y_est=b(1)*1+b(2)*x1(k)+b(3)*x2(k);
p_pred=1/(1+exp(-y_est));
b=b+gamma*(p(k)-p_pred)*p_pred*(1-p_pred)*x_reg(k,:)';
end

end

%*** Valores finales de las funciones (y_est y p_pred=Funcion Logistica
y_est_final=b(1)+b(2)*x1+b(3)*x2;
p_pred_final=1./(1+exp(-y_est_final))

for k=1:length(p)
    if p_pred_final(k)<0.5
        p_pred_clase(k)=0;
    else
        p_pred_clase(k)=1;
    end
end
p_pred_clase=p_pred_clase'
%****Recta de separación
%X2=-b0/b2-b1/b2*X1
%*************************************************************************
e_bin_porcentual=sum(abs(p-p_pred_clase))/length(p)*100
