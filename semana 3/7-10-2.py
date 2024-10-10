#julio cesar sanchez saavedra 130232
#Factorial de un número: Dado un número entero no negativo n, 
# calcula su factorial (el producto de todos los enteros positivos desde 1 hasta n).
#  Por ejemplo, el factorial de 5 es 5! = 5 × 4 × 3 × 2 × 1.
try:
    n=(int(input("ingrese numero entero positivo / factorial: ")))
    signo=0
    nx=n
    n2=1
    print(f"el factorial de {n}!")
    if n>=0 :
        for n in range(n,0,-1):
            print(f"{n}", end="")
            n2=n2*n

            if signo<nx-1:
                print("x",end="")
                signo=signo+1
        print(f"={n2}")
    else:
        print("nomero no valido")
except ValueError:
    print("entrada no valida")
    exit()        



