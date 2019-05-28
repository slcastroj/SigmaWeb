from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def servicios(request):
    context = {
        "servicios": [
            { 
                "nombre": "Verificación instalaciones",
                "descripcion": "Mediante la verificación de instalaciones puedes ver si tu casa cumple los requerimientos arquitectónicos prometidos, así como los estándares de calidad y seguridad del mercado actuales."
            },
            { 
                "nombre": "Medición vivienda",
                "descripcion": "La medición de vivienda te permite asegurar que tu casa cumple el tamaño prometido, así como la estimación de espacios disponibles para ti y tu familia."
            },
            { 
                "nombre": "Inspección Infraestructura",
                "descripcion": "La inspección de infraestructura asegura que tu vivienda cumple todos los estándares de instalación de luminaria, agua potable y tuberías de gas, para que te sientas seguro en tu nuevo hogar."
            },
            { 
                "nombre": "Termografía",
                "descripcion": "A través de la termografía prometemos comodidad , entregando espacios con una temperatura de acorde a las necesidades de ti y tus seres queridos, en todo momento."
            },
        ]
    }
    return render(request, "core/servicios.html", context)