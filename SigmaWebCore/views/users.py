from django.shortcuts import render, redirect

def inicio_sesion(request):
    return render(request, "core/inicio_sesion.html")

def perfil(request):
    return render(request, "core/perfil.html")

def cierre_sesion(request):
    return redirect("index")