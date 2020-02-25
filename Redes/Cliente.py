import socket

Cliente = socket.socket()
Host = socket.gethostname()
Puerto = 2000
Cliente.connect((Host, Puerto))
print(Cliente.recv(1024))