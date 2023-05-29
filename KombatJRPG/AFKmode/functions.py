import json


class Joystick:

    def accion_botones(self):
        accion_boton = {
            "W": "Arriba",
            "S": "Abajo",
            "A": "Izquierda",
            "D": "Derecha",
            "P": "Puño",
            "K": "Patada"
        }
        return accion_boton

    def tonyn_movimientos(self, combinacion):
        movimientos = {
            "DSD+P": "Taladoken",
            "SD+K": "Remuyuken",
            "P": "Puño",
            "K": "Patada"
        }
        movimiento = movimientos[combinacion]
        return movimiento

    def arnaldor_movimientos(self, combinacion):
        movimientos = {
            "SA+K": "Remuyuken",
            "ASA+P": "Taladoken",
            "P": "Puño",
            "K": "Patada"
        }
        movimiento = movimientos[combinacion]
        return movimiento

    def energia_movimientos(self, movimiento):
        energias = {
            "DSD+P": 3,
            "SA+K": 3,
            "SD+K": 2,
            "ASA+P": 2,
            "P": 1,
            "K": 1
        }
        try:
            energia = energias[movimiento]
        except (Exception, ):
            energia = False
        return energia

    def kombat_simulacion(self):
        kombat_json = open('static/Kombat_simulation.json').read()
        kombat_secuencia = json.loads(kombat_json)
        return kombat_secuencia

    def secuencia_tecnicas(self, player):
        ataques_jugadores = self.kombat_simulacion()
        ataques_jugador = ataques_jugadores['Jugadores']
        movimientos_jugador = ataques_jugador[player]['movimientos']
        golpes_jugador = ataques_jugador[player]['golpes']
        combinacion_jugador = []
        for i in range(len(movimientos_jugador)):
            movimientos_jugador[i] = movimientos_jugador[i] + "+"
            combinacion_jugador.append(movimientos_jugador[i] + f"{golpes_jugador[i]}")
        return combinacion_jugador

    def primer_turno(self, combinacion_tonyn, combinacion_arnaldor):
        tonyn = 'tonyn'
        arnaldor = 'arnaldor'
        for secuencia_ataque in range(len(combinacion_tonyn)):
            if len(combinacion_tonyn[secuencia_ataque]) == len(combinacion_arnaldor[secuencia_ataque]):
                if secuencia_ataque == 4:
                    return tonyn
                else:
                    continue
            elif len(combinacion_tonyn[secuencia_ataque]) < len(combinacion_arnaldor[secuencia_ataque]):
                return tonyn
            else:
                return arnaldor

    def resultado_pelea(self, primer_turno, combinacion_tonyn, combinacion_arnaldor):
        resultado_final = ""
        salud_tonyn = 6
        salud_arnaldor = 6
        if primer_turno == 'tonyn':
            for turno in range(len(combinacion_tonyn)):
                ejecucion_tonyn = combinacion_tonyn[turno]
                if self.energia_movimientos(ejecucion_tonyn) is False:
                    movimiento_golpe_tonyn = ejecucion_tonyn.split('+')
                    movimiento_tonyn = movimiento_golpe_tonyn[0]
                    golpe_tonyn = movimiento_golpe_tonyn[1]
                    if movimiento_tonyn == '':
                        salud_arnaldor = salud_arnaldor - int(self.energia_movimientos(golpe_tonyn))
                        print(f"Tonyn lanza una {self.tonyn_movimientos(golpe_tonyn)}")
                        resultado_final = (resultado_final + f"Tonyn lanza una {self.tonyn_movimientos(golpe_tonyn)}""\n")
                    elif golpe_tonyn == '':
                        print(f"Tonyn se mueve pero no ejecuta un golpe")
                        resultado_final = (resultado_final + f"Tonyn se mueve pero no ejecuta un golpe""\n")
                    else:
                        salud_arnaldor = salud_arnaldor - int(self.energia_movimientos(golpe_tonyn))
                        print(f"Tonyn se mueve y ejecuta un {self.tonyn_movimientos(golpe_tonyn)}")
                        resultado_final = (resultado_final + f"Tonyn se mueve y ejecuta un {self.tonyn_movimientos(golpe_tonyn)}""\n")
                else:
                    especial_daño_tonyn = self.energia_movimientos(ejecucion_tonyn)
                    especial_nombre_tonyn = self.tonyn_movimientos(ejecucion_tonyn)
                    salud_arnaldor = salud_arnaldor - int(especial_daño_tonyn)
                    print(f"Tonyn conecto un {especial_nombre_tonyn}")
                    resultado_final = (resultado_final + f"Tonyn conecto un {especial_nombre_tonyn}""\n")

                if salud_arnaldor == 0:
                    print(f"Tonyn es el victorioso con {salud_tonyn} de energia restante")
                    resultado_final = (resultado_final + f"Tonyn es el victorioso con {salud_tonyn} de energia restante""\n")
                    break

                ejecucion_arnaldor = combinacion_arnaldor[turno]
                if self.energia_movimientos(ejecucion_arnaldor) is False:
                    movimiento_golpe_arnaldor = ejecucion_arnaldor.split('+')
                    movimiento_arnaldor = movimiento_golpe_arnaldor[0]
                    golpe_arnaldor = movimiento_golpe_arnaldor[1]
                    if movimiento_arnaldor == '':
                        salud_tonyn = salud_tonyn - int(self.energia_movimientos(golpe_arnaldor))
                        print(f"Arnaldor lanza una {self.arnaldor_movimientos(golpe_arnaldor)}")
                        resultado_final = (resultado_final + f"Arnaldor lanza una {self.arnaldor_movimientos(golpe_arnaldor)}""\n")

                    elif golpe_arnaldor == '':
                        print(f"Arnaldor se mueve pero no ejecuta un golpe")
                        resultado_final = (resultado_final + "Arnaldor se mueve pero no ejecuta un golpe""\n")
                    else:
                        salud_tonyn = salud_tonyn - int(self.energia_movimientos(golpe_arnaldor))
                        print(f"Arnaldor se mueve y ejecuta un {self.arnaldor_movimientos(golpe_arnaldor)}")
                        resultado_final = (resultado_final + f"Arnaldor se mueve y ejecuta un {self.arnaldor_movimientos(golpe_arnaldor)}""\n")
                else:
                    especial_daño_arnaldor = self.energia_movimientos(ejecucion_arnaldor)
                    especial_nombre_arnaldor = self.arnaldor_movimientos(ejecucion_arnaldor)
                    salud_tonyn = salud_tonyn - int(especial_daño_arnaldor)
                    print(f"Arnaldor conecto un {especial_nombre_arnaldor}")
                    resultado_final = (resultado_final + f"Arnaldor conecto un {especial_nombre_arnaldor}""\n")

                if salud_tonyn == 0:
                    print(f"Arnaldor es el victorioso con {salud_arnaldor} de energia restante")
                    resultado_final = (resultado_final + f"Arnaldor es el victorioso con {salud_arnaldor} de energia restante""\n")
                    break
        else:
            for turno in range(len(combinacion_tonyn)):
                ejecucion_arnaldor = combinacion_arnaldor[turno]
                if self.energia_movimientos(ejecucion_arnaldor) is False:
                    movimiento_golpe_arnaldor = ejecucion_arnaldor.split('+')
                    movimiento_arnaldor = movimiento_golpe_arnaldor[0]
                    golpe_arnaldor = movimiento_golpe_arnaldor[1]
                    if movimiento_arnaldor == '':
                        salud_tonyn = salud_tonyn - int(self.energia_movimientos(golpe_arnaldor))
                        print(f"Arnaldor lanza una {self.arnaldor_movimientos(golpe_arnaldor)}")
                        resultado_final = (resultado_final + f"Arnaldor lanza una {self.arnaldor_movimientos(golpe_arnaldor)}""\n")

                    elif golpe_arnaldor == '':
                        print(f"Arnaldor se mueve pero no ejecuta un golpe")
                        resultado_final = (resultado_final + f"Arnaldor se mueve pero no ejecuta un golpe""\n")

                    else:
                        salud_tonyn = salud_tonyn - int(self.energia_movimientos(golpe_arnaldor))
                        print(f"Arnaldor se mueve y ejecuta un {self.arnaldor_movimientos(golpe_arnaldor)}")
                        resultado_final = (resultado_final + f"Arnaldor se mueve y ejecuta un {self.arnaldor_movimientos(golpe_arnaldor)}""\n")

                else:
                    especial_daño_arnaldor = self.energia_movimientos(ejecucion_arnaldor)
                    especial_nombre_arnaldor = self.arnaldor_movimientos(ejecucion_arnaldor)
                    salud_tonyn = salud_tonyn - int(especial_daño_arnaldor)
                    print(f"Arnaldor conecto un {especial_nombre_arnaldor}")
                    resultado_final = (resultado_final + f"Arnaldor conecto un {especial_nombre_arnaldor}""\n")

                if salud_tonyn == 0:
                    print(f"Arnaldor es el victorioso con {salud_arnaldor} de energia restante")
                    resultado_final = (resultado_final + f"Arnaldor es el victorioso con {salud_arnaldor} de energia restante""\n")
                    break
    
                    ejecucion_tonyn = combinacion_tonyn[turno]
                    if self.energia_movimientos(ejecucion_tonyn) is False:
                        movimiento_golpe_tonyn = ejecucion_tonyn.split('+')
                        movimiento_tonyn = movimiento_golpe_tonyn[0]
                        golpe_tonyn = movimiento_golpe_tonyn[1]
                        if movimiento_tonyn == '':
                            salud_arnaldor = salud_arnaldor - int(self.energia_movimientos(golpe_tonyn))
                            print(f"Tonyn lanza una {self.tonyn_movimientos(golpe_tonyn)}")
                            resultado_final = (resultado_final + f"Tonyn lanza una {self.tonyn_movimientos(golpe_tonyn)}""\n")

                        elif golpe_tonyn == '':
                            print(f"Tonyn se mueve pero no ejecuta un golpe")
                            resultado_final = (resultado_final + f"Tonyn se mueve pero no ejecuta un golpe""\n")

                        else:
                            salud_arnaldor = salud_arnaldor - int(self.energia_movimientos(golpe_tonyn))
                            print(f"Tonyn se mueve y ejecuta un {self.tonyn_movimientos(golpe_tonyn)}")
                            resultado_final = (resultado_final + f"Tonyn se mueve y ejecuta un {self.tonyn_movimientos(golpe_tonyn)}""\n")

                    else:
                        especial_daño_tonyn = self.energia_movimientos(ejecucion_tonyn)
                        especial_nombre_tonyn = self.tonyn_movimientos(ejecucion_tonyn)
                        salud_arnaldor = salud_arnaldor - int(especial_daño_tonyn)
                        print(f"Tonyn conecto un {especial_nombre_tonyn}")
                        resultado_final = (resultado_final + f"Tonyn conecto un {especial_nombre_tonyn}""\n")

                    if salud_arnaldor == 0:
                        print(f"Tonyn es el victorioso con {salud_tonyn} de energia restante")
                        resultado_final = (resultado_final + f"Tonyn es el victorioso con {salud_tonyn} de energia restante")

                        break
        if salud_tonyn > 0 and salud_arnaldor > 0:
            print("Tenemos un Empate. Ambos jugadores lucharon valerosamente hasta el ultimo minuto.")
            resultado_final = (resultado_final + "Tenemos un Empate. Ambos jugadores lucharon valerosamente hasta el ultimo minuto.""\n")
        return resultado_final
