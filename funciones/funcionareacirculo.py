#julio cesar sanchez saavedra #130232
def area_circulo(r):
    area=(3.1416*r*r)
    return area


entrada=(int(input("ingresa el radio del circulo:")))
area=area_circulo(entrada)
print(f"{area:.2f}")
