from movie_service import MovieService


class MovieController():

    def render_movies(self):
        movie_service = MovieService()
        movies = movie_service.fetch_movies()
        return movies
