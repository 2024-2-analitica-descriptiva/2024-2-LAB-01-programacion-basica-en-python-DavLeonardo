"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    ruta = "files/input/data.csv"
    letra = []
    numero = []
    ListaLetras = []
    SumaNumeros = []

    with open(ruta, "r", encoding="utf-8") as files:
        lines = files.readlines()

    data = [linea.strip().split("\t") for linea in lines]

    for i in range(len(data)):
        letra.append(data[i][0])
        numero.append(data[i][1])

    #! lista de las letras
    for i in range(len(letra)):
        if not (letra[i] in ListaLetras):
            ListaLetras.append(letra[i])
            SumaNumeros.append(0)
    ListaLetras.sort()

    #! suma de los numeros
    for i in range(len(ListaLetras)):
        for j in range(len(letra)):
            if letra[j] == ListaLetras[i]:
                SumaNumeros[i] += int(numero[j])

    out = list(zip(ListaLetras, SumaNumeros))
    return out
