"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    RUTA = "files/input/data.csv"

    claves = []
    lista = []
    claves_clean = []
    out = {}

    with open(RUTA, "r", encoding="utf-8") as files:
        lines = files.readlines()
    data = [linea.strip().split("\t") for linea in lines]

    for i in enumerate(data):
        lista.extend(i[1][4].split(","))

    for i in lista:
        x = i.split(":")[0]
        claves_clean.append(x)
    claves_clean.sort()

    for claves in claves_clean:
        if not claves in out:
            out[claves] = 1
        else:
            out[claves] += 1

    return out
