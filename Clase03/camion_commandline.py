import csv
import sys


def costo_camion(nombre_archivo):
    costo_pagado = 0
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                costo_pagado += float(row[2]) * int(row[1])
            except Exception as e:
                print(e)
    return costo_pagado


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = "./Data/camion.csv"

costo = costo_camion(nombre_archivo)
print("Costo total (f): ", costo)


# sys.argv es una lista que contiene los argumentos que le pasamos al script al
# momento de llamarlo desde la línea de comandos (si es que le pasamos alguno).
# Por ejemplo, desde una terminal de Unix (en Windows es similar), para correr
#  nuestro programa y que procese el mismo archivo podríamos escribir:

# bash $ python3 camion_commandline.py ../Data/camion.csv
