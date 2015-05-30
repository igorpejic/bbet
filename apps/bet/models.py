from django.db import models
from django.contrib.auth.models import User


class Better(User):
    points = models.IntegerField(default=100)
    for_week = models.IntegerField(default=0)


class Song(models.Model):
    name = models.CharField(max_length=200)
    youTube_link = models.URLField()


class Betting(models.Model):
    user = models.ForeignKey(Better)
    date_time = models.DateTimeField(auto_now_add=True)
    is_won = models.BooleanField(default=False)
    models.ManyToManyField(Song, through='ListOfBets')


class ListOfBets(models.Model):
    bet_id = models.ForeignKey(Betting)
    song = models.ForeignKey(Song)
    unique_together = ("bet_id", "song")
    data = models.CharField(max_length=20)


class Artist(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    models.ManyToManyField(Song, through='Collaboration')


class Collaboration(models.Model):
    artist_id = models.ForeignKey(Artist)
    song = models.ForeignKey(Song)
    unique_together = ("artist_id", "song")
