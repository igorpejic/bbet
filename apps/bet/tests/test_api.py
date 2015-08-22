import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from model_mommy import mommy

from apps.bet.models import(
    Bet, Better, Week, Position, Song
)


class MyBetsViewTest(APITestCase):

    def setUp(self):
        today = datetime.date.today()
        sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=2)
        mommy.make(Week, date=sunday)

    def test_dont_return_other_user_bets(self):
        self.user = mommy.make(User)
        mommy.make(Better, user=self.user)
        self.other_user = mommy.make(User)
        mommy.make(Better, user=self.other_user)
        mommy.make(Bet, better=self.user.better)
        mommy.make(Bet, better=self.user.better)
        mommy.make(Bet, better=self.other_user.better)

        self.url = reverse('api:mybets-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class LastWeekViewSetTest(APITestCase):
    def setUp(self):
        today = datetime.date.today()
        sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=2)
        self.song = mommy.make(Song, name='foo')
        self.last_week = mommy.make(Week, date=sunday)
        self.some_week = mommy.make(Week, date=sunday-datetime.timedelta(weeks=2))

    def test_return_only_latest_week(self):
        self.user = mommy.make(User)
        mommy.make(Better, user=self.user)
        self.other_user = mommy.make(User)
        mommy.make(Better, user=self.other_user)
        self.last_week_position = mommy.make(Position, song=self.song, week=self.last_week)
        self.some_week_position = mommy.make(Position, week=self.some_week)

        self.url = reverse('api:lastweek-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['song']['name'], 'foo')
