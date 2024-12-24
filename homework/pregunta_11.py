"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    RUTA = "files/input/data.csv"
    out = {}
    out_ordendado = {}

    with open(RUTA, "r", encoding="utf-8") as files:
        lines = files.readlines()
    data = [linea.strip().split("\t") for linea in lines]

    for datos in data:
        letras = datos[3].split(",")
        for letra in letras:
            if not letra in out:
                out[letra] = int(datos[1])
            else:
                out[letra] += int(datos[1])

    for clave in sorted(out):
        out_ordendado[clave] = out[clave]

    return out_ordendado
