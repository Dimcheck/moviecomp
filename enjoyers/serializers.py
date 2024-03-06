from rest_framework import serializers
from enjoyers.models import MovieEnjoyer, PersonalComp


class PersonalCompCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalComp
        fields = ['name']


class AddMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalComp
        fields = ['name', 'movies']


class PersonalCompDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    movies = serializers.StringRelatedField(many=True)

    class Meta:
        model = PersonalComp
        fields = ['id', 'user', 'name', 'movies']


class MovieEnjoyerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieEnjoyer
        fields = ['username', 'password']


class MovieEnjoyerDetailSerializer(serializers.ModelSerializer):
    compilation = serializers.PrimaryKeyRelatedField(
        queryset=PersonalComp.objects.all(),
        many=True,
    )

    class Meta:
        model = MovieEnjoyer
        fields = ['id', 'username', 'date_joined', "compilation"]
