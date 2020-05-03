# instrucciones repetitivas - while - for
# listas anidadas
persona = [
    ["Jose", "Jimenez", 22, "M"],
    ["Juan", "Samaniego", 20, "M"],
    ["Bryam", "Adauto", 24, "M"],
    ["Solansh", "Ventura", 24, "F"]
]
print("Recorrer lista anidada con While")
print("================================")
i = 0
while i < len(persona):
    print(f"Recorrido de {i+1} fila")
    print("_________________________")
    j = 0
    while j < len(persona):
        print(persona[i][j])
        j += 1
    i += 1
print("Recorrer lista anidada con For")
print("================================")
for i in persona:
    print(f"Recorrido de {persona.index(i)+1} fila")
    print("_________________________")
    for j in range(len(persona)):
        print(i[j])
