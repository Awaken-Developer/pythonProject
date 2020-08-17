import socket
serverSideObj = socket.socket()

print("Server side object has been created!")
serverSideObj.bind(('localhost', 9999))

serverSideObj.listen(3)
print("Waiting for connections")

while True:
    clientSocket, clientAddress = serverSideObj.accept()
    print("connection is established with", clientAddress)
    clientSocket.send(bytes('Welcome to the network', 'utf-8'))
    clientSocket.close()


