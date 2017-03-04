from django.contrib import admin
from adopcion.models import Post, CategoriaPost, Usuario, Eventos, Comedog, CategoriaAdopcion, Raza, Color, Castrado, Tamano, Estado, Adopcion
# Register your models here.



admin.site.register(CategoriaPost)
admin.site.register(Post)
admin.site.register(Usuario)
admin.site.register(Eventos)
admin.site.register(Comedog)
admin.site.register(Adopcion)
admin.site.register(Estado)
admin.site.register(Tamano)
admin.site.register(Castrado)
admin.site.register(Color)
admin.site.register(Raza)
admin.site.register(CategoriaAdopcion)
