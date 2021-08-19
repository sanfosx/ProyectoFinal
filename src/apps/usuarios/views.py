from django.shortcuts import render

from .models import Usuario


def listar_usuarios(request):
	template_name="usuario/listar.html"
	lista_de_usuarios = Usuario.objects.all()
	
	ctx={
		'usuarios': lista_de_usuarios
	}
	return render(request,template_name, ctx )