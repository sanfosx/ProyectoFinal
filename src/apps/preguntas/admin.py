from django.contrib import admin
from .models import Pregunta, Respuesta

# Register your models here

# tabular inline es para poder ver respuestas en la misma pantalla que las preguntas
class RespuestaInline(admin.TabularInline):
	model = Respuesta

class PreguntaAdmin(admin.ModelAdmin):
	inlines = [RespuestaInline]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
