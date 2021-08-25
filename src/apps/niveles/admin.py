from django.contrib import admin

from .models import Nivel, Pregunta, Respuesta 

class NivelesAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'descrip','pregs_nivel']

admin.site.register(Nivel, NivelesAdmin)


class PreguntasAdmin(admin.ModelAdmin):
	list_display = ['id', 'det_preg', 'rtas_preg']

admin.site.register(Pregunta, PreguntasAdmin)

class RespuestasAdmin(admin.ModelAdmin):
	list_display = ['id', 'det_rta', 'is_true']

admin.site.register(Respuesta, RespuestasAdmin)

