from rest_framework import serializers

from .models import ListOfBet, Song


class NewBetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListOfBet


class WeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        depth = 1
        fields = ('name', 'artist',)
