from django import forms
from models import Bet


class NormalBetForm(forms.Form):

    class Meta:
        model = Bet
