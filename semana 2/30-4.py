#Invertir un número de tres dígitos: Elaboraremos un algoritmo para invertir un
#número almacenado en una variable A. Por ejemplo, si ingresamos 834, el
#programa debe dar como salida 438. El dato ingresado debe estar en un rango
#de 1 a 999.
try:
    A=int(input("Ingrese un número (de 1 a 999): "))
    if A>0 and A<999:
        centenas=A%100
        decenas=centenas//10
        unidad=A//100
        centenas2=centenas%10
        print(f"el numero invertido es:{centenas2}{decenas}{unidad}")
    else:
        print("numero fuera de rango")
except ValueError: 
    print("solo numeros enteros")
    exit()
