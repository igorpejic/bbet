import time
from datetime import datetime

import urllib

from bs4 import BeautifulSoup
from apps.bet.models import Week, Song, Position, Artist
from datetime import timedelta

from django.core.management.base import BaseCommand


class WeeklyChart(object):

    def __init__(self, url):
        self.url = url

        sock = urllib.urlopen(url)
        htmlSource = sock.read()
        sock.close()
        soup = BeautifulSoup(htmlSource)
        x = []
        y = []
        chart = []
        for node in soup.select(".row-title > h2"):
            x.append(''.join(node.findAll(text=True)).strip())
        for node in soup.select(".row-title > h3"):
            y.append(''.join(node.findAll(text=True)).strip())

        chart = zip(x, y)

        week_time = time.strptime(soup.time.text, "%B %d, %Y")
        dt = datetime.fromtimestamp((time.mktime(week_time)))
        this_week = Week.objects.get_or_create(date=dt)[0]

        for position, (song_name, artist_name) in enumerate(chart):
            song = Song.objects.get_or_create(name=song_name)[0]
            artist = Artist.objects.get_or_create(name=artist_name)[0]
            artist.songs.add(song)
            artist.save()
            Position.objects.get_or_create(week=this_week, song=song,
                                           position=position + 1)


def populate():
    url = 'http://www.billboard.com/charts/hot-100'
    WeeklyChart(url)
    url += '/'
    week_time = time.strptime('May 30, 2015', "%B %d, %Y")
    week = datetime.fromtimestamp(time.mktime(week_time))
    date_week = week.date()
    time_delta = timedelta(days=-7)
    for i in xrange(10):
        WeeklyChart(url + str(date_week))
        date_week = date_week + time_delta
        print date_week


class Command(BaseCommand):
    populate()

    def handle(self, *args, **options):
        pass
