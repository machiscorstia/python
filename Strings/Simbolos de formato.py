"""
	Simbolo		Explicación
	*			Indica precisión desde los argumentos.
	-			Justifica a la izquierda el string.
	.			Trunca strings.
	+			Despliega el signo del valor numérico.
	0			Llena de 0's los espacios.
	()			Referencias desde objetos
"""

print("Nombre: [%10s]" %("Cave"))
print("Nombre: [%-10s]" %("Cave"))

print("Nombre: [%*s]" %(5, "Cave"))
print("Nombre: [%-*s]" %(5, "Cave"))

print("Edad: [%+d]" %34)
print("Edad: [%+d]" %-34)

print("Edad: [%05d]" %34)
print("Edad: [%+05d]" %34)

print("El nombre completo de cave es: [%10s]" %"Cave pelotudo")
print("El nombre completo de cave es: [%.10s]" %"Cave pelotudo")


Colores = {"Cave": "Negro", "Color": "Negro"}
Datos = {"Edad": 30, "Peso": 60.50}

print("%(Cave)s es de color %(Color)s" %(Colores))