#julio cesar sanchez saavedra 130232

# Solicitar al usuario que ingrese 6 números
numeros = []
for i in range(0,6):
    numero = float(input(f"Ingrese el numero {i+1}: "))
    numeros.append(numero)

# Comprobar si el arreglo está ordenado de menor a mayor
ordenado = numeros == sorted(numeros)

# Mostrar el resultado
if ordenado:
    print("El arreglo esta ordenado de menor a mayor.")
else:
    print("El arreglo no esta ordenado de menor a mayor.")
