from django.forms import ModelForm
from django import forms
from .models import *


 
class addPreguntaform(ModelForm):

    correct=forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))

    class Meta:
        model=CuestionarioModel
        fields="__all__"