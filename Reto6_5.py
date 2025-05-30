def divisores_numero(n):
    print(f"Divisores de {n}:")
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            print(divisor)
        divisor += 1

if __name__ == "__main__":
    n = int(input("Ingrese un numero entre 2 y 50: "))
    if 2 <= n <= 50:
        divisores_numero(n)
    else:
        print("Numero fuera del rango")