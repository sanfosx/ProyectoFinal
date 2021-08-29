from django.forms import ModelForm
from .models import *


 
class addPreguntaform(ModelForm):
    class Meta:
        model=CuestionarioModel
        fields="__all__"