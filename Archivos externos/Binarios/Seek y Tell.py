NOMBRE_ARCHIVO = "Lectura.py"

posicionInicial = 0
posicionActual = 1
posicionFinal = 2

Archivo = open(NOMBRE_ARCHIVO, "r")


Archivo.seek(0, posicionInicial)

posicion = Archivo.tell()

