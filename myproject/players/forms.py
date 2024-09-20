# players/forms.py
from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['id_player','last_name', 'first_name', 'birth_year', 'club']