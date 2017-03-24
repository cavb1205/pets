from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from adopcion.models import Post, Adopcion, Eventos
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout



# Create your views here.
def perfil(request,id_user):
    print request.user.first_name
    return render(request,'perfil.html')

def socialLogin(request):
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

def inicio(request):

    return render(request,'index.html',{'inicio':inicio})

def nosotros(request):
    return render(request,'nosotros.html')

def unete(request):
    return render(request,'unete.html')

def historias(request):
    historias = Post.objects.filter(id_aprobacion=1)
    return render(request,'historias.html',{'historias':historias})

def detalleHistoria(request,id_post,slugPost):
    historia = Post.objects.get(id=id_post)
    return render(request,'detalle_historia.html',{'historia':historia})

def adopcion(request):
    animales = Adopcion.objects.filter(estadoAdopcion=1).filter(id_aprobacion=1)
    return render(request,'adopcion.html',{'animales':animales})

def detalleAdopcion(request,id_adopcion,nombreAdopcion):
    animal = Adopcion.objects.get(id=id_adopcion)
    return render(request,'detalle_adopcion.html',{'animal':animal})

def adoptados(request):
    adoptados = Adopcion.objects.filter(estadoAdopcion=2)
    return render(request,'adoptados.html',{'adoptados':adoptados})

def infoComedog(request):
    return render(request,'infoComedog.html')

def planPadrinoComedog(request):
    return render(request,'planPadrinoComedog.html')

def eventos(request):
    eventos = Eventos.objects.filter(id_estadoEvento=1).filter(id_aprobacion=1)
    return render(request,'eventos.html',{'eventos':eventos})

def historial_eventos(request):
    historial_eventos = Eventos.objects.filter(id_estadoEvento=2)
    return render(request,'historial_eventos.html',{'historial_eventos':historial_eventos})

def detalleEventos(request,id_evento,nombreEvento):
    evento = Eventos.objects.get(id=id_evento)
    return render(request,'detalle_evento.html',{'evento':evento})
