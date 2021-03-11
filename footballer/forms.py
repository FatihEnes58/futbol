from django import forms
from .models import Footballer
from footballteam.models import FootballTeam

class FootballerForm(forms.ModelForm):
    class Meta:
        model = Footballer
        fields = ["name", "age", "salary", "position", "marketValue", "overall", "team"]

    def save(self, commit=True):
        footballer = super(FootballerForm, self).save(commit=True)
        footballer.save()
        return footballer
