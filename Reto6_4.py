def factorial_numero(n):
    factorial = 1
    while n > 1:
        factorial *= n 
        n -= 1
    return factorial

if __name__ == "__main__":
    n = int(input("Ingrese un número natural: "))
    print(f"El factorial de {n} es: {factorial_numero(n)}")