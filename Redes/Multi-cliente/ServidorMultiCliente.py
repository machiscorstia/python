import socket, threading

Clientes = []

class recibeMensajes(threading.Thread):
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
	
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socketServidor.bind(("localhost", 9999))
print("> Servidor conectado a localhost:9999")

socketServidor.listen(5)
print("> Esperando alguna conexión..")

# Espera conexiones entrantes..
while True:
	socketCliente, direccion = socketServidor.accept()

	Cliente = recibeMensajes(socketCliente, direccion)
	Cliente.start()

socketServidor.close()