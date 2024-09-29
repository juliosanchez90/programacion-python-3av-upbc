#julio cesar sanchez saavedra 130232
print("vamos a calcular el area y perimetro de un triangulo")
base=(float(input("ingrese la base del triangulo ")))
altura=(float(input("ingrese l altura del triangulo ")))
hip=((base**2 + altura**2)**.5) # ** es potencia
area=(base*altura)/2
perimetro=(altura+base+hip)
print(f"la area es {area:.2f} y el perimetro es {perimetro:.2f}")