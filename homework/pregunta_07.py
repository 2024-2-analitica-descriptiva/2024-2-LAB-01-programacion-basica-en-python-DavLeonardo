"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    ruta = "files/input/data.csv"
    numeros = []
    letras = []
    numerosUnicos = []
    with open(ruta, "r", encoding="utf-8") as files:
        lines = files.readlines()
    data = [linea.strip().split("\t") for linea in lines]

    for i in range(len(data)):
        numeros.append(data[i][1])

    for i in range(len(numeros)):
        if not (numeros[i] in numerosUnicos):
            numerosUnicos.append(numeros[i])
    numerosUnicos.sort()

    for i in range(len(numerosUnicos)):
        x = []
        for j in range(len(data)):
            if numerosUnicos[i] == data[j][1]:
                x.append(data[j][0])
        letras.append(x)

    numerosUnicos = list(map(int, numerosUnicos))

    out = list(
        zip(
            numerosUnicos,
            letras,
        )
    )
    return out
