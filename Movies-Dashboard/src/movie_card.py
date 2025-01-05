import pygame
from io import BytesIO

class MovieCard:
    def __init__(self, x, y, movie_disc, img_content):
        self.x = x
        self.y = y
        self.movie_disc = movie_disc

        self.title = self.movie_disc['title']
        self.url = self.movie_disc['primaryImage']
        self.desc = self.movie_disc['description']
        self.rating = self.movie_disc['averageRating']
        self.votes = self.movie_disc['numVotes']
        self.len = self.movie_disc['runtimeMinutes']
        self.year = self.movie_disc['startYear']

        self.img_content = img_content
        self.img = self.load_img()

        self.width, self.height = 175, 300

        self.img = pygame.transform.smoothscale(self.img, (self.width, self.height))

    def load_img(self):

        return pygame.image.load(BytesIO(self.img_content)).convert_alpha()

    def draw(self, win):

        win.blit(self.img, (self.x, self.y))
        pygame.draw.rect(win, (255, 255, 255), pygame.Rect(self.x - 4, self.y - 4, self.width + 8, self.height + 8), 2)

    def __getstate__(self):
        
        state = self.__dict__.copy()

        del state['img']
        return state
    
    def __setstate__(self, state):

        self.__dict__.update(state)

        self.img = self.load_img()
        self.img = pygame.transform.smoothscale(self.img, (self.width, self.height))
        