from django.urls import path
from . import views


urlpatterns = [
    path('afkmode/combat', views.movimientos_jugadores),
]
