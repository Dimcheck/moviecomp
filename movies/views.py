from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.helpers import take_random_movie

from enjoyers import permissions as custom_permissions

from rest_framework.response import Response
from rest_framework import generics, views, status, permissions


class MovieList(generics.ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filterset_fields = ('release_date', 'director', 'cast')


class MovieRetrive(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [custom_permissions.IsSuperUserOrReadOnly]


class MovieCreate(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, *args, **kwargs):
        serializer = MovieSerializer(data=take_random_movie())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

