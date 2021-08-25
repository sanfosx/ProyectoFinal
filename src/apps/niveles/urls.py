from django.urls import path 

from .	import views
from .views import Listar, NivelListView

app_name = "niveles"

urlpatterns = [

	path('homen/',Listar.as_view(template_name= 'niveles/homen.html'), name='homen'),
	path('listar/<int:pk>/', NivelListView.as_view(template_name='niveles/listar'),name= 'listar')
	
] 














	