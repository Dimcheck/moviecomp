from movies.views import MovieCreate, MovieList, MovieRetrive

from django.urls import path


app_name = 'movies'

urlpatterns = [
    path('movie', MovieCreate.as_view(), name='movies_create'),
    path('movie/<int:pk>', MovieRetrive.as_view(), name='movies_get_one'),
    path('movies/', MovieList.as_view(), name='movies_get'),
]