from rest_framework import serializers

from filmes.models import Actor, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["create_date","name","age"]

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["name", "actor"]