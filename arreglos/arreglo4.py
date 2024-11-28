# julio cesar sanchjez saavedra 130232
# Solicitar al usuario que ingrese 5 letras
letras = []
for i in range(0,5):
    letra = input(f"Ingrese la letra {i+1}: ")
    letras.append(letra)

# Solicitar al usuario que ingrese una letra a buscar
buscar = input("Ingrese la letra a buscar: ")

# Contar cuántas veces aparece la letra en el arreglo
contador = letras.count(buscar)

# Mostrar el resultado
print(f"La letra '{buscar}' aparece {contador} veces en el arreglo.")
