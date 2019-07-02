from django.shortcuts import render
import requests
from .users import GetUser
import json

urlBase = 'http://localhost:2115/ok-casa/'

user = GetUser()

def index(request):
    return render(request, "core/index.html",{"usuario":user})

def servicios(request):
    headers = {'content-type': 'application/json'}
    s = requests.get(urlBase + 'servicio',headers=headers)
    context = {
        "servicios": s.json(),
        "usuario":user
    }
    print(context)
    return render(request, "core/servicios.html", context)