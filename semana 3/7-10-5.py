#julio cesar sanchez saavedra 130232
# Secuencia de Fibonacci: Genera los primeros N términos de la secuencia de Fibonacci.
# La secuencia comienza con 0 y 1, y cada término posterior es la suma de los dos términos anteriores.
# Por ejemplo, si N es 8, la secuencia sería: 0, 1, 1, 2, 3, 5, 8, 13.
try:
    nf=(int(input("ingresa un numero entero positivo(serie fibonaci)")))
    if nf>0:
        n=0
        n1=1
        r=0
        print(f"{n} {n1} ", end=" ")
        for nf in range(n,nf):
            r=n+n1
            n=n1
            n1=r
            print(f" {r}", end=" ")
    else:
        print("el numeri tiene que ser positivo")        
except ValueError:
    print("entrada no valida")
