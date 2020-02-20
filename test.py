# En python no se especifican los tipos de variables.
# Función con dos argumentos.
def sumar(primerNumero, segundoNumero):
	return primerNumero + segundoNumero

# LLamada de la función.
print("La sumatoria es", sumar(1, 3))

# Array/lista con textos/strings.
Lista = ["Lucas", "Alex", "Masucco", "Cave", "Erick", "Silvio"]

# Mostrar la lista completa [:]
# Mostrar la lista en intervalos [0:2] (equivale a [:2])
# Mostrar la lista en la posición 4 (equivale a [-2] -> 6-2)
# Mostrar la lista desde la posición 2 [2:]
print(Lista[:], Lista[0:2], Lista[:2], Lista[4], Lista[-2], Lista[2:])

# Agregar un nuevo elemento a la Lista.
Lista.append("El Bicho")
print(Lista[:])

# Agregar un nuevo elemento a la Lista en una posición.
Lista.insert(2, "Pene")
print(Lista[:])

# Concatenar (unir) dos listas.
# También se puede usar SegundaLista += Lista
SegundaLista = ["Concha", "Teta"]
Lista.extend(SegundaLista)
print(Lista[:])

# Obtener la posición de "Erick" en la lista.
print(Lista.index("Erick"))

# Muestra bool si "Erick" se encuentra en la lista.
print("Erick" in Lista)

# Elimina a "Cave" de la lista.
Lista.remove("Cave")
print(Lista[:])

# Muestra el último elemento de la lista.
print(Lista.pop())

# Una lista puede tener bools, números, floats y strings.
TerceraLista = [True, 10, -10, 10.5, "Hola"]
print(TerceraLista[:])

# Repite la lista 3 veces.
print(Lista * 3)