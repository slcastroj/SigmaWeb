from django.shortcuts import render

def inicio_sesion(request):
    return render(request, "core/inicio_sesion.html")

def registro(request):
    return render(request, "core/registro.html")