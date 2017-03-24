from django.contrib import admin
from adopcion.models import Perfil,EstadoEvento,Aprobacion,Ciudad,Pais, Region,Post, CategoriaPost, Eventos, Comedog, CategoriaAdopcion, Raza, Color, Castrado, Tamano, Estado, Adopcion

from draceditor.widgets import AdminDraceditorWidget

from django.db import models


class PostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }

admin.site.register(Post, PostModelAdmin)

admin.site.register(Perfil)
admin.site.register(EstadoEvento)
admin.site.register(CategoriaPost)
#admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Eventos)
admin.site.register(Comedog)
admin.site.register(Adopcion)
admin.site.register(Estado)
admin.site.register(Tamano)
admin.site.register(Castrado)
admin.site.register(Color)
admin.site.register(Raza)
admin.site.register(CategoriaAdopcion)
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Aprobacion)
