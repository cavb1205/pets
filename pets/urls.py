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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from adopcion import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.inicio),
    url(r'^nosotros/$', views.nosotros),
    url(r'^unete/$', views.unete),
    url(r'^historias/$', views.historias),
    url(r'^adopcion/$', views.adopcion),
    url(r'^detalle_adopcion/(?P<id_adopcion>.*)/(?P<nombreAdopcion>.*)/$', views.detalleAdopcion),
    url(r'^detalle_historia/(?P<id_post>.*)/(?P<slugPost>.*)/$', views.detalleHistoria),
    url(r'^info/comedog/$', views.infoComedog),
    url(r'^adoptados/$', views.adoptados),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
