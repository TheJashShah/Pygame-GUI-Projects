import pygame

class DropBox:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 400
        self.height = 175
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.font = pygame.font.SysFont("monospace", 20)
        self.text = "Drag and Drop your CSV Files!"

        self.icon = pygame.image.load("assets/icon.png")
        self.img_width, self.img_height = self.icon.get_width()//8, self.icon.get_height()//8
        self.icon = pygame.transform.scale(self.icon, (self.img_width, self.img_height))

        self.icon_display = False

    def draw(self, win):

        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x - 4, self.y - 4, self.width + 8, self.height + 8), 4, 4, 4, 4)
        pygame.draw.rect(win, (240, 240, 240), self.rect)

        text = self.font.render(self.text, True, (0, 0, 0))
        win.blit(text, text.get_rect(center = (self.x + self.width/2, self.y + self.height/2)))

        if self.icon_display:
            win.blit(self.icon, (self.x + self.width/2 - 32, self.y + 10))