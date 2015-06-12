from rest_framework import serializers

from .models import Song, Bet, Position, Week


class WeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        depth = 1
        fields = ('id', 'name', 'artist',)


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
        fields = ('artist', 'name', 'id')


class WeeksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Week
        exclude = ('songs',)


class PositionSerializer(serializers.ModelSerializer):
    week = WeeksSerializer()

    class Meta:
        model = Position
        depth = 1
        exclude = ('id', 'song')
