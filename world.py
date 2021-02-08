import pygame


class World(object):
    def __init__(self):
        self.name = ""
        self.license = ""
        self.players = []
        self.impostors = []
        self.map = pygame.image.load("assets/test.png")
        self.rect = self.map.get_rect()
        self.speed = 40
        self.scope = 100
