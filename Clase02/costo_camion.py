# jercicio 2.2: Lectura de un archivo de datos
# Las columnas en Data/camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión,
# y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el
# archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

costo_pagado = 0

with open("./Data/camion.csv", "rt", encoding="utf8") as f:
    headers = next(f).split(",")  # quito el header con los nombres de las columnas
    for line in f:
        row = line.split(",")
        precio_x_cajon = float(row[2])
        cant_cajones = int(row[1])
        costo_pagado += precio_x_cajon * cant_cajones
print("Costo total: ", costo_pagado)


# Ejercicio 2.6: Transformar un script en una función
# Transformá el programa anterior en una función costo_camion(nombre_archivo). Esta función recibe un nombre
#  de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve el costo de
# la carga de frutas como una variable de punto flotante.


def costo_camion(nombre_archivo):
    costo_pagado = 0
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        headers = next(f).split(",")  # quito el header con los nombres de las columnas
        for line in f:
            row = line.split(",")
            precio_x_cajon = float(row[2])
            cant_cajones = int(row[1])
            costo_pagado += precio_x_cajon * cant_cajones
    return costo_pagado


costo = costo_camion("./Data/camion.csv")
print("Costo total (f): ", costo)


# Modificá tu programa costo_camion.py para que use el módulo csv para leer los archivos CSV y probalo en un
# par de los ejemplos anteriores. Modificá el programa costo_camion.py para que atrape la excepción con un
#  bloque try - except, imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.

import csv


def costo_camion2(nombre_archivo):
    costo_pagado = 0
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                costo_pagado += float(row[2]) * int(row[1])
            except Exception as e:
                print(e)
    return costo_pagado


costo2 = costo_camion2("./Data/missing.csv")
print("Costo total (csv): ", costo2)
