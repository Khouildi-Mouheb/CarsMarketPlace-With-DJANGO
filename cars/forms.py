from django import forms
from .models import Car


class CarCreationForm(forms.ModelForm):
    class Meta:
        model=Car
        fields=['model','brand','description','type','price','location','image']