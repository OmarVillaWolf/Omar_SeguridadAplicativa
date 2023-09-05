def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingresa un numero: "))
if es_primo(num):
    print("Es primo")
else:
    print("No es primo")