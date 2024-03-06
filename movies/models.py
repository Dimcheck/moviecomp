# Create your models here.
from django.db import models
from django.conf import settings


class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateTimeField(blank=True, null=True)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str([self.name, self.director, self.release_date])

