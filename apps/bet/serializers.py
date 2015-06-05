from rest_framework import serializers

from .models import Bet, ListOfBet


class NewBet(serializers.ModelSerializer):

    class Meta:
        model = ListOfBet
