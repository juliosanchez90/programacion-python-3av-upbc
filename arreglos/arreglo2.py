#julio cesar sanchez saavedra #130232
# Solicitar al usuario que ingrese 5 números
numeros = []
for i in range(0,5):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Encontrar el valor máximo y mínimo del arreglo
n_maximo = max(numeros)
n_minimo = min(numeros)

# Mostrar los resultados
print(f"El valor máximo es: {n_maximo}")
print(f"El valor mínimo es: {n_minimo}")
