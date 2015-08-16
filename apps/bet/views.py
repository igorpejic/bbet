import requests
import json
import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings


from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

from .models import Week, Position, BetItem, Song, Bet, Better
from .serializers import(
    WeekSerializer,
    AddBetSerializer, BetHistorySerializer, SongSerializer, PositionSerializer,
    WeeksSerializer, BetSerializer, UserSerializer,
    SocialAuthSerializer
)


class PermissionView(GenericAPIView):

    permission_classes = (IsAuthenticated,)


class BetView(PermissionView):

    serializer_class = BetSerializer

    def post(self, request):
        serialized = BetSerializer(data=request.DATA)
        if serialized.is_valid():
            better = request.user.better
            if serialized.data['stake'] <= 0:
                return Response(
                    {'error': 'No bet stake.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            bet = Bet.objects.create(better=better, bet_type=serialized.data['bet_type'],
                                     stake=serialized.data['stake'])
            for serialized_bet in serialized.data['bets']:
                BetItem.objects.create(
                    bet=bet,
                    song=Song.objects.get(id=serialized_bet['song']),
                    odd=serialized_bet['odd'],
                    choice=serialized_bet['choice'])
            better.points -= serialized.data['stake']
            better.save()
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


class RegisterView(GenericAPIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serialized = UserSerializer(data=request.DATA)
        if serialized.is_valid():
            try:
                user = User.objects.create_user(
                    serialized.data['username'],
                    serialized.data['email'],
                    serialized.data['password']
                )
                Better.objects.create(user=user)
            except IntegrityError:
                return Response({'error': 'User with that email already exists.'},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response({'error': 'A field is missing.'},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class SocialAuthView(APIView):

    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        access_token_url = 'https://accounts.google.com/o/oauth2/token'
        people_api_url = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'

        payload = dict(client_id=request.data['clientId'],
                       redirect_uri=request.data['redirectUri'],
                       client_secret=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                       code=request.data['code'],
                       grant_type='authorization_code')

        # Step 1. Exchange authorization code for access token.
        r = requests.post(access_token_url, data=payload)
        token = json.loads(r.text)
        headers = {'Authorization': 'Bearer {0}'.format(token['access_token'])}

        # Step 2. Retrieve information about the current user.
        r = requests.get(people_api_url, headers=headers)
        profile = json.loads(r.text)

        user = None
        if 'email' in profile:
            try:
                user = User.objects.get(email=profile['email'])
            except User.DoesNotExist:
                pass

        if not user:
            user = User.objects.create(username=profile['email'], first_name=profile['given_name'],
                                       last_name=profile['family_name'], email=profile['email'])
            Better.objects.create(user=user)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token.decode('unicode_escape')},
                        status=status.HTTP_200_OK)


class SocialFacebookView(APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    social_serializer = SocialAuthSerializer
    user_serializer = None

    def post(self, request):
        access_token_url = 'https://graph.facebook.com/v2.3/oauth/access_token'
        people_api_url = 'https://graph.facebook.com/v2.3/me'

        payload = dict(client_id=request.data['clientId'],
                       redirect_uri=request.data['redirectUri'],
                       client_secret=settings.SOCIAL_AUTH_FACEBOOK_SECRET,
                       code=request.data['code'],
                       scope='email',
                       )

        # Step 1. Exchange authorization code for access token.
        r = requests.post(access_token_url, data=payload)
        token = json.loads(r.text)
        headers = {'Authorization': 'Bearer {0}'.format(token['access_token']), 'scope': 'email'}

        # Step 2. Retrieve information about the current user.
        r = requests.get(people_api_url, headers=headers)
        profile = json.loads(r.text)

        user = None
        if 'email' in profile:
            try:
                user = User.objects.get(email=profile['email'])
            except User.DoesNotExist:
                pass
        else:
            try:
                user = User.objects.get(email=profile['id'] + '@facebook.com')
            except User.DoesNotExist:
                pass
            profile['email'] = profile['id'] + '@facebook.com'

        if not user:
            user = User.objects.create(username=profile['email'],
                                       first_name=profile['name'].split()[0],
                                       last_name=profile['name'].split()[1],
                                       email=profile['email'])
            Better.objects.create(user=user)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token.decode('unicode_escape')},
                        status=status.HTTP_200_OK)


class SocialUserView(PermissionView):

    def get(self, request):
        name = request.user.first_name + " " + request.user.last_name
        betting_funds = request.user.better.points

        return Response({'name': name, 'betting_funds': betting_funds},
                        status=status.HTTP_200_OK)


class LeaderboardView(PermissionView):

    def get(self, request):
        betters = Better.objects.all().order_by('-points')[:100]
        serialized_betters = []
        for better in betters:
            serialized_better = {}
            serialized_better['name'] = better.user.first_name + " " + better.user.last_name
            serialized_better['points'] = better.points
            serialized_better['user_id'] = better.user.id
            serialized_betters.append(serialized_better)
        return Response({'users': serialized_betters}, status=status.HTTP_200_OK)
