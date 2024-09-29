# julio cesar sanchez saavedra 130232
#Escribir un programa que pida al usuario su peso (en kg) y
# estatura (en metros), calcule el índice de masa corporal y lo
# almacene en una variable, y muestre por pantalla la frase:
# a. Tu índice de masa corporal es <imc>, donde <imc> es el
# índice de masa corporal calculado redondeado con dosdecimales.
print("calculadora de <imc> indice de masa corporal")
peso=(float(input("untroduca su peso en KG: ")))
altura=(float(input("ingrese su altura en metros: ")))
imc=(peso/(altura*altura))
print(f"su indice de masa corporal es : {imc:.2f} IMC")