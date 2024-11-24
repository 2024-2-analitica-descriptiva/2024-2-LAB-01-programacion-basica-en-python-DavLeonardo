"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    ruta = "files/input/data.csv"
    fecha = []
    listaMeses = []
    sumaMeses = []
    with open(ruta, "r", encoding="utf-8") as files:
        lines = files.readlines()
    data = [linea.strip().split("\t") for linea in lines]

    for i in range(len(data)):
        linea = data[i][2].split("-")
        fecha.append(linea)

    #! lista de meses
    for i in range(len(fecha)):
        if not (fecha[i][1] in listaMeses):
            listaMeses.append(fecha[i][1])
            sumaMeses.append(0)
    listaMeses.sort()

    #! suma de los numeros
    for i in range(len(listaMeses)):
        for j in range(len(fecha)):
            if fecha[j][1] == listaMeses[i]:
                sumaMeses[i] += 1

    out = list(zip(listaMeses, sumaMeses))
    return out
