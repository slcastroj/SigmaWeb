from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def servicios(request):
    return render(request, "core/servicios.html")