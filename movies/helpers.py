from random import randint
from rest_framework.response import Response
from datetime import datetime

import json
import requests
import os


def take_random_movie() -> Response | dict:
    imdb_id = randint(1000000, 2000000)
    omdb_key = os.getenv("OMDB_KEY")

    try:
        movie = requests.get(url=f'https://www.omdbapi.com/?i=tt{imdb_id}&apikey={omdb_key}')
        movie = json.loads(movie.content)
        result = {
            "name": movie.get("Title"),
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

