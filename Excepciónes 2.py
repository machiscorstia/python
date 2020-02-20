import math

def calcularRaiz(numero):
	if numero < 0:
		raise ValueError("No se permiten números negativos")
	else:
		return math.sqrt(numero)

Numero = int(input("Escribe el número:"))

try:
	print(calcularRaiz(Numero))
except ValueError as errorNumeroNegativo:
	print(errorNumeroNegativo)