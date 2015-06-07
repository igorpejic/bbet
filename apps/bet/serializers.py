from rest_framework import serializers

from .models import Song, Bet


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
