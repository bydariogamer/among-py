import pygame
import socket

# Create a socket object
server = socket.socket()

# Define the port on which you want to connect
SERVER = '127.0.0.1'    # TODO add a way to configure the IP
PORT = 31416    # TODO which port

# connect to the server on local computer
server.connect((SERVER, PORT))

server.send(bytes(password))

