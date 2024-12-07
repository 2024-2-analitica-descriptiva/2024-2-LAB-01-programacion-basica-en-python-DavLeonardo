"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    ruta = "files/input/data.csv"
    Letras = []
    listaLetras = []
    mesMin = []
    mesMax = []
    with open(ruta, "r", encoding="utf-8") as files:
        lines = files.readlines()
    data = [linea.strip().split("\t") for linea in lines]

    for i in range(len(data)):
        fila = (data[i][0], data[i][1])
        Letras.append(fila)

    #! lista de meses
    for i in range(len(Letras)):
        if not (Letras[i][0] in listaLetras):
            listaLetras.append(Letras[i][0])
            mesMin.append(-1)
            mesMax.append(-1)
    listaLetras.sort()

    #! buscar minimos y maximos
    for i in range(len(listaLetras)):
        for j in range(len(Letras)):

            # verificar si es la letra
            if listaLetras[i] == Letras[j][0]:

                # verificar numero minimo
                if mesMin[i] == -1:
                    mesMin[i] = int(Letras[j][1])
                elif int(Letras[j][1]) < int(mesMin[i]):
                    mesMin[i] = int(Letras[j][1])

                # verificar numero maximo
                if mesMax[i] == -1:
                    mesMax[i] = int(Letras[j][1])
                elif int(Letras[j][1]) > int(mesMax[i]):
                    mesMax[i] = int(Letras[j][1])

    out = list(zip(listaLetras, mesMax, mesMin))
    return out
