from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from apps.usuarios.models import Usuario
from django.views.generic.edit          import UpdateView 
from django.urls          import reverse_lazy

def home(request):
    if request.method == 'POST':
        print(request.POST)

        resul=[]
      
        preguntas=CuestionarioModel.objects.all()
        puntos=0
        incorrectas=0
        correctas=0
        total=0
        for p in preguntas:
            total+=1

            resul.append(request.POST.get(p.pregunta))
            print('Resul',request.POST.get(p.pregunta))
            
            print(p.correct)
            print()
            if (p.correct) ==  request.POST.get(p.pregunta):
                puntos+=10
                correctas+=1
            else:
                incorrectas+=1
        porcentaje = puntos/(total*10) *100
        

        context = {
            'preguntas':preguntas,
            'resul':resul,
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
                return redirect('listar')
        context={'form':form}
        return render(request,'cuestionario/addpregunta.html',context)
    else: 
        return redirect('/') 


class ListarPreguntas(LoginRequiredMixin, ListView):
    template_name = "cuestionario/listar.html"
    model = CuestionarioModel
    context_object_name = 'preguntas'

    def get_queryset(self):
        if self.request.user.is_staff:
            return CuestionarioModel.objects.all()

class EditarPregunta(LoginRequiredMixin, UpdateView):
    model = CuestionarioModel
    template_name = "cuestionario/editar.html"
    form_class = addPreguntaform 

    def get_success_url(self, **kwargs):
        return reverse_lazy("listar")