def Dividir():
	try:

		primerNumero = float(input("Escribe el primer número:"))
		segundoNumero = float(input("Escribe el segundo número:"))
		print("La división es: " + str(primerNumero/segundoNumero))

	except ValueError:
		print("No escribas otro valor que no sea decimal.")

	except ZeroDivisionError:
		print("No se puede dividir entre 0")

	finally:
		print("Terminó el calculo")

# finally siempre se ejecutará aunque se haya encontrado una excepción.

Dividir()