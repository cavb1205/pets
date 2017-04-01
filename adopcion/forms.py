from django import forms
from django.forms import ModelForm
from models import Contacto
from django.contrib.admin import widgets
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
