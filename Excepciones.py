# Las excepciones son errores que ocurren durante la ejecución del programa.
# El código aunque esté bien le puede suceder algo inesperado durante la ejecución.

def sumar(primerNumero, segundoNumero):
	return primerNumero + segundoNumero

def restar(primerNumero, segundoNumero):
	return primerNumero + segundoNumero


while True:
	try:
		pNumero = int(input("Introduce el primer numero"))
		sNumerro = int(input("Introduce el segundo numero"))
		break;
	except ValueError:
		print("No ingreses otro valor que no sea númerico.") 