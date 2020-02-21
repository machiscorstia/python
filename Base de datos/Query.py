import sqlite3

Conexion = sqlite3.connect("Jugador")

Puntero = Conexion.cursor()

Puntero.execute("SELECT * FROM Jugadores WHERE Puntaje > 10")

Resultado = Puntero.fetchall()

print(Resultado)

for i in Resultado:
	print("Nombre:", i[0], " Contraseña:", i[1], " Puntaje:", i[2])

Conexion.commit()

Conexion.close()
