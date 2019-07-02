from django.shortcuts import render, redirect
from SigmaWebCore.data.models import User, Solicitud
from SigmaWebCore.data.repositories import UserRepository
from .users import GetUser
import time
import requests
import json

urlBase = 'http://localhost:2115/ok-casa/'
headers = {'content-type': 'application/json'}

user = GetUser()
soli = Solicitud()
def solicitud(request):
    if not user.IsLoged():
        return redirect("inicio_sesion")
    s = requests.get(urlBase + 'servicio/'+request.GET['id'],headers=headers)
    context = {
        "usuario":user,
        "solicitud":soli,
        "servicio":s.json()
    }
    if request.method == 'POST':
        o = request.POST
        obj = {
            'direccion':o['direccion'],
            'creacion':time.strftime("%d/%m/%y"),
            'id_estado':1,
            'id_servicio':o['id'],
            'id_equipo':1,
            'usuario':user.rut
        }
        print(obj)
        r = requests.post(urlBase + 'solicitud/',headers=headers,data=json.dumps(obj))
        if r.status_code == 200:
            return redirect("historial")
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