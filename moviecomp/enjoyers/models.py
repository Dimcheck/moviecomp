from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


class MovieEnjoyer(AbstractUser):

    def __str__(self) -> str:
        return str([self.username, self.password])


class PersonalComp(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(MovieEnjoyer, related_name='compilation', on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, related_name='compilation', blank=True)

    def __str__(self) -> str:
        return str([self.name, self.user])
