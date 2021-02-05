import pygame

class Player(pygame.sprite.Sprite):
    """this class stands for the player"""

    def __init__(self):
        super().__init__()
        self.name = ""
        self.impostor = False
        self.alife = True
        self.tasks = []
        self.images = {
            "alife": pygame.image.load("assets/player/player.png"),
            "ghost": pygame.image.load("assets/player/phantom.png")
        }
        self.pos_x = 0
        self.pos_y = 0

    def interact(self, world):
        """this class will be called when the interaction buttom is pressed. It will check if there is an interactive
        object or puzzle object around and call their `interact()` function in that case"""

        for interactive in world.interactives:
            if abs(interactive.pos_x - self.pos_x) < world.scope:
                pass # TODO



