# Clase padre
class Vehiculo():
	def __init__(self, modelo, motor):
		self.modelo = modelo
		self.motor = motor
		self.velocidad = 0

		# Atributo privado, solo la clase puede acceder a ello.
		self.__codigo = str(modelo) + str(motor)

	# Método privado, solamente la clase puede acceder a eso.
	def __mostrarCodigo(self):
		return self.__codigo

	def mostrarVelocidad(self):
		return self.velocidad


# Clase hijo
class Auto(Vehiculo):
	def __init__(self, nombre, modelo, motor):
		self.nombre = nombre
		Vehiculo.__init__(self, modelo, motor)
		print(super().mostrarVelocidad())

	def mostrarDatos(self):
		return self.nombre + self.modelo + self.motor

Ford = Auto("Fiesta", "Ford", "43B")

print(Ford.mostrarDatos())

