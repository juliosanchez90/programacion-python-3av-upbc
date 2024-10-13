#julio cesar sanchez saavedra 130232
#Escribe un programa que inicie mostrando en pantalla la letra de “Un
#elefante se columpiaba” iniciando con el número 1, después pregunta al
#usuario cuantos elefantes más se columpiarán y debe responder un
#número más al mostrado. En caso de ingresar un número diferente, pedirle
#que intente de nuevo y repetir el ciclo hasta tener 10 elefantes.
print("los elefantes que se columpiaban")

contador=1
contador2=3
print(" un elefante se columpiaba")
while contador<10:
    r=int(input("que mas sigue?: "))
    try:
        if r>contador and r<contador2:
            print(f"{r} elefantes SE columpiaban")
            contador+=1
            contador2+=1
        else:
            print("intenta otra vez")    
    except ValueError:
        print("entrada no valida")
print("fin del ciclo")                