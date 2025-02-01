import pygame

class Line:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont("monospace", 15)

        self.visible = True

    def draw(self, win):

        if self.visible:
            text = self.font.render(self.text, True, (0, 0, 0))
            win.blit(text, (self.x, self.y))