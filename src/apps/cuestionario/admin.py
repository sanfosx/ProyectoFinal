from django.contrib import admin
from .models import *
 
class CuestionariosAdmin(admin.ModelAdmin):
	list_display = ['id', 'pregunta','rta1','rta2','rta3','correct']

admin.site.register(CuestionarioModel, CuestionariosAdmin)