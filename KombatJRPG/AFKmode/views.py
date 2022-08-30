from django.http import JsonResponse
import json
from .functions import Joystick
joystick = Joystick()


def movimientos_jugadores(request):
    data = joystick.kombat_simulacion()
    return JsonResponse(data)


combinacion_tonyn = joystick.secuencia_tecnicas('tonyn')
combinacion_arnaldor = joystick.secuencia_tecnicas('arnaldor')
primer_turno = joystick.primer_turno(combinacion_tonyn, combinacion_arnaldor)
resultado_pelea = joystick.resultado_pelea(primer_turno, combinacion_tonyn, combinacion_arnaldor)
