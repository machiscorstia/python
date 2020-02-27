import socket, threading

class Atiende(threading.Thread):
	def __init__(self, socket, direccionCliente):
		threading.Thread.__init__(self)

		self.socket = socket
		self.direccionCliente = direccionCliente

	def run(self):
		print("> Conexión entrante..")
		print("> Cliente conectado ", self.direccionCliente[0], ":", self.direccionCliente[1])

		while True:
			datosRecibidos = self.socket.recv(1024)
			Mensaje = datosRecibidos.decode("utf-8")

			if Mensaje == "salir":
				break

			print(self.direccionCliente[0], ":", self.direccionCliente[1], ">", Mensaje)

		print("> Se ha desconectado", self.direccionCliente[0], ":", self.direccionCliente[1])
		self.socket.close()
	
socketServidor = socket.socket()

socketServidor.bind(("localhost", 9999))
print("> Servidor conectado a localhost:9999")

socketServidor.listen(5)
print("> Esperando alguna conexión..")

# Espera conexiones entrantes..
while True:
	socketCliente, direccion = socketServidor.accept()

	Cliente = Atiende(socketCliente, direccion)
	Cliente.start()

socketServidor.close()