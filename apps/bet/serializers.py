from rest_framework import serializers

from .models import ListOfBet, Week


class NewBetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListOfBet


class WeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Week
        depth = 1
