"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    ruta = "files/input/data.csv"
    mapper = []
    listaFinal = {}

    with open(ruta, "r", encoding="utf-8") as files:
        lines = files.readlines()

    data = [linea.strip().split("\t") for linea in lines]

    for i in range(len(data)):
        tupla = (data[i][0], 1)
        mapper.append(tupla)

    for key, value in mapper:
        if key in listaFinal:
            listaFinal[key] += value
        else:
            listaFinal[key] = value

    ListaOredana = {key: listaFinal[key] for key in sorted(listaFinal)}
    ListaOredana = list(ListaOredana.items())
    return ListaOredana
