#julio cesar sanchez saavedra 130232
#Leer 10 números e imprimir cuantos son positivos, cuantos negativos y
#cuantos cero.
contador=0
contadorp=0
contadorn=0
print("contador de numeros")
while contador<10:
    try:
        num=(float(input("INGRESE UN NUMERO: ")))
        if num>=0:
            contadorp+=1
            contador+=1
        else:
            contadorn+=1
            contador+=1
    except ValueError:
        print("numero no valido")        
print(f"nos numeros positivos fueron: {contadorp} y los numero negativos fueron: {contadorn}")        
