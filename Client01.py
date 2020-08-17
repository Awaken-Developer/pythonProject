import socket

clientSocket = socket.socket()
clientSocket.connect(('localhost',9999))

print(clientSocket.recv(1024).decode())