print("Adivina el número que estoy pensando.")
num=input("Introduce un número entre el 1 y el 10: ")
if ((n < 1) || (n > 100)):
    print("El número introducido debe estar en el intervalo 1 - 10.")
    num=input("Introduce un número entre el 1 y el 10: ")
if (n == 7):
    print("¡Enhorabuena!, ¡has acertado!")
else:
    print("Lo siento, ese no es el número que estoy pensando.")
