"""# la trimple comida invalida el codigo de  uchas lineas.
def sumar_cinco_numeros(a, b, c, d, e):
    suma=a+b+c+d+e
    return suma

# ejemplo de uso
resultado= sumar_cinco_numeros(2,3,4,5,8)
print("la suma es :", resultado)

def promedio(resultado):
    prom=resultado/5
    return prom

promedioRes=promedio(resultado)
print(f"el primedio es : {promedioRes:.2f}")
"""
######### para llamar una funcion
from funcionEst import imprime #aqui exporta una funcion de del archivo "funcionEst"
name=input("ingresa tu nombre: ")
nombre=imprime(name)
