from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from leads.models import Lead, Movie
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, MovieSerializer

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

