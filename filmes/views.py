from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.admin import User
from filmes.models import Actor, Movie
from filmes.serializers import ActorSerializer, MovieSerializer


# Create your views here.
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer