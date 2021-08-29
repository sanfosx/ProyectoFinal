from django.urls import path 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .	import views
from .views import signup

app_name = "usuarios"

urlpatterns = [

	path('signup/',views.signup,name='signup'),
	path('login/',LoginView.as_view(template_name= 'login.html'), name='login'),
	path('logout/',auth_views.logout_then_login, name='logout'),
	path('listar/', views.ListarUsuarios.as_view(), name="listar"),
] 