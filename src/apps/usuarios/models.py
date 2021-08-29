from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

	ptos_totales = models.CharField(max_length=10,blank=True,null=True)
	comparte = models.BooleanField(default=True)
	
	
	class Meta:
		db_table = 'usuarios'

