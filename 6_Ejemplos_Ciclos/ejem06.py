# Instruccion repetitivas - uso con listas
num = [1, 3, 5, 7, 9, 11, 13, 15]
print("Recorrer la lista con While")
i = 0
while i < len(num):
    print(num[i], end=' - ')
    i += 1
print("Recorrer la lista con For")
for item in num:
    print(item)

for x in "Aprendiendo Python":
    print(x)
