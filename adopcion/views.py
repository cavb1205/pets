from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from adopcion.models import Post, Adopcion, Eventos, Contacto, Comedog
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import ContactoForm,PostForm, AdopcionForm,EventosForm,ComedogForm
from django.http import HttpResponseRedirect



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

def contacto(request):
    contactos = Contacto.objects.all()
    return render(request, 'contacto.html',{'contactos':contactos})

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

def comedog(request):
    comedogs = Comedog.objects.filter(id_aprobacion=1)
    return render(request,'comedogs.html',{'comedogs':comedogs})

def comedog_detalle(request,id_comedog,nombreComedog):
    comedog = Comedog.objects.get(id=id_comedog)
    return render(request,'comedog_detalle.html',{'comedog':comedog})

def eventos(request):
    eventos = Eventos.objects.filter(id_estadoEvento=1).filter(id_aprobacion=1)
    return render(request,'eventos.html',{'eventos':eventos})

def historial_eventos(request):
    historial_eventos = Eventos.objects.filter(id_estadoEvento=2)
    return render(request,'historial_eventos.html',{'historial_eventos':historial_eventos})

def detalleEventos(request,id_evento,nombreEvento):
    evento = Eventos.objects.get(id=id_evento)
    return render(request,'detalle_evento.html',{'evento':evento})

def gracias(request):
    return render(request,'gracias.html')

##Formularios Aca##

def contactoForm(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/gracias/')
    else:
        form = ContactoForm()
    return render(request, 'contactoform.html', {'form': form})

def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_User = request.user
            print post.imagenPost
            print post.id_User
            post.save()

            return HttpResponseRedirect('/gracias/')
    else:
        form = PostForm()
    return render(request,'postform.html',{'form':form})

def agregar_mascota(request):
    if request.method == 'POST':
        form = AdopcionForm(request.POST,request.FILES)
        if form.is_valid():
            adopcion = form.save(commit=False)
            adopcion.UserAdopcion = request.user
            adopcion.save()
            return HttpResponseRedirect('/gracias/')
    else:
        form = AdopcionForm()
    return render(request,'agregar_mascota.html',{'form':form})

def agregar_evento(request):
    if request.method == 'POST':
        form = EventosForm(request.POST,request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.id_User=request.user
            evento.save()
            return HttpResponseRedirect('/gracias/')
    else:
        form = EventosForm()
    return render(request,'agregar_evento.html',{'form':form})

def agregar_comedog(request):
    if request.method == 'POST':
        form = ComedogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/gracias/')
    else:
        form = ComedogForm()
    return render(request,'agregar_comedog.html',{'form':form})
