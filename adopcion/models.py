from __future__ import unicode_literals
from django.dispatch import receiver
from django.dispatch import Signal
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from markdownx.models import MarkdownxField


# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='fotos/avatar/',blank=True)
    biografia = models.TextField(max_length=500,blank=True)
    fecha_cumpleanos = models.DateField(auto_now=False,null=True,blank=True)

    def __unicode__(self):
        return unicode(self.user)

@receiver(post_save, sender=User)
def crear_user_perfil(sender, instance, created, **kwargs):
    print 'ingresa a la senal crear_user_perfil'
    print 'sender es:'
    print sender
    print 'instance es:'
    print instance
    print 'create es:'
    print created
    print 'kwargs es:'
    print kwargs
    if created:
        Perfil.objects.create(user=instance)
    else:
        print 'usuario ya fue creado'

@receiver(post_save, sender=User)
def save_user_perfil(sender, instance, **kwargs):
    print 'ingresa al save de senal'
    print instance
    instance.perfil.save()

class Pais(models.Model):
    nombrePais = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nombrePais

class Region(models.Model):
    nombreRegion = models.CharField(max_length=20)
    id_pais = models.ForeignKey(Pais,null=True)

    def __unicode__(self):
        return self.nombreRegion

class Ciudad(models.Model):
    nombreCiudad = models.CharField(max_length=20)
    id_region = models.ForeignKey(Region, null=True)

    def __unicode__(self):
        return self.nombreCiudad

class CategoriaPost(models.Model):
    nombreCategoriaPost = models.CharField(max_length=50)
    descripcionCategoriaPost = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombreCategoriaPost

class Aprobacion(models.Model):
    aprobacion = models.CharField(max_length=20)

    def __unicode__(self):
        return self.aprobacion

class Post(models.Model):
    tituloPost = models.CharField(max_length=100)
    contenidoPost = models.TextField(max_length=60000)
    imagenPost = models.ImageField(upload_to='fotos/post/',blank=True,null=True)
    videoPost = models.URLField(max_length=200,blank=True,null=True)
    slugPost = models.SlugField(editable=False,null=False,blank=True)
    fechaPubPost = models.DateField(auto_now_add=True)
    id_User = models.ForeignKey(User, null=True, blank=True)
    id_categoria = models.ForeignKey(CategoriaPost, null=True, blank=True)
    id_aprobacion = models.ForeignKey(Aprobacion, null=True, blank=True, default=2)

    def __unicode__(self):
        return self.tituloPost

    def save(self, *args, **kwargs):
        if not self.id:
            self.slugPost = slugify(self.tituloPost)
        super(Post, self).save(*args, **kwargs)

class Comedog(models.Model):
    nombreComedog = models.CharField(max_length=100)
    descripcionComedog = models.TextField()
    ubicacionComedog = models.CharField(max_length=100)
    responsableComedog = models.ForeignKey(User,null=True,blank=True)
    imagenComedog = models.ImageField(upload_to='fotos/comedog/')
    id_ciudadComedog = models.ForeignKey(Ciudad,null=True)
    id_aprobacion = models.ForeignKey(Aprobacion, null=True, blank=True, default=2)


    def __unicode__(self):
        return self.nombreComedog


class CategoriaAdopcion(models.Model):
    nombreCategoriaAdopcion = models.CharField(max_length=100)
    descripcionCategoriaAdopcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombreCategoriaAdopcion

class Raza(models.Model):
    nombreRaza = models.CharField(max_length=100)
    descripcionRaza = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombreRaza

class Color(models.Model):
    nombreColor = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombreColor

class Castrado(models.Model):
    obcionCastrado = models.CharField(max_length=10)

    def __unicode__(self):
        return self.obcionCastrado

class Tamano(models.Model):
    nombreTamano = models.CharField(max_length=50)
    descripcionTamano = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombreTamano

class Estado(models.Model):
    nombreEstado = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombreEstado


class Adopcion(models.Model):
    nombreAdopcion = models.CharField(max_length=100, verbose_name='Nombre de la Mascota')
    edadAdopcion = models.IntegerField(help_text='Meses')
    historiaAdopcion = models.TextField()
    imagenDestacadaAdopcion = models.ImageField(upload_to='fotos/adopcion/')
    imagenAdopcion1 = models.ImageField(upload_to='fotos/adopcion/',blank=True,null=True)
    imagenAdopcion2 = models.ImageField(upload_to='fotos/adopcion/',blank=True,null=True)
    fechaPubAdopcion = models.DateField(auto_now_add=True)
    categoriaAdopcion = models.ForeignKey(CategoriaAdopcion)
    razaAdopcion = models.ForeignKey(Raza)
    colorAdopcion = models.ForeignKey(Color)
    castradoAdopcion = models.ForeignKey(Castrado)
    tamanoAdopcion = models.ForeignKey(Tamano)
    estadoAdopcion = models.ForeignKey(Estado)
    UserAdopcion = models.ForeignKey(User,null=True,blank=True)
    id_ciudadAdopcion = models.ForeignKey(Ciudad,null=True)
    id_aprobacion = models.ForeignKey(Aprobacion,null=True, blank=True, default=2)

    def __unicode__(self):
        return self.nombreAdopcion

class EstadoEvento(models.Model):
    nombreEstado = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nombreEstado

class Eventos(models.Model):
    nombreEvento = models.CharField(max_length=100)
    descripcionEvento = models.TextField()
    fechaEvento = models.DateTimeField(auto_now=False)
    lugarEvento = models.CharField(max_length=100)
    valorEvento = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPubEvento = models.DateField(auto_now_add=True)
    imagenEvento = models.ImageField(upload_to='fotos/eventos/')
    id_User = models.ForeignKey(User,null=True,blank=True)
    id_ciudadEvento = models.ForeignKey(Ciudad,null=True)
    id_estadoEvento = models.ForeignKey(EstadoEvento,null=True,default=1)
    id_aprobacion = models.ForeignKey(Aprobacion,null=True,blank=True,default=2)

    def __unicode__(self):
        return self.nombreEvento
