import os
import json
import re
from settings import APP_DATA
from models.movie import Movie


class MovieService():
    FILE_NAME = 'movie.json'

    def __init__(self):
        pass

    def read_from_file(self):
        with open(os.path.join(APP_DATA, self.FILE_NAME)) as file:
            data = json.loads(file.read())
        return data

    def fetch_movies(self):
        movie_list = []
        list = self.read_from_file()
        for item in list['movies']:
            trailer_id = self.get_youtube_id(item["youtube_trailer_url"])
            movie = Movie(item["title"], item["storyline"], item["poster_image_url"], trailer_id)
            movie_list.append(movie)
        return movie_list

    def get_youtube_id(self, url):
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)
        return trailer_youtube_id
