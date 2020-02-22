"""
		 128 64 32 16 8 4 2 1
	8  =   0  0  0  0 1 0 0 0
	15 =   0  0  0  0 1 1 1 1

Operador & -> AND.

Operador | -> OR.

Operador ^ -> XOR (tabla de verdad diferentes 0-1, 1-0).

Operador ~ -> Complemento A2: 00001000 (8) -> 11110111 (-9).

Operador >> Desplaza bits a la derecha.

Operador << Desplaza bits a la izquierda.
"""


print("8 & 15 =", 8 & 15)
print("8 | 15 =", 8 | 15)
print("8 ^ 15 =", 8 ^ 15)
print("8 ^ 15 =", 8 ^ 15)
print("~8, ~15=", ~8, ~15)
print("8 << 2 =", 8 << 2)
print("8 >> 2 =", 8 >> 2)