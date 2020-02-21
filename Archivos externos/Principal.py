from io import open

Archivo = open("Pelotudos.txt", "w")
Texto = "Silvio\nErick\nLucas"
Archivo.write(Texto)