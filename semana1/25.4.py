#julio cesar sanchez saavedra 130232
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla:
# a. La <n> entre <m> da un cociente <c> y un resto <r>.
# b. Donde <n> y <m> son los números introducidos por el usuario.
# c. Y <c> y <r> son el cociente y el resto de la división entera respectivamente.
print("ingresen dos números enteros")
n=( input("ingrese primer numero entero: "))
m=( input("ingrese segundo numero entero: "))
div=str(int(n)//int(m)) #se agrega str porque no se difinio el tipo de variable, 
# el imput esta en cadena de caracteres lo pasara a int.
# el "//" es divicion entera
residuo=str(int(n)%int(m)) # es para mostar el residuo
print(f"el modulo de la divicion n/m es {div}")
print(f"el reiduo de la divicion n/m es {residuo}")
