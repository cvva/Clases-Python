# listas o arreglos
letras = ["a", "e", "i", "o", "u"]
print(letras)
# print(letras[4])
# print(letras[-1])
# print(letras[-2])
# print(len(letras))
letras.append("ae")
print(letras)
letras.remove(letras[-3])
print(letras)
# listas anidadas
persona = [
    ["Cesar", 17, True],
    ["Luis", 17, True],
    ["Jeanpier", 18, False]
]
print(persona)
print(persona[0][1])
print(persona[2][0])
print(persona[2][-2])
persona.append(["Josue", 19, False])
print(persona)
