import threading, time

class Tiempo(threading.Thread):

	def __init__(self, nombre, segundos, contador):
		threading.Thread.__init__(self)
		self.nombre = nombre
		self.segundos = segundos
		self.contador = contador

	def run(self):
		while True:
			Hoy = time.localtime()
			print(self.nombre, "Hora:", Hoy.tm_hour, "Minuto:", Hoy.tm_min, "Segundo:", Hoy.tm_sec)
			print()
			time.sleep(self.segundos)
			self.contador -= 1
			if self.contador < 1:
				print("Fin timer", self.nombre)
				break

primerTimer = Tiempo("t1", 1, 5)

segundoTimer = Tiempo("t2", 2, 5)

primerTimer.start()

segundoTimer.start()