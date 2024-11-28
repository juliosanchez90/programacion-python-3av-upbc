# julio cesar sanchez saavedra 130232
# Solicitar al usuario que ingrese 5 palabras
palabras = []
for i in range(0,5):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)

# Ordenar el arreglo alfabeticamente
palabras.sort()

# Mostrar el resultado
print("Palabras ordenadas alfabeticamente:")
for palabra in palabras:
    print(palabra)