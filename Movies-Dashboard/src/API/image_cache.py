import requests, pickle
from .cache import get_movies

movie_list = get_movies()

def store_images():

    responses = []

    for movie in movie_list:
        response = requests.get(movie['primaryImage'])
        responses.append(response.content)

    with open("src/API/images.pkl", "wb") as file:
        pickle.dump(responses, file)

def load_images():

    try:
        with open("src/API/images.pkl", "rb") as file:
            responses = pickle.load(file)

        return responses

    except FileNotFoundError:
        store_images()
        return load_images()
    