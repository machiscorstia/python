import pickle

Lista = ["Erick", "Lucas", "Silvio", "Cave", "Masucco", "Alex"]

# wb: write binary

Archivo = open("Listita", "wb")

# Lo convierte.
pickle.dump(Lista, Archivo)

Archivo.close()

# Elimina de la memoria.
del (Archivo)