from django.contrib.auth.models import User
from django.shortcuts           import render
from	apps.usuarios.models	import Usuario

def inicio (request):
	template_name="inicio.html"

	usuarios= Usuario.objects.filter(comparte=True).order_by('-ptos_totales')
	context = {
            'usuarios':usuarios
        }

	return render(request,template_name,context)

