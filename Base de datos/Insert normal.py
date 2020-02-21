import sqlite3

Conexion = sqlite3.connect("Jugador")

Puntero = Conexion.cursor()

Puntero.execute("INSERT INTO Jugadores VALUES('Erick', 'octubres10', 10)")

Conexion.commit()

Conexion.close()
