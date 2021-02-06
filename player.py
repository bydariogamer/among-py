import pygame
# import socket


class Player(pygame.sprite.Sprite):
    """this class stands for the player"""

    def __init__(self, name, impostor, tasks, world, images):
        super().__init__()

        self.name = name
        self.impostor = impostor
        self.tasks = tasks
        self.world = world
        self.images = images

        self.alife = True

        self.pos_x = 0
        self.pos_y = 0

        self.up = False
        self.down = False
        self.right = False
        self.left = False

    def interact(self):
        """this class will be called when the interaction buttom is pressed. It will check if there is an interactive
        object or puzzle object around and call their `interact()` function in that case"""

        for interactive in self.world.interactives:
            if ((interactive.pos_x - self.pos_x) ** 2 + (interactive.pos_y - self.pos_y) ** 2) ** 0.5 < 100:
                interactive.interact()

    def assassin(self, other):
        if self.impostor:
            other.alife = 0

    def update(self):
        if self.down:
            self.pos_y += self.world.speed

        if self.up:
            self.pos_y -= self.world.speed

        if self.right:
            self.pos_x += self.world.speed

        if self.left:
            self.pos_x -= self.world.speed

        for wall in self.world.walls:
            if self.rect.colliderect(wall):
                if self.down:
                    self.pos_y -= self.world.speed

                if self.up:
                    self.pos_y += self.world.speed

                if self.right:
                    self.pos_x -= self.world.speed

                if self.left:
                    self.pos_x += self.world.speed
