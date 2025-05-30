def es_primo(n):
    if n < 2: 
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

def numeros_primos():
    print("Numeros primos del 1 al 100:")
    for i in range(1, 100):
        if es_primo(i):
            print(i)
    print()

if __name__ == "__main__":
    numeros_primos()