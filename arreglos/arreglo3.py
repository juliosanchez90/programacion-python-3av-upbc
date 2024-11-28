# julio cesar sanchez saavedra 130232

# Solicitar al usuario que ingrese 5 números
numeros = []
for i in range(0,5):
    numero = float(input(f"Ingrese el numero {i+1}: "))
    numeros.append(numero)

# Invertir el orden de los elementos en el arreglo
n_invertidos = numeros[::-1]

# Mostrar el resultado
print("Números en orden inverso:")
for numero in n_invertidos:
    print(numero)
