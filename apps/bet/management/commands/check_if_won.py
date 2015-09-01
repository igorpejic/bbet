import datetime
from datetime import timedelta

from apps.bet.models import Bet, Week, Position, Better

from django.core.management.base import BaseCommand


def check_if_won(existing_week, new_week):
    today = datetime.date.today()
    sunday_current = today + datetime.timedelta(days=-today.weekday() - 2)
    #sunday_latest = today + datetime.timedelta(days=-today.weekday() - 2, weeks=2)
    
    if (existing_week and new_week):
       sunday_pending = new_week
       sunday_latest = existing_week
       print(sunday_latest)
       print(sunday_pending)
    else:
        print("error with dates....exiting")
        return

    week = Week.objects.filter(date=sunday_pending)
    position_set_to_compare = Position.objects.filter(week=week)         
    week = Week.objects.filter(date=sunday_latest)
    position_set_current = Position.objects.filter(week=week)
    #print(position_set_current)
    #print(position_set_to_compare)

    for bet in Bet.objects.filter(date_time__gte=sunday_current):
        odds_total = 0
        if (bet.has_won != 'Pending'):
            print(bet)
            continue
        for betItem in bet.betitem_set.all():
            position_item_to_compare = check_if_song_exists(betItem.song, position_set_to_compare)
            position_item_current = check_if_song_exists(betItem.song, position_set_current)
            odds_total += betItem.odd
            if betItem.choice != check_single_song(position_item_current[0].position,
                                                   position_item_to_compare[0].position):
                print("not a god bet", bet.date_time, betItem.song, betItem.choice)
                bet.has_won = 'False'
                bet.save()
                break
            else:
                print("good bet", bet.date_time, betItem.song, betItem.choice)
        if bet.has_won == 'Pending':
            bet.has_won = 'True'
            bet.save()
            user = Better.objects.get(user__username=bet.better)
            points_wining = bet.stake*odds_total
            user.points += points_wining
            user.save()


def check_single_song(song_position_current, song_position_to_compare):
    '''returns corresponding bet choices based on changes between last week
    and new week songs position
    '''
    if song_position_to_compare < song_position_current:
        return '1'
    elif song_position_to_compare == song_position_current:
        return 'X'
    else:
        return '2'


def check_if_song_exists(betItem_song, position_set):
    '''returns one position object which purpose is to provide position for comparison
    '''
    item = [item for item in position_set if betItem_song == item.song ]
    # print ([item for item in to_compare_set if 1])
    '''
     if item == "":
        return ["101", "2015-08-08", "XXX"]
    TODO: make a false queryset with position 101 or above
    '''
    return item


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('week', nargs='+', type=Week)

    def handle(self, *args, **options):
        check_if_won(args[0], args[1])
