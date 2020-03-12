import hashlib, sys, ctypes

Clave = "1234"

def verificar(t):
    if t != Clave:
        ctypes.windll.user32.MessageBoxW(0, "Esa no es la clave maestra.", "Ups..", 0x10)
        sys.exit()
    return True

print("Ingresa la contraseña para proceder a desencriptar las cuentas.")
if verificar(str(input("> "))):
    print("bien")