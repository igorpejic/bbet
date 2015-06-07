import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import Week, Position, ListOfBet, Song, Bet
from .serializers import NewBetSerializer, WeekSerializer, BetSerializer


class PermissionView(GenericAPIView):

    permission_classes = (IsAuthenticated,)


class BetView(PermissionView):

    serializer_class = BetSerializer

    def post(self, request):
        serialized = BetSerializer(data=request.DATA)
        if serialized.is_valid():
            user = request.user.better
            bet_type = serialized.data['bet_type']
            bet = Bet.objects.create(bet_type=bet_type, user=user)

            return Response(
                {'bet_id': bet.id},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serialized._errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class NormalBetViewSet(PermissionView):
    def post(self, request):
        serialized = NewBetSerializer(data=request.DATA)
        if serialized.is_valid():
            user = request.user


class WeekViewSet(ReadOnlyModelViewSet, PermissionView):
    serializer_class = WeekSerializer
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
    week = Week.objects.get(date=sunday)
    queryset = Song.objects.filter(week__id=week.id)


def current_week(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/bet/week/')
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
    week = Week.objects.get(date=sunday)
    songs = Position.objects.filter(week=week)

    return render(request, 'bet/normal_bet.html', {'songs': songs})
