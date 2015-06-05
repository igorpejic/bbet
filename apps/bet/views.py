import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import Week, Position, ListOfBet
from .serializers import NewBet
from rest.framework.viewsets import ModelViewSet
from rest.framework.generics import GenericAPIView
from rest.framework.permissions import IsAuthenticated


class PermissionView(GenericAPIView):

    permission_classes = (IsAuthenticated,)


class NormalBetViewSet(ModelViewSet, PermissionView):
    serializer_class = NewBet
    queryset = ListOfBet.objects.all()


def current_week(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/bet/week/')
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
    print sunday
    week = Week.objects.get(date=sunday)
    songs = Position.objects.filter(week=week)

    return render(request, 'bet/normal_bet.html', {'songs': songs})
