import random
from random import *

def calificaciones(valor):
    # Genera una matriz de 8x5, con las calificaciones intruducidas manual mente

    filas = 8
    columnas = 5

    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):

            valor = float(input("Fila {}, Columna {} : ".format(i+1, j+1)))

            randomNumber = [
                [5, 6, 7, 8, 9, 10]
            ]
            valor = random.choice(randomNumber)

    print()

    for fila in matriz:
        print("[", end=" ")
        for elemento in fila:
            print("{:8.2f}".format(elemento), end=" ")
            print("]")
    print()

def imprime_matriz():
    [matrizx].str.split(' \ ', expand=True)

def examen_final(N,M):
    N = 8
    M = 5

    m = [[randint(5, 10) for j in range(M)] for i in range(N)]

    for f in m:
        print(f)


def imprime_lista([luni]):
    luni= [5,6,7,8,9,10]
    print(' '.join(map(str, luni)))


def saca_promedios(filas: object, columnas: object) -> object:
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(filas):
        matriz1.append([0] * columnas)
        matriz2.append([0] * columnas)
        matriz3.append([0] * columnas)

    print('Ingrese su Matriz 1: ')

    for i in range(filas):
        for j in range(columnas):
            matriz1[i][j] = int(input('Elemento (%d,%d): ' % (i, j)))
    print('Ingrese su Matriz 2: ')
    for i in range(filas):
        for j in range(columnas):
            matriz2[i][j] = int(input('Elemento (%d,%d): ' % (i, j)))

    for i in range(filas):
        for j in range(columnas):
            matriz3[i][j] += matriz1[i][j] + matriz2[i][j]
    print('Su matriz resultante es: ')
    return matriz3/5


if __name__ == '__main__':

    imprime_lista()
    filas = 8
    columnas = 5
    print(saca_promedios(filas, columnas))
    print()
    N = 8
    M = 5
    print(examen_final(N,M))
    matrizx= [2, 2, 3, 5, 4, 9, 1, 7, 7, 7, 4]
            [4, 8, 1, 9, 9, 6, 6, 10, 9, 2, 7]
            [7, 7, 8, 5, 1, 4, 9, 2, 3, 6, 10]
            [7, 3, 8, 8, 8, 6, 6, 2, 9, 7, 8]
            [3, 9, 10, 3, 5, 5, 8, 8, 10, 8, 5]
            [5, 4, 2, 2, 10, 9, 9, 9, 10, 3, 9]
        ]

    imprime_matriz(matrizx)

    opcion_menu = 1
        os.system("cls")
        opcion_menu = menu()
        while opcion_menu != "5":
            os.system("cls")
            if opcion_menu == "1" or opcion_menu == "2":
                main(opcion_menu)
                saca_promedios()
            elif opcion_menu == "3":
                examen_final()
                os.system("cls")

            elif opcion_menu == "4":
                imprime_lista()
                os.system("cls")
            elif opcion_menu == "6":
                calificaciones()
            else:
                os.system("cls")
                print("Valor no valido en el menu\n")
                opcion_menu = menu()
            os.system("cls")
            opcion_menu = menu()


