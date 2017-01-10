from models.movie import Movie


class MovieService():
    FILE_NAME = 'data/movie.json'

    def __init__(self):
        pass

    def fetch_movies(self):
        toy_story = Movie("Toy Story", "A story of a boy and his toy",
                          "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                          "https://www.youtube.com/watch?v=4KPTXpQehio")
        movie_list = []
        movie_list.append(toy_story)
        return movie_list
