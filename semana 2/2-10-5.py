#julio cesar sanchez saavedra 130232
#En la Ponduka State University, los veteranos sólo pagan $30 (dólares)
# por asignatura mientras que los demás (regulares) pagan $50 por asignatura. Escriba
# un algoritmo en el que el usuario introduce los datos del estudiante (Vet o Reg) y el
# número de asignaturas. La salida debe indicar si el estudiante es de la categoría
# veterano o regular e indicar el número de materias y los costos de la colegiatura.

print(" PONDUKA STATE UNIVERSITY ")
nombre=(str(input("ingrese el nombre del estudiante: ")))
rango=(str(input("ingrese el rango del estudiante: ")))
materias=(int(input("ingrese numero de materias: ")))
if rango=="veterano":
    cuota=materias*30
    print(f" estudiante: {nombre} / rango:{rango} / costo de inscripcion ${cuota} dolares")
else:
    cuota=materias*50
    print(f" estudiante: {nombre} / rango:{rango} / costo de inscripcion ${cuota} dolares")
    

