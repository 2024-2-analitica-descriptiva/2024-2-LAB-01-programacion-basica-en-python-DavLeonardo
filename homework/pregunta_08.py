"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

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
                if not data[j][0] in x:
                    x.append(data[j][0])
        x.sort()
        letras.append(x)

    numerosUnicos = list(map(int, numerosUnicos))

    out = list(
        zip(
            numerosUnicos,
            letras,
        )
    )
    return out
