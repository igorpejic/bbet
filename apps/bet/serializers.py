from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Song, Bet, Position, Week, BetItem


class LastWeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        depth = 1
        fields = ('id', 'name', 'artist',)


class BetItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BetItem
        fields = ('choice', 'song', 'odd')


class BetSerializer(serializers.ModelSerializer):
    bets = BetItemSerializer(many=True)

    class Meta:
        model = Bet
        fields = ('bet_type', 'bets', 'stake')


class CreateBetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bet
        fields = ('bet_type',)


class AddBetSerializer(serializers.Serializer):
    song = serializers.CharField(max_length=200)
    choice = serializers.CharField(max_length=5)
    bet_id = serializers.PrimaryKeyRelatedField(queryset=Bet.objects.all())


class BetHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bet


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        depth = 1


class WeeksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Week
        exclude = ('songs',)


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        depth = 2
        fields = ('position', 'song', 'odd_1', 'odd_2', 'odd_x')


class WeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Week
        depth = 1


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class SocialAuthSerializer(serializers.Serializer):

    """
    Serializer to receive social auth for python-social-auth
    """
    backend = serializers.CharField()
    access_token = serializers.CharField()
