#julio cesar sanchez saavedra 130232
#Determinar si dos números tienen signos opuestos: Escribiremos un
#algoritmo que lea dos números enteros como entrada y muestre el mensaje
#“Signos Opuestos” solo si uno de los números es positivo y el otro es negativo.
try:
    num1=(int(input("ingrese un numero: ")))
    num2=(int(input("ingrese otro numero: ")))
except ValueError:
    print("solo numeros enteros")
    exit()
if num1==0 or num2==0: 
    print("ingrese numeros diferentes de 0 ")
elif num1 < 0 and num2>0 or num2<0 and num1>0:
    print("signos opuestos")
else:
    print("signos iguales")




