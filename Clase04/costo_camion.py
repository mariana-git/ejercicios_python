#  copiá tu programa costo_camion.py a la carpeta de la clase actual, y modificalo de forma
# que imprima un aviso (warning) cada vez que encuentre una fila incorrecta, indicando el
# número de fila.

import csv


def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record["cajones"])
                precio = float(record["precio"])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
    return costo_total


costo_total = costo_camion("./Data/fecha_camion.csv")
print("Costo total (csv): ", costo_total)
