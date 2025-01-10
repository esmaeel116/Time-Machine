from django import forms
from .models import TimeDestination

class TimeDestinationForm(forms.ModelForm):
    class Meta:
        model = TimeDestination
        fields = ['name', 'description' ,'origin', 'destination']
