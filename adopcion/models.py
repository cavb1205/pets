from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=20)
    apellidoUsuario = models.CharField(max_length=20)
    telefonoUsuario = models.CharField(max_length=20)
    emailUsuario = models.EmailField(max_length=100)
    creacionUsuario = models.DateField(auto_now_add=True)
    avatarUsuario = models.ImageField(upload_to='fotos/avatar/',null=True, blank=True)

    def __unicode__(self):
        return self.nombreUsuario

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

class Post(models.Model):
    tituloPost = models.CharField(max_length=100)
    contenidoPost = models.TextField(max_length=60000)
    imagenPost = models.ImageField(upload_to='fotos/post/')
    slugPost = models.SlugField(max_length=50)
    fechaPubPost = models.DateField(auto_now_add=True)
    id_usuario = models.ForeignKey(Usuario, null=False, blank=False)
    id_categoria = models.ForeignKey(CategoriaPost, null=True, blank=True)

    def __unicode__(self):
        return self.tituloPost


class Comedog(models.Model):
    nombreComedog = models.CharField(max_length=100)
    descripcionComedog = models.TextField()
    ubicacionComedog = models.CharField(max_length=100)
    responsableComedog = models.ForeignKey(Usuario)
    imagenComedog = models.ImageField(upload_to='fotos/comedog/')
    id_ciudadComedog = models.ForeignKey(Ciudad,null=True)

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
    usuarioAdopcion = models.ForeignKey(Usuario)
    id_ciudadAdopcion = models.ForeignKey(Ciudad,null=True)

    def __unicode__(self):
        return self.nombreAdopcion

class Eventos(models.Model):
    nombreEvento = models.CharField(max_length=100)
    descripcionEvento = models.TextField()
    fechaEvento = models.DateTimeField(auto_now=False)
    lugarEvento = models.CharField(max_length=100)
    valorEvento = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPubEvento = models.DateField(auto_now_add=True)
    imagenEvento = models.ImageField(upload_to='fotos/eventos/')
    id_usuario = models.ForeignKey(Usuario)
    id_ciudadEvento = models.ForeignKey(Ciudad,null=True)
    id_estadoEvento = models.ForeignKey(Estado,null=True)

    def __unicode__(self):
        return self.nombreEvento
