from django.db import models


class CuestionarioModel(models.Model):
    pregunta = models.CharField(max_length=200,null=True)
    rta1 = models.CharField(max_length=200,null=True)
    rta2 = models.CharField(max_length=200,null=True)
    rta3 = models.CharField(max_length=200,null=True)
    correct = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = 'cuestionario'
    
    def __str__(self):

        return self.pregunta 

