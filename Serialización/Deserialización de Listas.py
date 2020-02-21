import pickle

# rb: read binary

Archivo = open("Listita", "rb")

Lista = pickle.load(Archivo)

print(Lista)

Archivo.close()
