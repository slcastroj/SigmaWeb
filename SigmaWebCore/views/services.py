from django.shortcuts import render

def cotizacion(request, id):
    return render(request, "core/cotizacion.html")

def solicitud(request, id):
    return render(request, "core/solicitud.html")