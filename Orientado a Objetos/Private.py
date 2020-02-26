class Vehiculo():
	def __init__(self, modelo, motor):
		self.modelo = modelo
		self.motor = motor

		# Atributo privado, solo la clase puede acceder a ello.
		self.__codigo = str(modelo) + str(motor)

	# Método privado, solamente la clase puede acceder a eso.
	def __mostrarCodigo(self):
		return self.__codigo

Ford = Vehiculo("Ford", "453B")

#print(Ford.__codigo)
#print(Ford.__mostrarCodigo)