from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=False)
    message = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Countries(models.Model):
    country_name = models.CharField(max_length=100)


class Movie(models.Model):

    title = models.CharField(max_length=100, unique=False, null=True)
    rating = models.CharField(max_length=100, unique=False, null=True)
    year = models.CharField(max_length=100, unique=False, null=True)
    user_rating = models.CharField(max_length=100, unique=False, null=True)
    votes = models.CharField(max_length=100, unique=False, null=True)
    metascore = models.CharField(max_length=100, null=True, )
    img_url = models.CharField(max_length=100, unique=False, null=True)
    description = models.CharField(max_length=100, unique=False, null=True)
    runtime = models.CharField(max_length=100, unique=False, null=True)
    imdb_url = models.CharField(max_length=100, unique=True, null=True)
    tagline = models.CharField(max_length=100, null=True, )
    countries = models.ManyToManyField(Countries)





