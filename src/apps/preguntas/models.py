from django.db import models
from apps.niveles.models import Nivel

# Create your models here.

class Pregunta(models.Model):
	texto = models.CharField(max_length=250)
	nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
	creado = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.texto)

	def get_respuestas(self):
		return self.respuesta_set.all()

class Respuesta(models.Model):
	texto = models.CharField(max_length=250)
	es_correcto = models.BooleanField(default=False)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	creado = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'pregunta: {self.pregunta.texto}, respuesta: {self.texto}, es correcta: {self.es_correcto}'