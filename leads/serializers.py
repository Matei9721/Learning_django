from rest_framework import serializers
from leads.models import Lead, Movie, Countries, Actors


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['country_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ['actor_name']


class MovieSerializer(serializers.ModelSerializer):
    countries = CountriesSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'



