# En python no se especifican los tipos de variables.
# Función con dos argumentos.
def sumar(primerNumero, segundoNumero):
	return primerNumero + segundoNumero

# LLamada de la función.
print("La sumatoria es", sumar(1, 3))

# Sintaxis de una Lista (Contiene textos)
Lista = ["Lucas", "Alex", "Masucco", "Cave", "Erick", "Silvio"]

# Mostrar la lista completa [:]
# Mostrar la lista en intervalos [0:2] (equivale a [:2])
# Mostrar la lista en la posición 4 (equivale a [-2] -> 6-2)
# Mostrar la lista desde la posición 2 [2:]
print(Lista[:], Lista[0:2], Lista[:2], Lista[4], Lista[-2], Lista[2:])

# Agregar un nuevo elemento.
Lista.append("El Bicho")
print(Lista[:])

# Agregar un nuevo elemento en una posición.
Lista.insert(2, "Pene")
print(Lista[:])

# Concatenar (unir) dos Listas.
# También se puede usar SegundaLista += Lista
SegundaLista = ["Concha", "Teta"]
Lista.extend(SegundaLista)
print(Lista[:])

# Obtener la posición de "Erick".
print(Lista.index("Erick"))

# Muestra bool si "Erick" existe.
print("Erick" in Lista)

# Elimina a "Cave" de la Lista.
Lista.remove("Cave")
print(Lista[:])

# Muestra el último elemento.
print(Lista.pop())

# Puede tener bools, números, floats y strings.
TerceraLista = [True, 10, -10, 10.5, "Hola"]
print(TerceraLista[:])

# Repite la lista 3 veces.
print(Lista * 3)

# Mostrar cuantos elementos tiene.
print(len(Lista))