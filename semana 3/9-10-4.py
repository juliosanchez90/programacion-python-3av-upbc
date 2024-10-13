#julio cesar sanchez saavedra 130232
# Tenemos la pantalla del celular bloqueada. Partiendo de un PIN_SECRETO,
#intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el
#proceso con Python. En caso de acceder, lanza al usuario &#39;login correcto&#39;.
#Sino, &#39;llamando al policía&#39;.
pin_secreto=1234
contador=0
while True:
    intento=(int(input("ingrese pin para desbloquear: ")))
    if intento==pin_secreto:
        print("login corrento !WELCOME!")
        break
    elif intento!=pin_secreto:
        print(f"PIN incorrecto")
        contador+=1
        if contador>=4:
            print("LLAMANDO AL DEPARTAMENTO DE POLICIA")
            break
