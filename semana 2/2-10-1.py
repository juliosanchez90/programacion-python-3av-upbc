#julio cesar sanchez saavedra 130232
#Categorización de edades:Problema 1: Crear un programa que pida al usuario su edad y 
# le indique a qué grupo etario pertenece. Puedes definir tus propios rangos de edad.
#  Infancia (0 a 6 años),Niñez (6 a 12 años), Adolescencia (12 a 20 años), Juventud (20 a 25 años)
#  Adultez (25 a 60 años),Ancianidad (60 años en adelante)
try:
    print("Categorización de edades ")
    edad=(int(input("ingrese la edad del cliente:")))
    if edad>=0 and edad<6:
        print("el cleinte esta en el grupo de: infancia")
    elif edad>=6 and edad<12 :
        print("el cliente esta en el grupo de: niñez")
    elif edad>=12 and edad<20 : 
        print("el cliente esta en el grupo de:Adolesencia")
    elif edad>20 and edad<=25 : 
        print("el cliente esta en el grupo de:juventud")
    elif edad>25 and edad<=60 : 
        print("el cliente esta en el grupo de:adultez")
    else: 
        print("el cliente esta en el grupo de: ancianidad")            
except ValueError:
    print("edad no valida")
    exit()