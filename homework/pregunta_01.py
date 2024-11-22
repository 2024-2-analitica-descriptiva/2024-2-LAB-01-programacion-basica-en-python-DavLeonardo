"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    ruta = "files/input/data.csv"
    suma = 0
    with open(ruta, "r", encoding="utf-8") as files:
        lines = files.readlines()

    data = [linea.strip().split("\t") for linea in lines]
    for i in range(len(data)):
        suma = suma + int(data[i][1])
    return suma
