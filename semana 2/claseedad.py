# julio cesar sanchez saavedra 130232
#print("programa que solicitita la edad de un usuario y este imprimira si es o no mayor.")
#pedimos al usuario que ingrese su edad
try: #el try: deve ir con el except Valueerror: mas el exit(), el exit() es oara que se cierre
    edad=int(input("por favor, ingrese su edad: "))
except ValueError:
    print("debes ingresar un numero valido (mayor a 0).")
    exit()
#verificamos si la edad dela persona es mayor
if edad >=18: # nota el if y else terminan con ":"
    print("eres mayor de edad. !puedes votar y conducir!")
else:
    print("eres menor de edad, aun no puedes votar ni conducir.")
    