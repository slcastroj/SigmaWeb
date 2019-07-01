from django.shortcuts import render
import requests
import json

urlBase = 'http://localhost:2115/ok-casa/'

def index(request):
    return render(request, "core/index.html")

def servicios(request):
    headers = {'content-type': 'application/json'}
    s = requests.get(urlBase + 'servicio',headers=headers)
    context = {
        "servicios": s.json()
    }
    return render(request, "core/servicios.html", context)