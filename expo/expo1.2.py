

while True:
    print("Conversor de Temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")
    opcion = input("Selecciona una opción (1, 2 o 3): ")
    if opcion == '1':
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C es igual a {fahrenheit}°F.")
        
    elif opcion == '2':
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F es igual a {celsius}°C.")
        
    elif opcion == '3':
        print("Saliendo del conversor.")
        break
        
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

