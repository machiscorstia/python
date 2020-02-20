# Generador

# Es más eficiente que una función tradicional.
# Es útil con listas de valores infinitos.

# Función tradicional
def obtenerNumeroPar(limite):
	Numero = 1
	Lista = []
	while Numero <= limite:
		Lista.append(Numero * 2)
		Numero += 1
	return Lista

print(obtenerNumeroPar(10))

# Generador.

def generarNumeroPar(limite):
	Numero = 1
	while Numero <= limite:
		yield Numero * 2
		Numero += 1

numerosPares = generarNumeroPar(10)

for i in numerosPares:
	print(i, end = " ")

# El geneador entra en un estado Standby.
