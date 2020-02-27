import socket

class Cliente(socket.socket):

    def __init__(self):
        self.socket = socket.socket()
        print(self.socket)


    def hacerConexion(self, host, puerto):
    	print("> Conectandose a", host, puerto, "...")
    	try:
    		self.socket.connect((host, puerto))
    		self.enviarMensajes()
    	except ConnectionRefusedError:
    		print("> No se pudo conectar al servidor, esa dirección no está disponible.")


    def enviarMensajes(self):
        while True:
            Mensaje = input("Escribe un mensaje: ")
            self.socket.send(bytes(Mensaje, "utf-8"))
            if Mensaje == "salir":
                break
        self.cerrarConexion()


    def cerrarConexion(self):
        print("> Te has desconectado del servidor.")
        self.socket.close()

Erick = Cliente()
Erick.hacerConexion("localhost", 9999)