import pygame


class TextBox(object):
    def __init__(self, x, y, height, width, font=None, hint: str = None, color_back=(255, 255, 255), color_font=(0, 0, 0)):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color_back = color_back
        self.color_font = color_font
        self.hint = hint
        self.back_surface = pygame.Surface((width, height))
        self.back_surface.fill(color_back)
        self.text_surface = pygame.Surface((0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.rect = pygame.Rect(x, y, width, height)
        self.box_surface = self.back_surface = pygame.Surface((width, height))
        if font is None:
            self.font = pygame.font.SysFont(pygame.font.get_default_font(), self.y - 10)
        else:
            self.font = font
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
            self.text_surface = self.font.render(self.text, True, (0, 0, 0))
            self.box_surface.blit(self.back_surface, (0, 0))
            self.box_surface.blit(self.back_surface, (5, 5))
            self.text_rect = self.text_surface.get_rect()

    def draw(self):
        return self.box_surface

    def render(self, screen):
        screen.blit(self.text_surface, self.rect)
        if self.active:
            pygame.draw.line(screen, self.color_font, self.text_rect.bottomright, self.text_rect.topright)


# TEST
pygame.init()
game = pygame.display.set_mode((800, 600))
tb = TextBox(10, 10, 50, 100)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            tb.click(event)
        if event.type == pygame.TEXTINPUT:
            tb.add_text(event)
    game.fill((0, 0, 0))
    tb.render(game)
    pygame.display.update()
    clock.tick(60)
