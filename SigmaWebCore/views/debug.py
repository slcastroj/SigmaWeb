from django.shortcuts import render

def base(request):
    return render(request, "core/__base__.html")