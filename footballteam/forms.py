from django import forms
from .models import FootballTeam

class FootballTeamForm(forms.ModelForm):
    class Meta:
        model = FootballTeam
        fields = ["name"]