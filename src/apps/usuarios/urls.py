from django.urls import path 

from . import views

app_name = "usuarios"

urlpatterns = [
	
	path('listar/', views.listar_usuarios, name="listar")
] 