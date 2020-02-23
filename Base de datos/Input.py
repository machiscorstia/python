"""
	Son colecciones de datos que se indexan a través de claves (keys)
	Estas claves pueden ser cadenas, números y tuplas. 
	Las listas no se pueden usar como keys.

"""
DatosDeSilvio = ["Gabriel", "Carames", 18]
Diccionario = {1: DatosDeSilvio, 2: "Erick"}

print(Diccionario.get("Erick"))