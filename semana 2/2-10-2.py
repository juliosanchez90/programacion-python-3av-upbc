#julio cesar sanchez saavedra 130232
#en python Crear un programa que pida al usuario los tres lados de un triángulo y
# determine si es equilátero, isósceles o escaleno.
try:
    print("Tipo de triangulo")
    a=(float(input("ingrese el primer  lado de su triangulo:")))
    b=(float(input("ingrese el segundo lado de su triangulo:")))
    c=(float(input("ingrese el tercer lado de su  triangulo:")))
    if a==b and b==c :
        print("este triangulo es: equilatero")
    elif a == b or a == c or b == c:  
        print("este triangulo es: isoceles")
    else:
        print("este triangulo es:escaleno")      
except ValueError:
    print("medida de lado no valida")
    exit