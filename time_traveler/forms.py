from django import forms
from .models import TimeTraveler

class TimeTravelerForm(forms.ModelForm):
    class Meta:
        model = TimeTraveler
        fields = '__all__'
