import threading, time

class Tiempo(threading.Thread):

	def __init__(self, nombre, segundos, contador):
		threading.Thread.__init__(self)
		self.nombre = nombre
		self.segundos = segundos
		self.contador = contador
		self.pausa = False

	def run(self):
		while True:

			if self.contador == 0:
				print("Fin timer", self.nombre)
				break

			Hoy = time.localtime()

			if not self.pausa:
				print(self.nombre, "Hora:", Hoy.tm_hour, "Minuto:", Hoy.tm_min, "Segundo:", Hoy.tm_sec)
				print()
				time.sleep(self.segundos)
				self.contador -= 1

	def parar(self):
		self.contador = 0

	def pausar(self):
		self.pausa = True

	def despausar(self):
		self.pausa = False

primerTimer = Tiempo("t1", 2, 5)

primerTimer.start()


