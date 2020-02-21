from io import open

# 2 argumento "r" de solamente leer.

Archivo = open("Pelotudos.txt", "r")
Texto = Archivo.read()

# .seek(num) para empezar a leer desde esa posición del str.
# Lineas = Archivo.readlines() para leer en lineas y guardarlo en una lista.
print(Texto)

Archivo.close()