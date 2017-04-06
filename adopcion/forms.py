from django import forms
from django.forms import ModelForm
from models import Contacto, Post, Adopcion, Eventos, Comedog
from django.contrib.admin import widgets
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('tituloPost','contenidoPost','id_categoria','imagenPost','videoPost')
        widgets = {
        'id_categoria':forms.Select(attrs={'class':'browser-default'})
        }

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ('nombreAdopcion','edadAdopcion','historiaAdopcion','imagenDestacadaAdopcion','imagenAdopcion1','imagenAdopcion2','categoriaAdopcion','razaAdopcion','colorAdopcion','castradoAdopcion','tamanoAdopcion','id_ciudadAdopcion')
        widgets = {
        'categoriaAdopcion':forms.Select(attrs={'class':'browser-default'}),
        'razaAdopcion':forms.Select(attrs={'class':'browser-default'}),
        'colorAdopcion':forms.Select(attrs={'class':'browser-default'}),
        'castradoAdopcion':forms.Select(attrs={'class':'browser-default'}),
        'tamanoAdopcion':forms.Select(attrs={'class':'browser-default'}),
        'id_ciudadAdopcion':forms.Select(attrs={'class':'browser-default'}),

         }

class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ('nombreEvento','descripcionEvento','fechaEvento','lugarEvento','valorEvento','imagenEvento','id_ciudadEvento',)
        widgets = {
        'id_ciudadEvento':forms.Select(attrs={'class':'browser-default'}),
        'fechaEvento':forms.DateTimeInput(format=['%Y-%m-%d %H:%M'])
        }

class ComedogForm(forms.ModelForm):
    class Meta:
        model = Comedog
        fields = ('nombreComedog','descripcionComedog','ubicacionComedog','responsableComedog','imagenComedog','id_ciudadComedog')
        widgets = {
        'id_ciudadComedog':forms.Select(attrs={'class':'browser-default'}),
        'responsableComedog':forms.Select(attrs={'class':'browser-default'}),

        }
