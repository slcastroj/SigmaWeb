from django.urls import path, include

from .views import debug

urlpatterns = [
    path('base', debug.base, name='base')
]
