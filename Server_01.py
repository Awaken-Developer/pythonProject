import pickle
import socket
import threading
import time

#_______HOST ATTRIBUTES______
HOST = 'localhost'
PORT = 9999

class NoteBooks:
    def __init__(self, pages, price, size):
        self.pages = pages
        self.price = price
        self.size = size

    def show(self):
        return self
#server side object creation
serverSideObj: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#object definations
navneet = NoteBooks(140, 56.00, "a4")
classmate = NoteBooks(120, 45.00, "a4")
genius = NoteBooks(160, 50.00, "a4")

#object defination for lock
lock = threading.Lock()

class clientThread (threading.Thread):
    def __init__(self, threadID, name, serverSideObj, hostIP, portNumber):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.serverSideObj = serverSideObj
        self.hostIP = hostIP
        self.portNumber = portNumber

    def run(self):
        lock.acquire()
        self.serverSideObj.listen(1)
        print("Waiting for connection")
        navneetStream = pickle.dumps(navneet)
        clientSocket, clientAddress = self.serverSideObj.accept()
        print("connection is established with", clientAddress)
        clientSocket.send(navneetStream)
        clientSocket.close()
        time.sleep(2.4)
        print("thread is in sleep for 2.4secs")
        lock.release()


clientOne = clientThread(1, "Thread-1", serverSideObj, HOST, PORT)
clientTwo = clientThread(2, "Thread-2", serverSideObj, HOST, PORT)

# execution of the serverside tcp requests
serverSideObj.bind((clientOne.hostIP, clientOne.portNumber))
print("sercver is binded to host", clientOne.hostIP, "on port", clientTwo)
clientOne.start()
clientTwo.start()


