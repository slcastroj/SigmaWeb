from django.urls import path, include

from .views import debug, core, users, services

urlpatterns = [
    path("base/", debug.base, name="base"),
    path("", core.index, name="index"),
    path("servicios/", core.servicios, name="servicios"),
    path("inicio_sesion/", users.inicio_sesion, name="inicio_sesion"),
    path("registro/", users.registro, name="registro"),
    path("cotizacion/?<int:id>", services.cotizacion, name="cotizacion"),
    path("solicitud/?<int:id>", services.solicitud, name="solicitud"),
]
