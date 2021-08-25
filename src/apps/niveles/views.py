from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView 
from django.urls import reverse_lazy
from .models import Nivel



class Listar(LoginRequiredMixin, ListView):
	template_name = 'niveles/homen.html'
	model = Nivel
	context_object_name = 'niveles'

	def get_queryset(self):
		if self.request.user.is_active:
			return Nivel.objects.all()


class NivelListView(LoginRequiredMixin,ListView):
	template_name = "niveles/listar.html" # Esto lo tengo que redirigir a 'usuario/home.html' ???
	model = Nivel
	context_object_name = 'niveles' # define al objeto como niveles en vez de object_list en el template

	def get_queryset(self):
		if self.request.user.is_active:
			return Nivel.objects.all()

	def get_success_url(self, **kwargs):
		return reverse_lazy('niveles:homen')