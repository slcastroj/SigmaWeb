from django.shortcuts import render, redirect
from SigmaWebCore.data.models import User
from SigmaWebCore.data.repositories import UserRepository
import requests
import json

urlBase = 'http://localhost:2115/ok-casa/'

user = User()
headers = {'content-type': 'application/json'}

def GetUser():
    return user

def inicio_sesion(request):
    if request.method == 'POST':
        u = requests.get(urlBase + 'usuario/'+request.POST['rut'],headers=headers)
        if u.status_code == 200:
            us = u.json()
            if us['clave'] == request.POST['clave']:
                user.clave = us['clave']
                user.rut = us['rut']
                user.nombre = us['nombre']
                user.email = us['email']
                user.nacimiento = us['fecha_nac']
                user.id_tipo = us['id_tipo']
                user.LogIn()
            return redirect("index")
    return render(request, "core/inicio_sesion.html")

def perfil(request):
    if not user.IsLoged():
        return redirect("inicio_sesion")
    context = {
        "rut": user.rut,
        "nombre": user.nombre,
        "email": user.email
    }
    return render(request, "core/perfil.html", context)

def cierre_sesion(request):
    user.Drop()
    return redirect("index")

def registrar(request):
    us = request.POST
    if us['clave'] == us['clave2']:
        obj = {
            'clave':us['clave'],
            'rut':us['rut'],
            'email':us['email'],
            'nombre':us['nombre'],
            'fecha_nac':us['nacimiento'],
            'id_tipo':1,
        }
        r = requests.post(urlBase + 'usuario/',data=json.dumps(obj),headers=headers)
        if r.status_code == 200:
            user.clave = us['clave']
            user.rut = us['rut']
            user.nombre = us['nombre']
            user.email = us['email']
            user.nacimiento = us['nacimiento']
            user.id_tipo = 1
            user.LogIn()
            return redirect("perfil")
    return redirect("inicio_sesion")

def clave(request):
    if not user.IsLoged():
        return redirect("inicio_sesion")
    o = request.POST
    if o['clavea'] == user.clave:
        if o['clave1'] == o['calve2']:
            obj = {"clave":o['clave']}
            r = requests.put(urlBase + 'usuario/'+user.rut,data=json.dumps(obj),headers=headers)
    return redirect("perfil")

def email(request):
    if not user.IsLoged():
        return redirect("inicio_sesion")
    o = request.POST
    if o['clave'] == user.clave:
        if o['email'] == o['email2']:
            obj = {"email":o['email']}
            r = requests.put(urlBase + 'usuario/'+user.rut,data=json.dumps(obj),headers=headers)
    return redirect("perfil")