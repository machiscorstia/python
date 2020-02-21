import sqlite3

Conexion = sqlite3.connect("Jugador")

Puntero = Conexion.cursor()

Jugadores = [
	("Manu", "soymanu44", 15),
	("Silvio", "manuputo", 15)
]

Puntero.executemany("INSERT INTO Jugadores VALUES(NULL, ?, ?, ?)", Jugadores)

Conexion.commit()

Conexion.close()
