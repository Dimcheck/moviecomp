from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.helpers import take_random_movie

from rest_framework.response import Response
from rest_framework import generics, views, status, permissions


class MovieList(generics.ListAPIView):
    """Get all movies with filter options"""

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filterset_fields = ('name', 'release_date', 'director', 'cast')


class MovieRetrive(generics.RetrieveUpdateDestroyAPIView):
    """
    Get movie by it's ID and if you have enough permission you can manage it
    """

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieCreate(views.APIView):
    """Adds random movie from OMDBAPI"""

    serializer_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, *args, **kwargs):
        serializer = MovieSerializer(data=take_random_movie())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

