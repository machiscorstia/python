from io import open
import os

# "rb" read binary, "wb" write binary

Archivo = open("Pelotudos.rar", "rb")
nombreArchivo = os.path.basename(str(Archivo.name))

posicionPunto = 0
contadorLetras = 0

for i in nombreArchivo:
	contadorLetras += 1
	if i == '.':
		posicionPunto = contadorLetras - 1
		break

nombreCopia = nombreArchivo[0:posicionPunto]
print(nombreCopia)
nombreCopia = nombreCopia + "Copia.rar"

ArchivoFinal = open(nombreCopia, "wb")

contadorBytes = 0
bytesCopiados = 0

while True:
	
	# Se lee un byte del archivo.
	byte = Archivo.read(1)

	if len(byte) == 0:
		break

	ArchivoFinal.write(byte)

	bytesCopiados += 1

print("Bytes copiados:", bytesCopiados)

Archivo.close()
ArchivoFinal.close()
