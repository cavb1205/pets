"""pets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.db import models
from django.conf.urls.static import static
from django.conf import settings




from adopcion import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^perfil/(?P<id_user>.*)/', views.perfil),
    url(r'^$', views.inicio),
    url(r'^login/$', views.socialLogin),
    url(r'^logout/$', views.logout_view),
    url(r'^nosotros/$', views.nosotros),
    url(r'^unete/$', views.unete),
    url(r'^historias/$', views.historias),
    url(r'^adopcion/$', views.adopcion),
    url(r'^contacto/$', views.contactoForm),
    url(r'^detalle_adopcion/(?P<id_adopcion>.*)/(?P<nombreAdopcion>.*)/$', views.detalleAdopcion),
    url(r'^detalle_historia/(?P<id_post>.*)/(?P<slugPost>.*)/$', views.detalleHistoria),
    url(r'^info/comedog/$', views.infoComedog),
    url(r'^comedog/plan_padrino_comedog/$', views.planPadrinoComedog),
    url(r'^comedogs/$', views.comedog),
    url(r'^comedog/(?P<id_comedog>.*)/(?P<nombreComedog>.*)/$', views.comedog_detalle),
    url(r'^adoptados/$', views.adoptados),
    url(r'^proximos_eventos/$', views.eventos),
    url(r'^historial_eventos/$', views.historial_eventos),
    url(r'^detalle_evento/(?P<id_evento>.*)/(?P<nombreEvento>.*)/$', views.detalleEventos),
    url(r'^gracias/$', views.gracias),
    ##url formularios##
    url(r'^historia/nueva/$', views.agregar_post),
    url(r'^adopcion/nueva/$', views.agregar_mascota),
    url(r'^evento/nuevo/$', views.agregar_evento),
    url(r'^comedog/nuevo/$', views.agregar_comedog),



    # Python Social Auth URLs
    url('', include('social_django.urls', namespace='social')),
    #markdown
    url(r'^draceditor/', include('draceditor.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
