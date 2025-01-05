import json

from .api import get_top_movies_all_time

def save_movies_to_file(LIST):

    with open("src/API/cache.json", "w") as file:
        json.dump(LIST, file)


def load_movies_from_file():

    try:
        with open("src/API/cache.json", "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return None
    
def get_movies():

    LIST = load_movies_from_file()

    if not LIST:
        LIST  = get_top_movies_all_time()
        save_movies_to_file(LIST)

    return LIST