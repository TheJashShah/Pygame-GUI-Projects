import pygame

class Button:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 50
        self.text = text

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.font = pygame.font.SysFont("monospace", 20)

        self.visible = False

    def draw(self, win):

        if self.visible:

            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4), 2, 2, 2, 2)
            pygame.draw.rect(win, (10, 10, 200), self.rect)

            text = self.font.render(self.text, True, (200, 200, 200))
            win.blit(text, text.get_rect(center = (self.x + self.width/2, self.y + self.height/2)))