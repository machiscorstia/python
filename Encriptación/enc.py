import sys, ctypes, os.path, base64

Clave = "1234"
Comandos = ['E', 'D', 'S']

def accion(cmd):
    if cmd not in Comandos:
        return print("No existe ese comando.")
    
    if cmd == 'E':
        return encriptar()
    elif cmd == 'D':
        
        return desencriptar()

def verificar(t):
    if t != Clave:
        ctypes.windll.user32.MessageBoxW(0, "Esa no es la clave maestra.", "Ups..", 0x10)
        return sys.exit()
    return True

def definirArchivo():
    nombreArchivo = input("Nombre archivo > ")
    nombreArchivo = nombreArchivo + ".txt"
    return nombreArchivo

def limpiarArchivo(Archivo):
    Archivo.seek(0)
    Archivo.truncate()

def mostrarOpciones():
    print("Comandos > \nE -> encriptar .txt\nD -> desencriptar .txt\nS -> salir del programa")

def estaEncriptado(nombreArchivo):
    en = False
    with open(nombreArchivo, "r") as Archivo:
        for index, valor in enumerate(Archivo):
            if index == 0 and valor.strip() == "Encriptado":
                en = True
                break
            else:
                break
    return en

def encriptar():
    print("Encriptación de txt..")
    nombreArchivo = definirArchivo()

    if not os.path.isfile(nombreArchivo):
        return print("[ERROR] No existe ese archivo en el directorio.")

    if estaEncriptado(nombreArchivo):
         return print("[ERROR] El archivo ya se encuentra encriptado.")
    
    with open(nombreArchivo, "r+") as Archivo:
        con = Archivo.read()
        mensaje_encriptado  = base64.b64encode(con.encode())
        limpiarArchivo(Archivo)
        Archivo.write("Encriptado\n" + mensaje_encriptado.decode())
        Archivo.close()
    
    print("Archivo encriptado correctamente.")
    return True

def desencriptar():
    print("Desencriptación de txt..")
    nombreArchivo = definirArchivo()

    if not os.path.isfile(nombreArchivo):
        return print("[ERROR] No existe ese archivo en el DIR.")

    if not estaEncriptado(nombreArchivo):
         return print("[ERROR] El archivo no se encuentra encriptado.")

    with open(nombreArchivo, "r+") as Archivo:
        con = Archivo.readlines()
        texto_encriptado = con[1]
        mensaje_desencriptado = base64.b64decode(texto_encriptado.encode())
        limpiarArchivo(Archivo)
        Archivo.write(mensaje_desencriptado.decode())
        Archivo.close()
    print("Archivo desencriptado correctamente.")
    return True

print("Ingresa la contraseña para proceder a desencriptar las cuentas.")
verificar(str(input("> ")))
mostrarOpciones()

while True:
    cmd = input("> ")
    if cmd == 'S':
        break
    accion(cmd)
    