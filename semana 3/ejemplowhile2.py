#ejeplo del ciclo while con entrada del usuario,pedira y sumara los numeros mientas
#no ingrese la palabra fin.
total=0
while True: #mientras no se encuentre un "Break" el ciclo while seguira ejecutandose
    try:
        numero= input("ingresa un numero (o escribe la palabra 'fin'para terminar)")
        if numero.lower()=="fin": #".lower" combierte las letras a minustculas
            break
        numero=int(numero)
        total+=numero# "total+=numero es igual a total=total+1"
    except ValueError:
        print("Error: ingresa un numero valido o escribe 'fin' para terminar")
print(f"la suma total es: {total}")        
