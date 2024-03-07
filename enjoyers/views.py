from enjoyers.models import MovieEnjoyer, PersonalComp
from enjoyers import permissions as custom_permissions
from enjoyers.serializers import (
    MovieEnjoyerDetailSerializer,
    MovieEnjoyerCreateSerializer,
    PersonalCompDetailSerializer,
    PersonalCompCreateSerializer,
    AddMovieSerializer,
)

from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions


class MovieEnjoyersCreate(generics.CreateAPIView):
    """Create User"""

    serializer_class = MovieEnjoyerCreateSerializer

    def post(self, request, *args, **kwargs):
        if request.data.get('password'):
            request.data['password'] = make_password(request.data['password'])
        return super().post(request, *args, **kwargs)


class MovieEnjoyersRetrieve(generics.RetrieveUpdateDestroyAPIView):
    """
    Get User by it's ID and if you have enough permission you can manage it
    """

    serializer_class = MovieEnjoyerDetailSerializer
    queryset = MovieEnjoyer.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsTheUserOrReadOnly,
    ]


class MovieEnjoyersList(generics.ListAPIView):
    """Get all Users with their PerspnalCompilations"""

    serializer_class = MovieEnjoyerDetailSerializer
    queryset = MovieEnjoyer.objects.all()


class PersonalCompAppend(generics.RetrieveUpdateDestroyAPIView):
    """
    Get PersonalCompilation, if you have enough permission - manage it
    To extend compilation, add Movie IDs to it.
    """

    serializer_class = AddMovieSerializer
    queryset = PersonalComp.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly,
    ]


class PersonalCompCreate(generics.CreateAPIView):
    """
    Create PersonalCompilation
    """

    serializer_class = PersonalCompCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PersonalCompList(generics.ListAPIView):
    """
    Get all PersonalCompilation
    """

    serializer_class = PersonalCompDetailSerializer
    queryset = PersonalComp.objects.all()

