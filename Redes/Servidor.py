"""
	El socket es un componente básico en las comunicaciones de redes, es denominado el canal de información, 
	ya que permite hacer un intercambio entre el servidor y el cliente en un puerto en especifico.

	En este caso el socket del servidor atenderá la información que le entre por el flujo de entrada.
"""

import socket

# Creamos una instancia de la clase socket.
Servidor = socket.socket()

# La función gethostname devuelve la dirección del host de nuestra nuestra red.
Host = socket.gethostname()

# Un puerto cualquiera, que no este ocupado.
Puerto = 2000

# Enlaza el host y el puerto al Servidor.
Servidor.bind((Host, Puerto))

# Establecemos cuantos clientes podemos tener conectados.
Servidor.listen(3)

# En este bucle básicamente lo que hace es aceptar la conexión de algún cliente.
# Una vez que lo acepta le envia al cliente un mensaje y cierra su conexión.
while True:
	Cliente, Direccion = Servidor.accept()
	print("Conexion obtenida de… ", Direccion)
	Cliente.send(b'Te has conectado al servidor')
	Cliente.close()