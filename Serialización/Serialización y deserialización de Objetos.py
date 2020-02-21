import pickle

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

Alcatel = Celular()	
Samsung = Celular()
Motorola = Celular()

Smartphones = [Alcatel, Samsung, Motorola]

Archivo = open("Smartphones", "wb")

pickle.dump(Smartphones, Archivo)

Archivo.close()

del (Archivo)

Archivo = open("Smartphones", "rb")

Smartphones = pickle.load(Archivo)


for i in Smartphones:
	print(i)

Archivo.close()