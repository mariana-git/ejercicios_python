# Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto
# de precios arme un diccionario donde las claves sean los nombres de
# frutas y verduras, y los valores sean los precios por cajón.
# Para hacerlo, empezá con un diccionario vacío y andá agregándole valores igual
#  a como hiciste antes, pero ahora esos valores los vas leyendo del archivo.

import csv
from pprint import pprint


def leer_precios(nombre_archivo):
    precios = {}

    with open(nombre_archivo, encoding="utf8") as f:
        rows = csv.reader(f)
        try:
            for k, v in rows:
                precios[k] = float(v)

        except Exception as e:
            print(e)
    return precios


precios = leer_precios("./Data/precios.csv")
pprint(precios)
