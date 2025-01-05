import pygame

pygame.init()

from card_cache import get_list

class App:
    def __init__(self):
        self.width, self.height = 1200, 400
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (16, 16, 16)
        self.win.set_alpha(128)

        self.movie_card_list = get_list()

    def draw_cards(self):

        for i in range(len(self.movie_card_list)):

            if self.movie_card_list[i].x >= 0 and self.movie_card_list[i].x <= self.width:
                self.movie_card_list[i].draw(self.win)

    def main_function(self):

        Running = True
        while Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RIGHT:

                        if self.movie_card_list[len(self.movie_card_list) - 1].x >= 1000:

                            for card in self.movie_card_list:
                                card.x -= 200

                    if event.key == pygame.K_LEFT:

                        if self.movie_card_list[0].x <= 200:

                            for card in self.movie_card_list:
                                card.x += 200
                    
            self.draw()

    def draw(self):

        self.win.fill(self.color)

        self.draw_cards()

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()