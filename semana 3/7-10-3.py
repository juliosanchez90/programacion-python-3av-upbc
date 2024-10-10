#julio cesar sanchez saavedra 130232
#Tabla de multiplicar: Dado un número entero x, imprime la tabla de multiplicar para ese 
# número hasta un cierto límite (por ejemplo, las primeras 10 multiplicaciones).
#  Por ejemplo, si x es 7, mostraría:7 × 1 = 7,7 × 2 = 14 …7 × 10 = 70
try:
    n=(int(input("ingrese numero entero positivo / multiplicasion: ")))
    print(f"la tabla de multiplicar del 1 a al de{n} es:")
    if n>=0 :
        for multi in range(1,11):
            print(f"{n} x {multi}", end="")
            n2=n*multi
            print(f" = {n2}")   
    else:
        print("nomero no valido")
except ValueError:
    print("entrada no valida")
    exit()        


