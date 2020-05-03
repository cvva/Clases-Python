# programa que pida el la cantidad de numeros
# a ingresar y calcular cuantos son pares e impares
c, pares, impares = 1, 0, 0
n = int(input("¿Cuantos numeros deseas ingresar ? : "))
while c <= n:
    a = int(input(f"Ingrese {c} numero : "))
    if a % 2 == 0:
        pares += 1
    else:
        impares += 1
    c += 1
print(f"Pares ingresados son :{pares}")
print(f"Impares ingresados son :{impares}")
