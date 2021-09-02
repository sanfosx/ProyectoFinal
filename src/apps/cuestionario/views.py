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
import random

def home(request,nivel):
    
    #Cargo la cantidad de preguntas segun el nivel elegido
    preguntas=CuestionarioModel.objects.all()    

    if (nivel == 1 and len(preguntas)> 3):
        preguntas=random.sample(list(preguntas),3)

    elif (nivel == 2 and len(preguntas)> 5):
        preguntas=random.sample(list(preguntas),5)

    elif (nivel== 3 and len(preguntas)> 10):
        preguntas=random.sample(list(preguntas),10)
    

    print("PREGUNTAS INICIO",preguntas)
    print("------------------------------------")

 # Logica del juego    
    if request.method == 'POST':
        print(request.POST)
        print('Nivel',nivel)
        aprueba=False

        print("PREGUNTAS POST",preguntas)
        print("------------------------------------")
        ELIGIO=[]

        puntos=0
        incorrectas=0
        correctas=0
        total=0
        for p in preguntas:
            total+=1
            #pruebas----------------------------------
            print("que tiene preguntas", preguntas)
            #fin  de pruebas----------------------------- 

            if (p.correct) ==  request.POST.get(p.pregunta):
                if request.user.nivel=="Medio": 
                    puntos+=25
                elif request.user.nivel=="Dificil":
                    puntos+=50
                elif request.user.nivel=="Chaqueñazo":
                    puntos+=100
                else:
                    puntos+=10

                correctas+=1
            else:
                incorrectas+=1

            #Guardo para mostrar
            x=request.POST.get(p.pregunta)
          
            if x=="rta1":
                print('ELIGIO',p.rta1)
                ELIGIO.append(p.rta1)
            elif x=="rta2":
                print('ELIGIO',p.rta2)
                ELIGIO.append(p.rta2)
            elif x=="rta3":
                print('ELIGIO',p.rta3)
                ELIGIO.append(p.rta3)
            
            if p.correct=="rta1":
                print('Pregunta correcta',p.rta1)
                p.correct=p.rta1
            elif p.correct=="rta2":
                print('Pregunta correcta',p.rta2)
                p.correct=p.rta2
            else: 
                print('Pregunta correcta',p.rta3)
                p.correct=p.rta3    
        
        #Segun el porcentaje y el nivel aprueba y pasa al siguiente nivel

        porcentaje = (correctas/total) *100

        if (request.user.nivel=="Medio" and porcentaje>=60): 
            request.user.nivel="Dificil"
            aprueba=True
        elif (request.user.nivel=="Dificil" and porcentaje>=80):
            request.user.nivel="Chaqueñazo"
            aprueba=True
        elif (request.user.nivel=="Chaqueñazo" and porcentaje==100):
            request.user.nivel="DIOS"
            aprueba=True
        elif (request.user.nivel=="Facil" and porcentaje>=50):
            request.user.nivel="Medio"
            aprueba=True

        #Guardo los puntos en usuario
        if request.user.ptos_totales < puntos:
            request.user.ptos_totales=puntos
        request.user.save()

        context = {
            'aprueba':aprueba,
            'preguntas':preguntas,
            'ELIGIO':ELIGIO,
            'puntos':puntos,
            'time': request.POST.get('timer'),
            'correctas':correctas,
            'incorrectas':incorrectas,
            'porcentaje':porcentaje,
            'total':total
        }
        return render(request,'cuestionario/resultados.html',context)
    else:
        print("PREGUNTAS NO POST",preguntas)
        print("------------------------------------")
        #preguntas=CuestionarioModel.objects.all()
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