from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include

from . import views
urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.inicio, name='principal'),

    #path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/',auth_views.logout_then_login, name="logout"),
    path('registro/', views.registro, name='registro'),
    path('home/', views.home, name='home'),
    
    path('usuarios/', include('apps.usuarios.urls')),


]
