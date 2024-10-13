# julio cesar sanchez saavedra 130232
#Crear un programa que permita al usuario ingresar los montos de las
#compras de un cliente (se desconoce la cantidad de datos que cargará, la
#cual puede cambiar en cada ejecución), cortando el ingreso de datos
#cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se
#debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar,
#informar el total a pagar teniendo que cuenta que, si las ventas superan el
#total de $1000, se le debe aplicar un 10% de descuento.
total=0
print("SISTEMA DE PAGO:")
while True:
    try:
        articulo=(float(input("ingrese el costo del articulo: ")))
        if articulo>0:
            total=total+articulo
        elif articulo<0:
            print("monto no valido")
        elif articulo==0:
            break    
    except ValueError:
        print("entrada no valida")
if total>1000:
    descuento=total-(total*.1)
    print(f"el valor total de los articulos es: {descuento} $ con un descuento del 10%")
else:
    print(f"el valor total de los articulos es: {total} $")
            