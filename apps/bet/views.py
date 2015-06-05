import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Week, Position, ListOfBet
from .serializers import NewBetSerializer, WeekSerializer


class PermissionView(GenericAPIView):

    permission_classes = (IsAuthenticated,)


class NormalBetViewSet(ModelViewSet, PermissionView):
    serializer_class = NewBetSerializer
    queryset = ListOfBet.objects.all()


class WeekViewSet(ReadOnlyModelViewSet, PermissionView):
    serializer_class = WeekSerializer
    queryset = Week.objects.all()


def current_week(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/bet/week/')
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
    print sunday
    week = Week.objects.get(date=sunday)
    songs = Position.objects.filter(week=week)

    return render(request, 'bet/normal_bet.html', {'songs': songs})
