# Una tupla es una lista inmutable, no se puede modificar después de su creación.

# Es más rápida.
# Mayor optimización.
# Puede utilizarse como claves en un diccionario.
# Permite comprobar si existe un elemento dentro.
# No permite añadir, eliminar, mover elementos, etc.
# No permiten búsquedas (no index).

# Sintaxis para crear una Tupla.
Tupla = ("Erick", 1, 2)
print(Tupla)

# Crear una Lista a partir de una Tupla (conversión).
Lista = list(Tupla)
print(Lista)

# Mostrar cuantas veces existe el número 2.
print(Tupla.count(2))

# Mostrar cuantos elementos contiene (lo mismo que se usó en Listas).
cantidadElementos = len(Tupla)
print(cantidadElementos)

# Empaquetado de una Tupla
segundaTupla = "Erick", 2001, 10
print(segundaTupla)

# Desempaquetado de una Tupla
# Se crea la Tupla.
Datos = "Erick", "Octubre", 2001

# Se asigna las variables a los datos que contien la Tupla.
Nombre, Mes, Year = Datos

# Mostrar las variables.
print(Nombre, Mes, Year)
