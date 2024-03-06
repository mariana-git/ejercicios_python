# Copiá el programa informe.py que escribiste antes (ver Ejercicio 3.4)
# a la carpeta de ejercicios de la clase actual, y modificalo para que
# use esta técnica para elegir las columnas a partir de sus encabezados.
# Probá correr el programa informe.py sobre el archivo Data/fecha_camion.csv
# y fijate si da la misma salida que antes.


import csv
import sys
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


def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                nombre = record["nombre"]
                ncajones = record["cajones"]
                precio = record["precio"]
                lote = (nombre, ncajones, precio)
                camion.append(lote)
            except ValueError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
    return camion


def hacer_informe(archivo_camion, archivo_precios):
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    tabla = []

    for producto, cajones, precio in camion:
        cambio = round(precios[producto] - float(precio), 2)
        tabla.append((producto, int(cajones), "$" + precio, cambio))

    return tabla


if len(sys.argv) == 2:
    archivo_camion = sys.argv[1]
    archivo_precios = sys.argv[2]
else:
    archivo_camion = "./Data/fecha_camion.csv"
    archivo_precios = "./Data/precios.csv"

informe = hacer_informe(archivo_camion, archivo_precios)
# for r in informe:
#     print("%10s %10d %10.2f %10.2f" % r)

headers = ("Nombre", "Cajones", "Precio", "Cambio")
headers_separators = []
for h in headers:
    headers_separators.append("-" * 9)

header_format = "%10s %10s %10s %10s"

print(header_format % headers)
print(header_format % tuple(headers_separators))

for nombre, cajones, precio, cambio in informe:
    print(f"{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}")
