import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.serializers import serialize

from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import Week, Position, ListOfBet, Song, Bet
from .serializers import(
    CreateBetSerializer, WeekSerializer,
    AddBetSerializer, BetHistorySerializer, SongSerializer, PositionSerializer,
)


class PermissionView(GenericAPIView):

    permission_classes = (IsAuthenticated,)


class BetView(PermissionView):

    serializer_class = CreateBetSerializer

    def post(self, request):
        serialized = CreateBetSerializer(data=request.DATA)
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


class AddBetView(PermissionView):

    serializer_class = AddBetSerializer

    def post(self, request):
        serialized = AddBetSerializer(data=request.DATA)
        if serialized.is_valid():
            data = serialized.data
            bet_id = data['bet_id']
            bet = Bet.objects.get(id=bet_id)
            song_name = data['song']
            song = Song.objects.filter(name=song_name)[0]
            choice = data['choice']
            ListOfBet.objects.create(bet=bet, song=song, choice=choice)
            return Response(
                status=status.HTTP_201_CREATED
            )
        return Response(
            serialized.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


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


class BetHistoryViewSet(ReadOnlyModelViewSet, PermissionView):
    serializer_class = BetHistorySerializer

    def get_queryset(self):
        user = self.request.user.better
        return Bet.objects.filter(user=user)


class SongViewSet(ReadOnlyModelViewSet, PermissionView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()


class PositionViewSet(PermissionView):
    serializer_class = PositionSerializer

    def get(self, request, pk):
        print pk
        song = Song.objects.get(id=pk)
        positions = PositionSerializer(song.position_set.all(), many=True)
        return Response(
            positions.data,
            status=status.HTTP_400_BAD_REQUEST
        )
