from django.shortcuts import render, redirect
from SigmaWebCore.data.models import User
from SigmaWebCore.data.repositories import UserRepository

repo = UserRepository()
repo.datasrc = [
    User(rut="200546695", nombre="Sergio Leonardo Castro Jiménez", email="sl.castroj@gmail.com")
]

def inicio_sesion(request):
    return render(request, "core/inicio_sesion.html")

def perfil(request):
    user : User = repo.get_single("200546695")
    context = {
        "rut": user.rut,
        "nombre": user.nombre,
        "email": user.email
    }
    return render(request, "core/perfil.html", context)

def cierre_sesion(request):
    return redirect("index")