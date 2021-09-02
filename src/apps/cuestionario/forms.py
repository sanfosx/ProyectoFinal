from django.forms import ModelForm
from django import forms
from .models import *


 
class addPreguntaform(ModelForm):
    pregunta=forms.CharField(max_length=500,  label='Pregunta', widget=forms.TextInput(attrs={'class':'form-control'}))
    rta1=forms.CharField(max_length=500,  label='Respuesta 1',widget=forms.TextInput(attrs={'class':'form-control'}) )
    rta2=forms.CharField(max_length=100,  label='Respuesta 2',widget=forms.TextInput(attrs={'class':'form-control'}))
    rta3=forms.CharField(max_length=100,  label='Respuesta 3',widget=forms.TextInput(attrs={'class':'form-control'}))
    correct=forms.ChoiceField(choices=ESTADO_CHOICES,label="Respuesta correcta", widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))

    class Meta:
        model=CuestionarioModel
        fields="__all__"