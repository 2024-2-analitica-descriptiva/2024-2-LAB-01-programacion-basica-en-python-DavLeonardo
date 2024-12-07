"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    ruta = "files/input/data.csv"
    lista = []
    listaOrdenada = []
    listaClave = []
    listaValorMin = []
    listaValorMax = []

    with open(ruta, "r", encoding="utf-8") as files:
        lines = files.readlines()
    data = [linea.strip().split("\t") for linea in lines]

    for i in range(len(data)):
        lista.append(data[i][4])

    lista = [linea.strip().split(",") for linea in lista]

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            linea = lista[i][j].split(":")
            listaOrdenada.append(linea)

    for i in range(len(listaOrdenada)):
        if not (listaOrdenada[i][0] in listaClave):
            listaClave.append(listaOrdenada[i][0])
            listaValorMax.append(-1)
            listaValorMin.append(-1)
    listaClave.sort()

    print(listaValorMin[0])

    for i in range(len(listaClave)):
        for j in range(len(listaOrdenada)):

            # verificar si es la letra
            if listaClave[i] == listaOrdenada[j][0]:

                # verificar numero minimo
                if listaValorMin[i] == -1:
                    listaValorMin[i] = int(listaOrdenada[j][1])
                elif int(listaOrdenada[j][1]) < int(listaValorMin[i]):
                    listaValorMin[i] = int(listaOrdenada[j][1])

                # verificar numero maximo
                if listaValorMax[i] == -1:
                    listaValorMax[i] = int(listaOrdenada[j][1])
                elif int(listaOrdenada[j][1]) > int(listaValorMax[i]):
                    listaValorMax[i] = int(listaOrdenada[j][1])

    out = list(zip(listaClave, listaValorMin, listaValorMax))
    return out
