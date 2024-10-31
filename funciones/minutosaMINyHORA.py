def Horasyminutos(MT):
    horas = MT // 60
    minutos = MT % 60
    return print(f"{horas} horas y {minutos} minutos")


minutostotales=(float(input("ingrese la cantidad de minutos: ")))
horasyminutos=Horasyminutos(minutostotales)
print(f"{horasyminutos}")

