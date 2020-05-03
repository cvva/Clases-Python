#* Sentencia múltiple (switch)

mes=int(input("Por favor, introduzca un numero de mes: "))
def switch_demo(argument):
    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Setiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Dciembre"
    }
    return switcher.get(argument, "Mes invalido")

#print("Mes " + mes + ": " + nombreDelMes)
print("Mes "+repr(mes) +": " +switch_demo(mes))
