#conversion de tipos
cantidad = int(input("Dígame una cantidad en dolares: "))
print(f"{cantidad} dolares son {round(cantidad * 3.4, 2)} soles")

cantidad = float(input("Dígame una cantidad en soles (hasta con 2 decimales): "))
print(f"{cantidad} soles son {round(cantidad / 3.4)} dolares")
