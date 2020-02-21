from io import open

# 2 argumento "w" de solamente escribir.

Archivo = open("Pelotudos.txt", "a")
Texto = "\nCave es un pelotudo"

Archivo.write(Texto)
Archivo.close()