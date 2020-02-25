import sqlite3

Conexion = sqlite3.connect("Jugador")

Puntero = Conexion.cursor()

Puntero.execute("INSERT INTO Jugadores VALUES(NULL, 'Erick', 'pene', 10)")

Conexion.commit()

Conexion.close()
