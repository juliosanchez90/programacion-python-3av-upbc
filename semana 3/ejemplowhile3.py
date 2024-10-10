#juego de adivinanza con ciclo while
numero_secreto=65
intentos=0
print("!BIENVENIDO AL JUEGO DE ADUVINANZA!")
print("Tienes que adivinar el numero secreto entre el 1 y 100")

while True: # la condicion 'True' significa que el ciclo se repetira hasta que se encuentre un break
    try:
        guess=int(input("ingresa tu intento: "))
        intentos+=1
        if guess == numero_secreto:
            print(f"!felicidades! adivinaste el numero en {intentos} intentos. ")
            break
        elif guess<numero_secreto:
            print("el numero secreto es mayor. sigue intentando")
        else:
            print("el numero secreto es menor. sigue intentando")
    except ValueError:
        print("Error: ingresa un numero valido")
print("gracias ppor jugar")        