import pickle

from movie_card_list import return_movie_card_list

X, Y, PAD = 10, 10, 200

def save_list():

    card_list = return_movie_card_list(X, Y, PAD)

    with open("src/card.pkl", "wb") as file:
        pickle.dump(card_list, file, protocol=pickle.HIGHEST_PROTOCOL)

def get_list():

    try:
        with open("src/card.pkl", "rb") as file:
            card_list = pickle.load(file)

        return card_list

    except FileNotFoundError:
        save_list()
        return get_list()