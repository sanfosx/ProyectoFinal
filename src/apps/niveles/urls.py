from django.urls import path
from .views import NivelListView, nivel_view

app_name = 'niveles'

urlpatterns = [
	path('', NivelListView.as_view(), name='main-view'),
	path('<pk>/', nivel_view, name='nivel-view')
	# <pk> es la clave de la tabla nivel, que usa nivel_view para traer el obj clase Nivel correspondiente
]