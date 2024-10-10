#julio cesar sanchez saavedra 130232
#Contar dígitos en un número: Dado un número entero positivo, 
#cuenta cuántos dígitos tiene. Por ejemplo, si el número es 12345, 
# la respuesta sería 5.Sé que el problema 4 no se hace con ciclo for, 
# pero me parece interesante para que aprendan algo nuevo.
try:
    n=(int(input("ingresa un numero entero positivo: ")))
    if n>0:
        n2=str(n)
        digitos=len(n2)
        print(f"la cantidad de digitos que tiene {n2} son : {digitos}")
    else:
        print("el numero tiene que ser possitivo")    
except ValueError:
    print("la entrada no es numero entero positivo")
    exit()