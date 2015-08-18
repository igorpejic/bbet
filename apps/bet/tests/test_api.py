import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from model_mommy import mommy

from apps.bet.models import Bet, Better, Week


class MyBetsViewTest(APITestCase):

    def setUp(self):
        today = datetime.date.today()
        sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
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
