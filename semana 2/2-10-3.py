#julio cesar sanchez saavedra
# Crear una calculadora simple que realice operaciones básicas (suma,resta, multiplicación y división)
#  de acuerdo con la elección del usuario. Después le
# solicitará al usuario 2 números para realizar la operación seleccionada.
print("CALCULADORA BASICA")
try:
    print("indiquen la operacion deseada:")
    respuesta=(int(input("1-suma, 2-resta, 3-multiplicacion, 4- divicion: ")))
    if respuesta==1:
        n1=(float(input("ingrese primer valor: ")))
        n2=(float(input("ingrese segundo valor: ")))
        r=n1+n2
        print(f"{n1}+{n2}={r:.2f}")
    elif respuesta==2:
        n1=(float(input("ingrese primer valor: ")))
        n2=(float(input("ingrese segundo valor: ")))
        r=n1-n2
        print(f"{n1}-{n2}={r:.2f}")
    elif respuesta==3:
        n1=(float(input("ingrese primer valor: ")))
        n2=(float(input("ingrese segundo valor: ")))
        r=n1*n2
        print(f"{n1}x{n2}={r:.2f}")
    elif respuesta==4:
        n1=(float(input("ingrese primer valor: ")))
        n2=(float(input("ingrese segundo valor: ")))
        r=n1/n2
        print(f"{n1}/{n2}={r:.2f}")
    else:
        print("entrada no valida")    
except ValueError:
    print("entrada no valida")
    exit()    





