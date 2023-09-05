
n1 = int(input("Ingrese el numero: "))

def multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(str(numero) + " x " + str(i) + " = " + str(resultado))

multiplicar(n1)