#julio cesar sanchez saavedra 130232
#Encontrar el mayor entre tres números: Dadas tres variables enteras num1,
#num2 y num3, debemos encontrar el número más grande entre ellos y
#almacenarlo en una variable entera llamada max.
print("cual sera el valor mas grande?")
try:
    num1=(int(input("ingrese el primer numero")))
except ValueError:
    print("valor no valido")
try:
    num2=(int(input("ingrese el segundo numero")))
except ValueError:
    print("valor no valido")
try:
    num3=(int(input("ingrese el tercer numero")))
except ValueError:
    print("valor no valido")
if num1>num2 and num1>num3: # la palabra "and y or" son reservadas 
    print(f"el numero mayor es {num1} ")
else:
    if num2>num1 and num2>num3:
        print(f"el numero mayor es {num2}")
    else:
        if num3>num1 and num3>num2:
            print(f"el numero {num3} el es mayor")
        

