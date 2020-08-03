"""cruddjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.principal.views import inicio,crearpersona,editarpersona, eliminarpersona
#importamos la clase para el crud
from apps.principal.class_views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(route='', view=inicio, name='index'),
    path(route='', view=PersonaList.as_view(), name='index'),
    #path(route='crearpersona', view=crearpersona, name='crearpersona'),
    path(route='crearpersona', view=PersonaCreate.as_view(), name='crearpersona'),
    #path(route='editarpersona/<int:id>', view=editarpersona, name='editarpersona'),
    path(route='editarpersona/<int:pk>', view=PersonaUpdate.as_view(), name='editarpersona'),
    #path(route='eliminarpersona/<int:id>', view=eliminarpersona, name='eliminarpersona'),
    path(route='eliminarpersona/<int:pk>', view=PersonaDelete.as_view(), name='eliminarpersona'),
]
