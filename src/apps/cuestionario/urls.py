from    django.contrib              import admin
from    django.urls                 import path
from    .views                      import *
from    django.conf                 import settings
from    django.conf.urls.static     import static
 
urlpatterns = [

    path('home/',home,name='home'),
    path('addpregunta/', addPregunta,name='addpregunta'),
   # path('resultado/', addPregunta,name='addPregunta'),
]