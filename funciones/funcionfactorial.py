def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado=resultado* i
    return resultado

entrada=(int(input("que numero factorial quiere calcular?: ")))

factorial1=factorial(entrada)
print(f"{factorial1}")

