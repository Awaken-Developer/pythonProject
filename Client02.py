import socket
import pickle

#defined class template for client side
class NoteBooks:
    def __init__(self, pages, price, size):
        self.pages = pages
        self.price = price
        self.size = size

    def show(self):
        return self

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 9999))

navneetStream = clientSocket.recv(1024)
navneet = pickle.loads(navneetStream)

print(navneet.show().size)
