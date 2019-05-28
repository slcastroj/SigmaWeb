from django.shortcuts import render

def solicitud(request):
    context = {
        "usuario":{},
        "solicitud":{}
    }
    return render(request, "core/solicitud.html", context)

def historial(request):
    context = {
        "estados": [
            { "id":0, "nombre":"Cualquiera" },
            { "id":1, "nombre":"Pendiente" },
            { "id":2, "nombre":"Cancelado" },
            { "id":3, "nombre":"Aprobado" },
            { "id":4, "nombre":"En seguimiento" },
            { "id":5, "nombre":"Finalizado" },
        ],
        "solicitudes": [
            {
                "nombre": "Verificación instalaciones",
                "direccion": "Av. Olimpo 423 Dpto. 32",
                "comuna": "Maipú",
                "fecha_creacion": "2018-08-18",
                "fecha_aprobacion": "2018-08-20",
                "fecha_inspeccion": "2018-08-29",
                "fecha_reparacion": "2018-09-19",
                "fecha_cierre": "2018-10-04", 
                "encargado": "Juan Acuña",
                "estado": "Finalizado"
            },
            {
                "nombre": "Inspección Infraestructura",
                "direccion": "Av. Olimpo 423 Dpto. 32",
                "comuna": "Maipú",
                "fecha_creacion": "2019-01-03",
                "fecha_aprobacion": "2018-01-06",
                "fecha_inspeccion": "2018-01-24", 
                "encargado": "Juan Acuña",
                "estado": "En seguimiento"
            }
        ],
        "ordenes": [
            { "id":0, "nombre":"Fecha descendente" },
            { "id":1, "nombre":"Fecha ascendente" },
        ]
    }
    return render(request, "core/historial.html", context)