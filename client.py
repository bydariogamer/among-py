import pygame
import socket


# initialize pygame
pygame.init()
pygame.mixer.init()

# set window mesures, title, icon
DISP_WID = 800
DISP_HEI = 400
DISP_TIT = 'AMONG PY'
DISP_ICO = pygame.image.load('assets/images/icon/icon.png')
clock = pygame.time.Clock()

# initialize window
pygame.display.set_caption(DISP_TIT)
pygame.display.set_icon(DISP_ICO)
game = pygame.display.set_mode((DISP_WID, DISP_HEI))

# read last configuration
config = open('client.config', 'r')

PORT = 31416
PASSWORD = 'helloworld'
SERVER = "127.0.0.1"

for line in config.readlines():
    if 'password: ' == line[0:9]:
        PASSWORD = line[10:]
    if 'port: ' == line[0:5]:
        PORT = line[6:]
    if 'server: ' == line[0:7]:
        SERVER = line[8:]


QUIT = False
while not QUIT:

    # Create a socket object
    server = socket.socket()

    # connect to the server on local computer
    server.connect((SERVER, PORT))

    server.send(bytes(PASSWORD))

