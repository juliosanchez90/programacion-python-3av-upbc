#Calcular la diferencia entre dos enteros positivos: Crearemos un algoritmo
#que reciba dos enteros positivos distintos y calcule la diferencia entre el número
#mayor y el menor. Además, aseguraremos que el programa siempre muestre 6
#como resultado, independientemente del orden de entrada (por ejemplo, tanto
#para 9 y 15 como para 15 y 9).

try:
    n1=(int(input(" introdusca un numero entero positivo  :")))
    n2=(int(input(" introdusca otro numero entero positivo:")))
    if n1<0 or n2<0:
        print("solo numeros enteros positivos")
        exit()
    if n1>n2:
        reusltado=abs(n1-n2)
        print(f"el resultado de {n1} menos {n2} es {reusltado}")
    else:
        reusltado=abs(n2-n1)
        print(f"el resultado de {n2} menos {n1} es {reusltado}")
except ValueError:
    print("solo numero enteros positivos ")
    exit()

        
        

    