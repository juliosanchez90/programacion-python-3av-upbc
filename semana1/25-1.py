#julio cesar sanchez saavedra 130232
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
#a. Después debe mostrar por pantalla la paga que le corresponde.
print("calculadora de sueldo.")
sueldo=(float(input("ingrese su sueldo por hora: ")))
horas=(float(input("ingrese horas trabajadas a la semana: ")))
sueldot= sueldo*horas
print(f"su sueldo semanal seria: {sueldot:.2f}")