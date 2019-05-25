from django.shortcuts import render

def solicitud(request):
    return render(request, "core/solicitud.html")

def historial(request):
    return render(request, "core/historial.html")