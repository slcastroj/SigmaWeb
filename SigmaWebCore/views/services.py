from django.shortcuts import render, redirect
from SigmaWebCore.data.models import User
from SigmaWebCore.data.repositories import UserRepository
from .users import GetUser
import requests
import json

urlBase = 'http://localhost:2115/ok-casa/'

user = GetUser()
def solicitud(request):
    if not user.IsLoged():
        return redirect("inicio_sesion")
    context = {
        "usuario":{},
        "solicitud":{}
    }
    return render(request, "core/solicitud.html", context)

def historial(request):
    if not user.IsLoged():
        return redirect("inicio_sesion")
    headers = {'content-type': 'application/json'}
    e = requests.get(urlBase + 'estadosol',headers=headers)
    s = requests.get(urlBase + 'solicitud',headers=headers)
    i = requests.get(urlBase + 'solicitud',headers=headers)
    solicitudes = []
    try:
        for sol in s.json():
            if sol.usuario == user.rut:
                solicitudes += sol
    except:
        solicitudes = s.json()
    print(solicitudes)
    #print('estados :' + e.json())
    #print('inspecciones :' + i.json())
    context = {
        "estados": e.json(),
        "solicitudes": solicitudes,
        "inspecciones": i.json(),
        "ins":len(i.json()),
        "ordenes": [
            { "id":0, "nombre":"Fecha descendente" },
            { "id":1, "nombre":"Fecha ascendente" },
        ]
    }
    return render(request, "core/historial.html", context)