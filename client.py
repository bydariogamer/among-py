import pygame
import socket
import sys

# initialize pygame
pygame.init()
pygame.mixer.init()

# set window mesures, title, icon
DISP_WID = 800
DISP_HEI = 600
DISP_TIT = 'AMONG PY'
DISP_ICO = pygame.image.load('assets/icon/icon.png')
clock = pygame.time.Clock()

# initialize window
pygame.display.set_caption(DISP_TIT)
pygame.display.set_icon(DISP_ICO)
game = pygame.display.set_mode((DISP_WID, DISP_HEI))


class TextBox:
    width = 200
    height = 50

    def __init__(self, x, y):
        self.back_surface = pygame.Surface((TextBox.width, TextBox.height))
        self.back_surface.fill("WHITE")
        self.rect = pygame.Rect(x, y, TextBox.width, TextBox.height)
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 50)
        self.text_surface = pygame.Surface((0, 0))
        self.text = ""
        self.active = False

    def click(self, event):
        mouse_location = event.pos
        if self.rect.collidepoint(mouse_location[0], mouse_location[1]):
            self.active = True
        else:
            self.active = False

    def add_text(self, event):
        if self.active:
            self.text += event.text
            self.text_surface = self.font.render(self.text, True, "BLACK")

    def render(self, screen):
        screen.blit(self.back_surface, self.rect)
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
                    

# read last configuration
port = 31416
password = 'helloworld'
server = "127.0.0.1"
name = 'bydariogamer'

configuration = open('client.conf', 'r')

for line in configuration.readlines():
    if 'password: ' == line[0:9]:
        password = line[10:]
    if 'port: ' == line[0:5]:
        port = str(line[6:])
    if 'server: ' == line[0:7]:
        server = line[8:]
    if 'name: ' == line[0:5]:
        name = line[6:]

configuration.close()

# pregame page

done = False
QUIT = False
textboxes = [TextBox(10,10),TextBox(10,110),TextBox(10,210),TextBox(10,410)]
while not done:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for textbox in textboxes:
                textbox.click(event)
        if event.type == pygame.TEXTINPUT:
            for textbox in textboxes:
                textbox.add_text(event)
    if QUIT:
        pygame.quit()
        break

    # rendering
    game.fill("BLACK")
    for textbox in textboxes:
        textbox.render(game)
    pygame.display.flip()
    clock.tick(60)
    
if not QUIT:
    configuration = open('client.conf', 'w')
    configuration.write(f"name: {name}\n")
    configuration.write(f"server: {server}\n")
    configuration.write(f"port: {port}\n")
    configuration.write(f"password: {password}\n")
    QUIT = False
    


# game loop
while not QUIT:
    # and here it goes the game itself
    # Create a socket object
    server = socket.socket()

    # connect to the server on local computer
    server.connect((server, port))

    server.send(bytes(password))

sys.exit()
