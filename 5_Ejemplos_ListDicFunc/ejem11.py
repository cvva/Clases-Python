def calcular(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma+lista[x]

    return suma


milista = [9, 5, 6, 1, 4, 12]
sum = calcular(milista)
print("La suma de la lista es : ", sum)
