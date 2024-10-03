print("JUEGO DE REGUNTAS, SI / NO ")
try:
    r1=(input("colon descrubrio america? "))
    if r1=="si":
        print("correcto")
        r2=(input("la independencia de mexico fue en el año 1810? "))
        if r2=="no":
            print("correcto")
            r3=(input("The Doors fue un grupo americano de rock?"))
            if r3=="si":
                print("correcto")
            else:
                print("incorrecto")
                exit()
except ValueError():
    print("solo puede ingresar si o no")
    exit()
