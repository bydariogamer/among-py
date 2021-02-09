import socket
import threading
import pygame
import player

PORT = 31416
PASSWORD = 'helloworld'

config = open('server.conf', 'r')
for line in config.readlines():
    if 'password: ' == line[0:9]:
        PASSWORD = line[10:]
    if 'port: ' == line[0:5]:
        PORT = line[6:]


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))


class Client(threading.Thread):
    def __init__(self, client_socket : socket.socket, client_data):
        super().__init__()
        self.connection = client_socket
        self.data = client_data
        self.running = True
        self.received = None
        self.player = None
        self.confirmed = False
        self.identified = False

    def run(self):
        while self.running:
            self.received = self.connection.recv(1024)
            self.process()
        self.connection.close()

    def process(self):
        if self.received is not None:
            if str(self.received) == 'QUIT':
                self.running = False
                self.received = None
            if self.player:
                if str(self.received) == PASSWORD:
                    self.connection.send(bytes('confirmed ' + str(self.data[0])))
                    self.confirmed = True
                    self.connection.send(bytes('identify'))
                    self.received = None
                if self.confirmed and self.player is None:
                    self.player =


