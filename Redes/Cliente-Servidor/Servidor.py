import socket
"""
	netstat -ano|findstr PUERTO
	tskill ID

"""
direccionServidor = "localhost", 9999

socketServidor = socket.socket()
#print(socketServidor)

socketServidor.bind(direccionServidor)
print("> Conectado a", direccionServidor)

# Solo va a aceptar una conexión.
socketServidor.listen(1)
print("> Esperando alguna conexión..")

# Si recibe una conexión, lo acepta.
socketCliente, direccionCliente = socketServidor.accept()
print("> Aceptando una conexión entrante..")
print(socketCliente, direccionCliente)

while True:
	datosRecibidos = socketServidor.recv(1024)

	Mensaje = datosRecibidos.decode("utf-8")

	if Mensaje == "salir":
		break

	print("Datos recibidos:", Mensaje)

print("Se cerró la conexión del cliente y del servidor")

socketServidor.close()
