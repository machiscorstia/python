def Adivinar(maxIntentos, Numero):
	Respuesta = int(input("Adivina el número: "))

	if Respuesta == Numero:
		print("Bien adivinaste.")
	else:
		if maxIntentos > 1:
			print("No, pelotudo.")
			Adivinar(maxIntentos - 1, Numero)
		else:
			print("Ya no tenes intentos.")

Adivinar(3, 10)
