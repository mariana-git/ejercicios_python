# Usando este código del Ejercicio 2.9 "costo_camion.py" como guía,
#  definí una función leer_camion(nombre_archivo) que abre un archivo con
# el contenido de un camión, lo lee y devuelve la información como una
# lista de tuplas. Para hacerlo vas a tener que hacer algunas
# modificaciones menores al código de arriba.

import csv
from pprint import pprint


def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                lote = (row[0], int(row[1]), float(row[2]))
                camion.append(lote)
        except Exception as e:
            print(e)
    return camion


costo = leer_camion("./Data/camion.csv")
pprint(costo)
