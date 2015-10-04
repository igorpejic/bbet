import datetime
from datetime import timedelta

from apps.bet.models import Bet, Week, Position, Better

from django.core.management.base import BaseCommand


def check_if_won(last_week, this_week):
    assert last_week, this_week

    position_set_last_week = Position.objects.filter(week=last_week)
    position_set_this_week = Position.objects.filter(week=this_week)

    for bet in Bet.objects.filter(week=last_week):
        odds_total = 0
        if (bet.has_won != 'Pending'):
            continue
        for betItem in bet.betitem_set.all():
            position_item_this_week = check_if_song_exists(betItem.song, position_set_this_week)
            position_item_last_week = check_if_song_exists(betItem.song, position_set_last_week)
            print position_item_this_week
            odds_total += betItem.odd
            if betItem.choice != check_single_song(position_item_last_week[0].position,
                                                   position_item_this_week[0].position):
                print("not a god bet", bet.date_time, betItem.song, betItem.choice)
                bet.has_won = 'False'
                bet.save()
                break
            else:
                print("good bet", bet.date_time, betItem.song, betItem.choice)
        if bet.has_won == 'Pending':
            bet.has_won = 'True'
            bet.save()
            winning_points = bet.stake*odds_total
            better = bet.better
            better.points += winning_points
            better.save()


def check_single_song(song_position_last_week, song_position_this_week):
    '''returns corresponding bet choices based on changes between last week
    and this week songs position
    '''
    # Song fell off the chart
    if not song_position_this_week:
        return '2'

    if song_position_last_week > song_position_this_week:
        return '1'
    elif song_position_last_week == song_position_this_week:
        return 'X'
    else:
        return '2'


def check_if_song_exists(betItem_song, position_set):
    '''returns one position object which purpose is to provide position for comparison
    '''
    item = [item for item in position_set if betItem_song == item.song ]
    return item


class Command(BaseCommand):

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('week', nargs='+', type=Week)

    def handle(self, *args, **options):
        check_if_won(args[0], args[1])
