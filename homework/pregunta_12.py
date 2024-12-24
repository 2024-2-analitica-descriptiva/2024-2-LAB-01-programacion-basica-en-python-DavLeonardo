"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    RUTA = "files/input/data.csv"
    out = {}
    out_ordendado = {}

    with open(RUTA, "r", encoding="utf-8") as files:
        lines = files.readlines()
    data = [linea.strip().split("\t") for linea in lines]

    for datos in data:
        linea = []
        suma = 0  # pylint: disable=invalid-name
        for valores in datos[4].split(","):
            linea = valores.split(":")
            suma += int(linea[1])

        if not datos[0] in out:
            out[datos[0]] = suma
        else:
            out[datos[0]] += suma

    for clave in sorted(out):
        out_ordendado[clave] = out[clave]

    return out_ordendado
