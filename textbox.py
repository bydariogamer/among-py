import pygame
class TextBox(pygame.Surface)
    def __init__(self, x, y, height, width, font = pygame.font.SysFont(pygame.font.get_default_font(), y - 10) , hint : Str = None, color_back = (255, 255, 255), color_font = (0, 0, 0)):
        super.__init__((height, width))
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hint = hint
        self.back_surface = pygame.Surface(width, height))
        self.back_surface.fill(color_back)
        self.rect = pygame.Rect(x, y, TextBox.width, TextBox.height)
        self.font = font
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
            self.text_surface = self.font.render(self.text, True, (0, 0, 0))

    def render(self, screen):
        screen.blit(self.back_surface, self.rect)
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))

"""
tb = TextBox(100, 100)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            tb.click(event)
        if event.type == pygame.TEXTINPUT:
            tb.add_text(event)
    screen.fill("BLACK")
    tb.render()
    pygame.display.flip()
    clock.tick(60)
"""
