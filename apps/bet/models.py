from django.db import models
from django.contrib.auth.models import User


class Better(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=100)

    def __unicode__(self):
        return unicode(self.user.username)


class Artist(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return unicode(self.name)


class Song(models.Model):
    name = models.CharField(max_length=200)
    youtube_link = models.URLField(null=True, blank=True)
    artist = models.ForeignKey(Artist)
    # billboard like name
    artist_name = models.CharField(max_length=250)

    def __unicode__(self):
        return unicode(self.name)


TYPE_CHOICES = (
    ('1', 'Top 10'),
    ('2', 'Top 20'),
    ('3', '1x2'),
)

RESULT_CHOICES = (
    ('True', 'True'),
    ('False', 'False'),
    ('Pending', 'Pending'),
)


class Bet(models.Model):
    better = models.ForeignKey(Better)
    date_time = models.DateTimeField(auto_now_add=True)
    has_won = models.CharField(max_length=20, choices=RESULT_CHOICES,
                               default='Pending')
    bet_type = models.CharField(max_length=20, choices=TYPE_CHOICES,
                                default='3')
    stake = models.FloatField()

    def __unicode__(self):
        return unicode('{} {}'.format(self.user, self.date_time))


BET_CHOICES = (
    ('1', 'Will rise'),
    ('X', 'Will stay'),
    ('2', 'Will fall'),
)


class BetItem(models.Model):
    bet = models.ForeignKey(Bet)
    song = models.ForeignKey(Song)
    unique_together = ("bet", "song")
    choice = models.CharField(max_length=20, choices=BET_CHOICES)
    odd = models.FloatField()

    def __unicode__(self):
        return unicode('{} {} {}'.format(self.bet, self.song, self.choice))


class Collaboration(models.Model):
    artist = models.ForeignKey(Artist)
    song = models.ForeignKey(Song)
    unique_together = ("artist", "song")


class Week(models.Model):
    date = models.DateField()
    songs = models.ManyToManyField(Song, through="Position")

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return unicode(self.date)


class Position(models.Model):
    week = models.ForeignKey(Week)
    song = models.ForeignKey(Song)
    position = models.SmallIntegerField()
    odd_1 = models.FloatField(blank=True, null=True)
    odd_x = models.FloatField(blank=True, null=True)
    odd_2 = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ['week']

    def __unicode__(self):
        return '{} {} {}'.format(self.position, self.week.date, self.song.name)

# GENRE_CHOICES(
    # ('1', 'rock'),
    # ('2,', 'pop'),
    # ('3', 'tehno'),
# )


class Genre(models.Model):
    genre = models.ForeignKey(Song)
    # genre_type = models.CharField(max_length=20, choices=GENRE_CHOICES)
