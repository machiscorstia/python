import sqlite3

Conexion = sqlite3.connect("Jugador")

Puntero = Conexion.cursor()

Puntero.execute("""
	CREATE TABLE Jugadores (
	Id INTEGER PRIMARY KEY AUTOINCREMENT,
	Nombre VARCHAR(24) UNIQUE, 
	Contraseña VARCHAR(24), 
	Puntaje INTEGER)

	""")

Conexion.close()