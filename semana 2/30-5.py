#julio cesar sanchez saavedra 130232
#en un  juego de preguntas se responde si y no gana quien responda correctamente las 3 preguntas .
#si responde mal mal cualquiera de ellas ya no se pregunta la siguiente y termina el juego
#las preguntas son: colon descrubrio america?
#la independencia de mexico fue en el año 1810?
# The Doors fue un grupo americano de rock?
print("JUEGO DE REGUNTAS, SI / NO ")
try:
    r1=(input("colon descrubrio america? "))
    if r1=="si":
        print("correcto")
    else: 
        print("incorrecto")
        exit()
        
    r2=(input("la independencia de mexico fue en el año 1810? "))
    if r2=="no":
        print("correcto")
    else:
        print("incorrecto")
        exit()
  
    r3=(input("The Doors fue un grupo americano de rock?"))
    if r3=="si":
        print("correcto")
    else:
        print("incorrecto")
        exit()
        
except ValueError():
    print("solo puede ingresar si o no")
    exit()
