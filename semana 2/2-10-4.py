#julio cesar sanchez saavedra 130232
# Suponiendo que se ingresa una vocal por teclado, realice un algoritmo
# para determinar si es abierta o cerrada.
v=(input("intgrese una vocal: "))
if v=="a" or v=="e" or v=="o":
    print(f"la vocal {v} es cerrada.")
elif v=="i" or v=="u":
    print(f"la vocal {v} es abierta. ")
else:
    print(f"La entrada {v} no es una vocal.")

    

