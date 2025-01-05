'''
'title', 'primaryImage', 'description', 'averageRating', 'numVotes', 'runtimeMinutes', 'startYear'
'''

def get_top_movies_all_time():

    import http.client, json

    connection = http.client.HTTPSConnection("imdb236.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "c402d331ecmsh1f4d40ad887d47dp1e7af9jsn3c27aa8347b1",
        'x-rapidapi-host': "imdb236.p.rapidapi.com"
    }

    connection.request("GET", "/imdb/top250-movies", headers=headers)

    response = connection.getresponse()
    data = response.read()

    movie_list = json.loads(data)

    return movie_list
