from django.shortcuts import render
import requests
import json

urlBase = 'http://localhost:2115/ok-casa/'

def solicitud(request):
    context = {
        "usuario":{},
        "solicitud":{}
    }
    return render(request, "core/solicitud.html", context)

def historial(request):
    headers = {'content-type': 'application/json'}
    e = requests.get(urlBase + 'estadosol',headers=headers)
    s = requests.get(urlBase + 'solicitud',headers=headers)
    context = {
        "estados": e.json(),
        "solicitudes": s.json(),
        "ordenes": [
            { "id":0, "nombre":"Fecha descendente" },
            { "id":1, "nombre":"Fecha ascendente" },
        ]
    }
    return render(request, "core/historial.html", context)