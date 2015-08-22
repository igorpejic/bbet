from datetime import date
from datetime import timedelta
import random

from apps.bet.models import Week, Position

from django.core.management.base import BaseCommand


def populate_odds():
    today = date.today()
    week_sunday = today + timedelta(days=-today.weekday() - 2,
                                    weeks=1) + timedelta(days=7)
    week = Week.objects.get(date=week_sunday)
    random.seed()
    for position in Position.objects.filter(week=week):
        position.odd_1 = int((random.uniform(1, 3) * 100) + 0.5) / 100.0
        position.odd_2 = int((random.uniform(1, 3) * 100) + 0.5) / 100.0
        position.odd_x = int((random.uniform(1, 3) * 100) + 0.5) / 100.0
        position.save()


class Command(BaseCommand):
    populate_odds()

    def handle(self, *args, **options):
        pass
