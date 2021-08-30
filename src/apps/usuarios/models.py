from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

	ptos_totales = models.CharField(max_length=10,blank=True,null=True,default='0')
	comparte = models.BooleanField(default=True)
	
	
	class Meta:
		db_table = 'usuarios'

def update_db_field(name,field,value):
    Usuario.objects.get(name=name).update(field=value)