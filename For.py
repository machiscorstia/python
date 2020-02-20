Texto = input("Introduce un texto")

for i in Texto:
	if i == '#':
		numeral = True
		break;
else:
	numeral = False

print(numeral)