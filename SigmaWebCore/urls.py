from django.urls import path, include

from .views import debug, core, users, services

urlpatterns = [
    path("base/", debug.base, name="base"),
    path("", core.index, name="index"),
    path("servicios/", core.servicios, name="servicios"),
    path("perfil", users.perfil, name="perfil"),
    path("inicio_sesion/", users.inicio_sesion, name="inicio_sesion"),
    path("cierre_sesion/", users.cierre_sesion, name="cierre_sesion"),
    path("solicitud", services.solicitud, name="solicitud"),
    path("historial/", services.historial, name="historial"),
    path("registrar/", users.registrar, name="registrar"),
    path("cambiar-correo/", users.email, name="email"),
    path("cambiar-clave/", users.clave, name="clave"),
]
