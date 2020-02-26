"""
	Un objeto es un espacio en la memoria que tiene almacenado variables y métodos.
"""
# Con dir y adentro del parámetro muestra todos los métodos de la clase.
# Mostrando metodos de una Lista.
print(dir([]))

class Auto():
	def __init__(self, nombre, modelo, color):
		self.nombre = nombre
		self.modelo = modelo
		self.color = color

Ford = Auto("Fiesta", "Ford", "Rojo")

print("El tipo es: " + str(type(Ford)))

print("Metodos de la clase Ford:", str(dir(Ford)))
