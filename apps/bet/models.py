from django.db import models
from django.contrib.auth.models import User


class Better(User):
    points = models.IntegerField(default=100)


class Song(models.Model):
    name = models.CharField(max_length=200)
    youTube_link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)

TYPE_CHOICES = (
    ('1', 'Top 10'),
    ('2', 'Top 20'),
    ('3', '1x2'),
)

class Bet(models.Model):
    user = models.ForeignKey(Better)
    date_time = models.DateTimeField(auto_now_add=True)
    has_won = models.BooleanField(default=False)
    bet_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    models.ManyToManyField(Song, through='ListOfBets')


BET_CHOICES = (
    ('1', 'Will rise'),
    ('x', 'Will stay'),
    ('2', 'Will fall'),
)


class ListOfBet(models.Model):
    bet = models.ForeignKey(Bet)
    song = models.ForeignKey(Song)
    unique_together = ("bet", "song")
    data = models.CharField(max_length=20, choices=BET_CHOICES)


class Artist(models.Model):
    name = models.CharField(max_length=250)
    songs = models.ManyToManyField(Song)
    # models.ManyToManyField(Song, through='Collaboration')

    def __unicode__(self):
        return unicode(self.name)


# Will be presented as if it existed in documentation
# class Collaboration(models.Model):
    # artist = models.ForeignKey(Artist)
    # song = models.ForeignKey(Song)
    # unique_together = ("artist", "song")


class Week(models.Model):
    date = models.DateField()
    songs = models.ManyToManyField(Song, through="Position")

    def __unicode__(self):
        return unicode(self.date)


class Position(models.Model):
    week = models.ForeignKey(Week)
    song = models.ForeignKey(Song)
    position = models.SmallIntegerField()

    def __unicode__(self):
        return '{} {} {}'.format(self.position, self.week.date, self.song.name)

#GENRE_CHOICES(
    #('1', 'rock'),
    #('2,', 'pop'),
    #('3', 'tehno'),
#)

class Genre(models.Model):
    genre = models.ForeignKey(Song)
    #genre_type = models.CharField(max_length=20, choices=GENRE_CHOICES)
    
