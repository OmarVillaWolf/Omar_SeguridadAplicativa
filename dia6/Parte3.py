for i in range (1, 101):
    prim = 0
    for cont2 in range (1, 101):
        if((i % cont2) == 0):
            prim = prim + 1
    if(prim == 2):
        print(i)
        
print("Obtener los primeros 100 numeros primos: ")