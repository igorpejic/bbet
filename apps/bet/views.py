import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import Week, Position, BetItem, Song, Bet
from .serializers import(
    CreateBetSerializer, WeekSerializer, LastWeekSerializer,
    AddBetSerializer, BetHistorySerializer, SongSerializer, PositionSerializer,
    WeeksSerializer, BetSerializer
)


class PermissionView(GenericAPIView):

    permission_classes = (IsAuthenticated,)


class BetView(PermissionView):

    def post(self, request):
        serialized = BetSerializer(data=request.DATA)
        if serialized.is_valid():
            user = request.user.better
            bet = Bet.objects.create(user=user, bet_type=serialized.data['bet_type'])
            for serialized_bet in serialized.data['bets']:
                BetItem.objects.create(
                    bet=bet,
                    song=Song.objects.get(id=serialized_bet['song']),
                    choice=serialized_bet['choice'])
            return Response(
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
            song_id = data['song']
            song = Song.objects.get(id=song_id)
            choice = data['choice']
            BetItem.objects.create(bet=bet, song=song, choice=choice)
            return Response(
                status=status.HTTP_201_CREATED
            )
        return Response(
            serialized.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LastWeekViewSet(ReadOnlyModelViewSet, PermissionView):
    serializer_class = PositionSerializer
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
    week = Week.objects.get(date=sunday)
    queryset = Position.objects.filter(week__id=week.id).order_by('position')


def current_week(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/bet/week/')
    today = datetime.date.today()
    sunday = today + datetime.timedelta(days=-today.weekday() - 2, weeks=1)
    week = Week.objects.get(date=sunday)
    songs = week.songs.all()

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
        song = Song.objects.get(id=pk)
        positions = PositionSerializer(song.position_set.all(), many=True)
        return Response(
            positions.data,
            status=status.HTTP_200_OK
        )


class WeekViewSet(ReadOnlyModelViewSet, PermissionView):
    queryset = Week.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return WeeksSerializer
        if self.action == 'retrieve':
            return WeekSerializer
        return WeekSerializer
