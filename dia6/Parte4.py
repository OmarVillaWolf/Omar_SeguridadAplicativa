dicc = {
"Alo":"7", 
"Najarro":"8", 
"Meraz":"9", 
"Esperanza":"7", 
"Puebla":"7", 
"Arco":"9", 
"Brazil":"8", 
"Sotomayor":"6", 
"Ortis":"5", 
"Arcos":"7", 
"Borja":"5", 
"Guerrero":"5", 
"Bermejo":"6", 
"Garcia":"7", 
"Ortiz":"8", 
"Mar":"9", 
"Monica":"7", 
"Verdugo":"7", 
"Rossel":"9", 
"Lagunas":"10", 
"Rosado":"10", 
"Pulido":"6", 
"Alvarado":"7", 
"Vea":"8", 
"Lozano":"9", 
"Godinez":"6", 
"Herran":"5", 
"Rengifo":"6", 
"Brizuela":"7", 
"Berlanga":"1"
} 
 
def promedio(c):
    cont = len(c)
    suma = 0
    for i in c:
        suma = suma + int(c[i])
    return suma / cont

print("El promedio es: ", promedio(dicc))
Re = promedio(dicc)

def menor(r):
    for i in r:
        if int(r[i]) < Re:
            print(i)


def mayor(m):
    for i in m:
        if int(m[i]) > Re:
            print(i)

print(' ')
print("Personas con calificación menor al promedio")          
menor(dicc)
print(' ')
print("Personas con calificación mayor al promedio")          
mayor(dicc)