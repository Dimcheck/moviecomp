from random import randint
from rest_framework.response import Response
from datetime import datetime

import json
import requests


def take_random_movie() -> Response | dict:
    imdb_id = randint(1000000, 2000000)

    try:
        movie = requests.get(url=f'https://www.omdbapi.com/?i=tt{imdb_id}&apikey=5628d32f')
        movie = json.loads(movie.content)
        result = {
            "name": movie.get("Title"),
            # "release_date": datetime.strptime(movie.get("Released"), "%d %b %Y"),
            "release_date": datetime.strptime(movie.get("Year"), "%Y"),
            "director": movie.get("Director"),
            "cast": movie.get("Actors"),
        }
    except (TypeError, ValueError):
        return {
            "name": movie.get("Title"),
            "director": movie.get("Director"),
            "cast": movie.get("Actors"),
        }

    return result

