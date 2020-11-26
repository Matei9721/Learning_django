from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


from leads.models import Lead, Movie, Countries, Actors
from rest_framework import viewsets, permissions, views
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
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title', 'year', 'countries__country_name']
    search_fields = ['countries__country_name', 'title']
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
