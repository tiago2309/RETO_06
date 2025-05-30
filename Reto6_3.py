def numeros_pares_descendentes(n):
    if n % 2 != 0:
        n -= 1
    while n >= 2:
        print(n)
        n -=2
    print()

if __name__ == "__main__":
    n = int(input("Ingrese un número natural mayor o igual a 2: "))
    numeros_pares_descendentes(n)