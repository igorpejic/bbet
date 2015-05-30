from django import forms
from models import Song


class NormalBetForm(forms.Form):

    class Meta:
        model = Song
