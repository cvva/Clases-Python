# funcion con retorno de valor
def doble(numero):
    return numero*2


num = int(input("Ingrese un número : "))
num2 = doble(num)
print(f"el doble de {num} es {num2}")
print(doble(doble(doble(num))))
