# import pygame
import socket

# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
SERVER = '127.0.0.1'    # TODO how to give adifferent IP
PORT = 12345    # TODO which port?

# connect to the server on local computer
s.connect((SERVER, PORT))

# receive data from the server
print(s.recv(1024))
# close the connection
s.close()