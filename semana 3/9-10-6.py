# julio cesar sanchez saavedra 130232
#Realice un programa que calcule todas las ordenadas pares de la función
#Y=f(x)= x *x*x+1, debe imprimir la abscisa y la ordenada para los valores
#comprendidos entre 0 y 30.
contador=0
x=0
# x=absisa
# y= ordenada
while contador<31:
   y=(x*x*x)+1
   print(f" x= {x} y= {y}")
   contador+=1
   x+=1
    