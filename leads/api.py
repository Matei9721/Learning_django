from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from leads.models import Lead, Movie, Countries, Actors
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, MovieSerializer, CountriesSerializer

import json


# Lead ViewSet
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id', 'name', 'email', 'message']

    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title', 'year']

    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


json_data = open('leads/fixtures/movie.json')
data1 = json.load(json_data)  # deserialises it
data2 = json.dumps(data1)  # json formatted string

json_data.close()

#################### Populate the database
for film in data1:
    Movie.objects.update_or_create(title=film['title'], rating=film['rating'], year=film['year'],
                                   user_rating=film['users_rating'],
                                   votes=film['votes'],
                                   metascore=film['metascore'], img_url=film['img_url'],
                                   description=film['description'],
                                   runtime=film['runtime'], imdb_url=film['imdb_url'], tagline=film['tagline'])
    mov = Movie.objects.create(title='Test din json')
    for nume_tara in film['countries']:
        mov.countries.create(country_name=nume_tara)
    for nume_actor in film['actors']:
        mov.actors.create(actor_name=nume_actor)


