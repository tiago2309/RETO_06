def numeros_impares():
    num = 1
    while num <= 1000:
        print(num)
        num += 2

def numeros_pares():
    num = 2
    while num <= 1000:
        print(num)
        num += 2

if __name__ == "__main__":
    print("Pares del 1 al 1000")
    numeros_pares()
    print("Impares del 1 al 1000")
    numeros_impares()
