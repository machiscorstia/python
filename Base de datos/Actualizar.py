import sqlite3

Conexion = sqlite3.connect("Jugador")

Puntero = Conexion.cursor()

# Cambia el nombre de Manu a ne0de
Puntero.execute("UPDATE Jugadores SET Nombre = 'ne0de' WHERE Id = 1")

Conexion.commit()

# Elimina a silvio.
Puntero.execute("DELETE FROM Jugadores WHERE Id = 2")

Conexion.commit()

Conexion.close()
