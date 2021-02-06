import socket
import threading
import pygame

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind("", )


class Client(threading.Thread):
    def __init__(self, client_socket, client_data):
        super().__init__(self)
        self.connection = client_socket
        self.data = client_data
        self.running = True
        self.received = None

    def run(self):
        while self.running:
            self.received = self.connection.recv()
            self.process()
        self.connection.close()

    def process(self):
        if self.received is not None:
            if self.received == 'QUIT':
                self.running = False
