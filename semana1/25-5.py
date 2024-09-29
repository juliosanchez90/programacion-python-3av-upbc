#julio sanchez saavedra 130232
# Una juguetería tiene mucho éxito en dos de sus productos:
# payasos y muñecas. Suele hacer venta por correo y la empresa de logística 
# les cobra por peso de cada paquete así que deben calcular el peso 
# de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca75g.
# a. Escribir un programa que lea el número de payasos y muñecas vendidos en el último 
# pedido y calcule el peso total del paquete que será enviado. 
# b. ¿Cuánto se cobrará de envío, si la paquetería cobra 120 pesos por cada 600g?
print("calculadora de productos payasos/muñecas")
payaso=(float(input("ingrese las unidades a vender del jugete payaso: ")))
muñeca=(float(input("ingrese las unidades a vender del jugete Muñeca: ")))
pp=112
pm=75
peso=((muñeca*pm)+(payaso*pp))
costo=(peso/600)*(120)
print(f"el peso total de los productos payaso x {payaso} y muñeca x {muñeca} = {peso} gramos ")
print(f"el costo de envio por {peso} gramos es : {costo} pesos$")