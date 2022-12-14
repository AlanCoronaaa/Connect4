from lib_frames_conecta4 import *
from Generador_matrices import *
import datetime
import os
from datetime import datetime
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

#::::::::::::::::::::::::::::

registro_de_juegos = []
top_global = []


#::::::::::::::::::::::::::::

def cargar_archivos():
    cargarMatriz = (registro_juegos_localidad, registro_de_juegos)
    cargarMatriz = (top_global_localidad, top_global)


def buscar_elemento(matriz, columna, valor):
    id_elemento = -1
    for x in range(len(matriz)):
        if valor == matriz[x][columna].upper():
            id_elemento = x
            break
        else:
            id_elemento = -1
    return id_elemento


def registro_datos_partida(jugador_ganador, jugador_perdedor):
    score = 1
    id_nombre = buscar_elemento(top_global, 0, jugador_ganador.upper())
    lista_a_registro_juegos = [jugador_ganador, jugador_perdedor]
    lista_a_top_global = jugador_ganador
    registro_juegos_anadir = [lista_a_registro_juegos[0], lista_a_registro_juegos[1], datetime.now()]
    registro_de_juegos.append(registro_juegos_anadir)
    guardarMatriz = (registro_juegos_localidad, registro_de_juegos)
    if id_nombre == -1:
        top_global_anadir = [lista_a_top_global, score]
        top_global.append(top_global_anadir)
    else:
        top_global[id_nombre][1] = int(top_global[id_nombre][1]) + 1
    guardarMatriz = (top_global_localidad, top_global)

    print("Partida guardada")
    input()


def ingreso_de_datos(op):
    jugador_2 = "Computadora"
    jugador_1 = input("Nombre del jugador 1: ")
    if int(op) == 2:
        jugador_2 = input("Nombre del jugador 2: ")
    return jugador_1, jugador_2


def main(op_juego):
    os.system("cls")
    instrucciones()
    input()
    os.system("cls")
    reiniciar_variables()
    juego = True
    turno_jugador = 1
    jugadores = ingreso_de_datos(op_juego)
    while juego:
        os.system("cls")
        imprimir_forma()
        re_ingresar = True
        while re_ingresar:
            if turno_jugador == 1:
                print(f"Turno de {jugadores[0]} (Jugador 1)\n")
                jugada = input("Elige tu opcion ---> ")
                if validacion_numero(jugada):
                    jugada = int(jugada)
                    if n_columnas >= jugada >= 0:
                        jugada -= 1
                        print(Fore.RED + Back.RED)
                        agregar_ficha_matriz(jugada, ficha1)
                        turno_jugador = 2
                        re_ingresar = False
                    else:
                        print("Columna invalida")
                        re_ingresar == True
                else:
                    print("Columna invalida")
                    re_ingresar == True

            else:
                print(f"Turno de {jugadores[1]} (Jugador 2)\n")
                if int(op_juego) == 2:
                    jugada = input("Elige tu opcion ---> ")
                else:
                    jugada = valor_compu()
                    input("Enter para continuar")
                if validacion_numero(jugada):
                    jugada = int(jugada)
                    if n_columnas >= jugada >= 0:
                        jugada -= 1
                        print(Fore.YELLOW + Back.YELLOW)
                        agregar_ficha_matriz(jugada, ficha2)
                        turno_jugador = 1
                        re_ingresar = False

                    else:
                        print("Columna invalida")
                        re_ingresar == True
                else:
                    print("Columna invalida")
                    re_ingresar == True
            estado_ganadores = inspeccion()
            if estado_ganadores[0]:
                os.system("cls")
                imprimir_forma()
                print(Felicidades_jugador1[0])
                registro_datos_partida(jugadores[0], jugadores[1])
                input()
                juego = False
            elif estado_ganadores[1]:
                os.system("cls")
                imprimir_forma()
                print(Felicidades_jugador2[0])
                registro_datos_partida(jugadores[1], jugadores[0])
                input()
                juego = False

    os.system("cls")


if __name__ != '__main__':
    pass
else:
    cargar_archivos()
    inicio()
    input()
    opcion_juego = 1
    os.system("cls")
    opcion_juego = menu()
    while opcion_juego != "5":
        os.system("cls")
        if opcion_juego == "1" or opcion_juego == "2":
            main(opcion_juego)
        elif opcion_juego == "3":
            top_global = sorted(top_global, key=lambda x: -int(x[1]))
            os.system("cls")
            print("""
    Jugador || Numero de partidas ganadas
    """)
            imprimir_tablas(top_global)
            input("\n  Preciona ENTER para continuar")
        elif opcion_juego == "4":
            os.system("cls")
            print("""
    Ganador  || Perdedor  || Fecha
    """)
            imprimir_tablas(registro_de_juegos)
            input("\n  Preciona ENTER para continuar")
        else:
            os.system("cls")
            print("Valor no valido en el menu\n")
            opcion_juego = menu()
        os.system("cls")
        opcion_juego = menu()
