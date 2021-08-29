from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from apps.usuarios.models import Usuario

def home(request):
    if request.method == 'POST':
        print(request.POST)
        preguntas=CuestionarioModel.objects.all()
        puntos=0
        incorrectas=0
        correctas=0
        total=0
        for p in preguntas:
            total+=1
            print(request.POST.get(p.preguntas))
            print(p.correct)
            print()
            if p.correct ==  request.POST.get(p.preguntas):
                puntos+=10
                correctas+=1
            else:
                incorrectas+=1
        porcentaje = puntos/(total*10) *100
        context = {
            'puntos':puntos,
            'time': request.POST.get('timer'),
            'correctas':correctas,
            'incorrectas':incorrectas,
            'porcentaje':porcentaje,
            'total':total
        }
        return render(request,'cuestionario/resultados.html',context)
    else:
        preguntas=CuestionarioModel.objects.all()
        context = {
            'preguntas':preguntas
        }
        return render(request,'cuestionario/home.html',context)
 
def addPregunta(request):    
    if request.user.is_staff:
        form=addPreguntaform()
        if(request.method=='POST'):
            form=addPreguntaform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'cuestionario/addpregunta.html',context)
    else: 
        return redirect('home') 


class ListarPreguntas(LoginRequiredMixin, ListView):
    template_name = "cuestionario/listar.html"
    model = Usuario
    context_object_name = 'usuarios'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Usuario.objects.all()