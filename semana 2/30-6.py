#julio cesar sanchez saavedra 130232
# una fruteria  ofrese las manzanas con descuento, (0 - 2)kg 0% de (2.01 a 5)kg 10%
#(5.01 - 10)kg 15% y de 10kg en adelante 20%
# determine cuanto pagara una persona que compre manzanas en esa fruteria
try:
    manzanas=(float(input("cuantos kilos de manzana llevara? ")))
    if manzanas<=0 :
        print("usted indico que no quiere manzanas, vuelva pronto :)")
    if manzanas>0 and manzanas<=2:
        prescio= manzanas*30
        print(f"el pesocio de los {manzanas}kg de manzanas es : {prescio}") 
    if manzanas>=2.01 and manzanas <=5: #10% de descuento
        prescio= manzanas*30
        descuento=prescio-(prescio*.1)
        print(f"el pesocio de los {manzanas}kg de manzanas es : {descuento}")
    if manzanas>=5.01 and manzanas <=10 : #15% descuento
        prescio= manzanas*30
        descuento=prescio-(prescio*.15)
        print(f"el pesocio de los {manzanas}kg de manzanas es : {descuento}")
    if manzanas>10:
        prescio=manzanas*30
        descuento=prescio-(prescio*.2)
        print(f"el pesocio de los {manzanas}kg de manzanas es : {descuento}")
except ValueError:
    print("ingrese solo valores numericos")
    exit()