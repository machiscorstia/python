"""
	Una función es recursiva cuando se puede llamar a si misma dentro de su código.

	Como ejemplo, el factorial de un número:
	!3 = 3 * 2 * 1
	!2 = 2 * 1

	Redefiniendo:
	!3 = 3 * !2

"""


def Factorial(Numero):
	print("Calculando el factorial de ", Numero)

	if Numero == 0 or Numero == 1:
		Resultado = 1
		print("1. Devolviendo %d" %Resultado)
		return Resultado
	else: # Para cualquier otro número usa recursividad.
		# Coloca el resultado en una variable
		Resultado = Numero * Factorial(Numero - 1)
		print("2. Devolviendo %d" %Resultado)
		return Resultado

print(Factorial(4))
