from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from adopcion.models import Post, Adopcion
from django.template import RequestContext

# Create your views here.
def inicio(request):
    return render_to_response('index.html',{'inicio':inicio})

def historias(request):
    historias = Post.objects.all()
    return render_to_response('historias.html',{'historias':historias})

def detalleHistoria(request,id_post,slugPost):
    historia = Post.objects.get(id=id_post)
    return render_to_response('detalle_historia.html',{'historia':historia})

def adopcion(request):
    animales = Adopcion.objects.all()
    return render_to_response('adopcion.html',{'animales':animales})

def detalleAdopcion(request,id_adopcion,nombreAdopcion):
    animal = Adopcion.objects.get(id=id_adopcion)
    return render_to_response('detalle_adopcion.html',{'animal':animal})
