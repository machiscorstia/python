from io import open

# 2 argumento "w" de solamente escribir.

Archivo = open("Pelotudos.txt", "w")
Texto = "Silvio\nErick\nLucas"
Archivo.write(Texto)
Archivo.close()