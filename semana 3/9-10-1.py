#julio cesar sanchez saavedra 
#Realiza un programa que pida números mientras no se ingrese uno
# negativo. Al final, se debe mostrar la suma de los números ingresados.
print("suma de numeros positvios")
total=0
while True:
    num=(int(input("ingrese numero: ")))
    if num<0:
        print("el numero es negativo, se cerrara el programa")
        break
    else:
        total+=num
print(f"la suma de los numeros ingresado es: {total}")
