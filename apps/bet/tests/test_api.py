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

    def test_return_only_latest_week_positions(self):
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
        self.assertEqual(response.data[0]['id'], self.last_week.id)


class BetView(APITestCase):
    def setUp(self):
        today = datetime.date.today()
        sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=2)
        self.song = mommy.make(Song, name='foo')
        self.last_week = mommy.make(Week, date=sunday)
        self.some_week = mommy.make(Week, date=sunday-datetime.timedelta(weeks=2))
        self.user = mommy.make(User)

    def test_user_cant_make_his_points_negative(self):
        mommy.make(Better, user=self.user, points=2)
        self.last_week_position = mommy.make(Position, song=self.song, week=self.last_week)
        self.some_week_position = mommy.make(Position, week=self.some_week)

        self.url = reverse('api:bet')
        self.client.force_authenticate(user=self.user)
        self.data = {'stake': 3, 'bet_type': 3, 'date': self.last_week.date,
                     'bets': [{'choice': 1, 'song': self.song.id}]}

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Insufficient points.'})

    def test_user_cant_bet_without_stake(self):
        mommy.make(Better, user=self.user, points=2)
        self.last_week_position = mommy.make(Position, song=self.song, week=self.last_week)
        self.some_week_position = mommy.make(Position, week=self.some_week)

        self.url = reverse('api:bet')
        self.client.force_authenticate(user=self.user)
        self.data = {'stake': 0, 'bet_type': 3, 'date': self.last_week.date,
                     'bets': [{'choice': 1, 'song': self.song.id}]}

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'No bet stake.'})

    def test_can_bet_only_on_last_week(self):
        mommy.make(Better, user=self.user, points=2)
        self.last_week_position = mommy.make(Position, song=self.song, week=self.last_week)
        self.some_week_position = mommy.make(Position, week=self.some_week)

        self.url = reverse('api:bet')
        self.client.force_authenticate(user=self.user)
        self.data = {'stake': 2, 'bet_type': 3, 'date': self.some_week.date,
                     'bets': [{'choice': 1, 'song': self.song.id}]}

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Invalid week.'})

    def test_chooses_odd_based_on_choice(self):
        self.song_X = mommy.make(Song, name='foobar')
        self.better = mommy.make(Better, user=self.user, points=5)
        self.last_week_position = mommy.make(Position, song=self.song, week=self.last_week,
                                             odd_1='2.0')
        mommy.make(Position, song=self.song_X, week=self.last_week,
                   odd_x='8.0')
        self.some_week_position = mommy.make(Position, week=self.some_week)

        self.url = reverse('api:bet')
        self.client.force_authenticate(user=self.user)
        self.data = {'stake': 3, 'bet_type': 3, 'date': self.last_week.date,
                     'bets': [{'choice': '1', 'song': self.song.id},
                              {'choice': 'X', 'song': self.song_X.id}]}

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.better.bet_set.all()[0].stake, 3)
        self.assertEqual(self.better.bet_set.all()[0].betitem_set.all()[0].odd, 2.0)
        self.assertEqual(self.better.bet_set.all()[0].betitem_set.all()[1].odd, 8.0)

    def test_bad_request(self):
        '''
        4 is invalid bet_type
        '''
        self.song_X = mommy.make(Song, name='foobar')
        self.better = mommy.make(Better, user=self.user, points=5)
        self.last_week_position = mommy.make(Position, song=self.song, week=self.last_week,
                                             odd_1='2.0')
        mommy.make(Position, song=self.song_X, week=self.last_week,
                   odd_x='8.0')
        self.some_week_position = mommy.make(Position, week=self.some_week)

        self.url = reverse('api:bet')
        self.client.force_authenticate(user=self.user)
        self.data = {'stake': 3, 'bet_type': 4, 'date': self.last_week.date,
                     'bets': [{'choice': '1', 'song': self.song.id},
                              {'choice': 'X', 'song': self.song_X.id}]}

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
