"""
	Mejor que programación orientada a procedimientos xD

	Un método es una función especial que pertenece a la clase, ya que es de esa clase.

	Para encapsular usar __ para que no sea accesible desde otro lado que no sea la misma clase.

"""
class Celular():

	def __init__(self): # Constructor
		self.__Estado = False
		self.__Bateria = 50
		self.__Memoria = 1000 	# En megabytes.
		self.__TarjetaDeRed = True	

	def Escender(self, valor):
		self.__Estado = valor
		if(self.__Estado):
			if(self.__chequearDatos()):
				print("El chequeo salió bien")
			else:
				print("El chequeo salió mal")
			
			print("El celular se prendió")
		else:
			print("El celular se apagó")

	def obtenerEstado(self):
		return self.__Estado

	# Chequeo de la memoria y la tarjeta de red, simple ejemplo.
	def __chequearDatos(self):
		return (self.__Memoria == 1000 and self.__TarjetaDeRed)

Samsung = Celular()

print(Samsung.obtenerEstado())
Samsung.Escender(True)


Samsung.Estado = True


class Pene():
	def mostrar():
		print(hola)
