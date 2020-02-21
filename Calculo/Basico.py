
def Sumar(primerNumero, segundoNumero):
	return primerNumero +  segundoNumero

def Restar(primerNumero, segundoNumero):
	return primerNumero - segundoNumero

def Multiplicar(primerNumero, segundoNumero):
	return primerNumero * segundoNumero

def Dividir(Dividendo, Divisor):
	try:
		Total = Dividendo/Divisor
		return Total
	except ZeroDivisionError:
		print("No se puede dividir entre 0")

def Potenciar(Numero, Exponente):
	return Numero ** Exponente

def Redondear(Numero):
	return round(Numero)


