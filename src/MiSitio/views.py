from django.contrib.auth.models import User
from django.shortcuts           import render

def inicio (request):
	template_name="inicio.html"

	return render(request,template_name)

"""def login (request):
	template_name="login.html"

	return render(request,template_name)
"""

def registro (request):
	template_name="registro.html"

	return render(request,template_name)

def home (request):
	template_name="home.html"

	return render(request,template_name)