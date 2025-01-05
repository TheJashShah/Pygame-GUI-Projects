from movie_card import MovieCard
from API.cache import get_movies
from API.image_cache import load_images

movie_list = get_movies()
images = load_images()

def return_movie_card_list(X, Y, PAD):

    movie_card_list = []

    for i in range(len(movie_list)):
        movie_card_list.append(MovieCard(X + (PAD * i), Y, movie_list[i], images[i]))

    return movie_card_list