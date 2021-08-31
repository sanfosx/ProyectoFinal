from django.db import models


ESTADO_CHOICES = (
    ("rta1", "Respuesta 1"),
    ("rta2", "Respuesta 2"),
    ("rta3", "Respuesta 3")
)
class CuestionarioModel(models.Model):

    pregunta = models.CharField(max_length=200,null=True)
    rta1 = models.CharField(max_length=200,null=True)
    rta2 = models.CharField(max_length=200,null=True)
    rta3 = models.CharField(max_length=200,null=True)
    correct = models.CharField(max_length=4, choices=ESTADO_CHOICES, default=" ")
    

    class Meta:
        db_table = 'cuestionario'
    
    def __str__(self):

        return self.pregunta 

