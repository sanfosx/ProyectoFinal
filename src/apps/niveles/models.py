from django.db import models

class Respuesta(models.Model):
	det_rta = models.CharField(max_length=255)
	is_true = models.BooleanField(default= False)

	class Meta:
		db_table = 'respuestas'

	def __str__(self):
		return self.det_rta


class Pregunta(models.Model):
	det_preg = models.CharField(max_length=255)
	rtas_preg = models.ForeignKey(Respuesta, on_delete= models.CASCADE)
	
	class Meta:
		db_table = 'preguntas'

	def __str__(self):
		return self.det_preg


class Nivel(models.Model):
	nombre = models.CharField(max_length=50)
	descrip = models.CharField(max_length=255)
	pregs_nivel = models.ForeignKey(Pregunta, on_delete= models.CASCADE)

	class Meta:
		db_table = 'niveles'

	def __str__(self):
		return self.nombre

