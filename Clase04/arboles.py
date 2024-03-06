# Definí una función leer_parque(nombre_archivo, parque) que abra el archivo de arbolado y
# devuelva una lista de diccionarios con la información del parque especificado. La lista
# debe tener un diccionario por cada árbol del parque elegido. Dicho diccionario debe
# tener los datos correspondientes a un árbol (recordá que cada fila del csv corresponde
# a un árbol).

import csv
import sys
from collections import Counter


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = "./Data/arbolado-en-espacios-verdes.csv"

parque = "CENTENARIO"
especie = "Jacarandá"


def leer_parque(nombre_archivo, parque=None):
    """devuelva una lista de diccionarios con la información del parque especificado.
    La lista debe tener un diccionario por cada árbol del parque elegido. Dicho diccionario
    debe tener los datos correspondientes a un árbol (recordá que cada fila del csv
    corresponde a un árbol)."""

    resultado = []
    with open(nombre_archivo, encoding="utf-8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))

            if parque:
                if record["espacio_ve"] == parque:
                    try:
                        resultado.append(record)
                    except ValueError:
                        print(f"Fila {n_fila}: No pude interpretar: {fila}")

            else:
                try:
                    resultado.append(record)
                except ValueError:
                    print(f"Fila {n_fila}: No pude interpretar: {fila}")

    return resultado


lista_arboles = leer_parque(nombre_archivo, parque)


def especies(lista_arboles):
    """toma una lista de árboles como la generada en el ejercicio anterior y devuelve el conjunto
    de especies (la columna 'nombre_com' del archivo) que figuran en la lista."""
    especies = []
    for a in lista_arboles:
        especies.append(a["nombre_com"])
    especies = set(especies)
    return especies


def contar_ejemplares(lista_arboles):
    """dada una lista como la generada con leer_parque(), devuelve un diccionario contador en
    el que las especies (recordá, es la columna 'nombre_com' del archivo) sean las claves y tengan
    como valores asociados la cantidad de ejemplares en esa especie en la lista dada."""
    contador_ejemplares = Counter()
    for a in lista_arboles:
        contador_ejemplares[a["nombre_com"]] += 1
    return contador_ejemplares


def ejemplares_mas_comunes(lista_arboles):
    """combinando esta función con leer_parque() y con el método most_common() para informar las
    cinco especies más frecuentes en cada uno de los siguientes parques:"""
    contador_ejemplares = contar_ejemplares(lista_arboles)
    mas_comunes = contador_ejemplares.most_common(5)
    return mas_comunes


def obtener_alturas(lista_arboles, especie):
    """dada una lista de árboles como la anterior y una especie de árbol (un valor de la columna
    'nombre_com' del archivo), devuelve una lista con las alturas (columna 'altura_tot') de los
    ejemplares de esa especie en la lista."""
    alturas = []
    for l in lista_arboles:
        if l["nombre_com"] == especie:
            alturas.append(l["altura_tot"])
    return alturas


# parque = "CENTENARIO"
# especie = "Jacarandá"
# lista_arboles = leer_parque(nombre_archivo, parque)
# alt = obtener_alturas(lista_arboles, especie)
# print(f"Total de {especie} en {parque}:", len(alt))
# if alt:
#     print("Altura maxima: ", max(alt))
#     average = round(sum(alt) / len(alt), 2)
#     print("Altura promedio: ", average)


def obtener_inclinaciones(lista_arboles, especie):
    """dada una especie de árbol y una lista de árboles como la anterior, devuelve una lista
    con las inclinaciones (columna 'inclinacio') de los ejemplares de esa especie."""
    inclinaciones = []
    for l in lista_arboles:
        if l["nombre_com"] == especie:
            inclinaciones.append(int(l["inclinacio"]))
    return inclinaciones


def especimen_mas_inclinado(lista_arboles):
    """dada una lista de árboles devuelve la especie que tiene el ejemplar más inclinado y su inclinación."""
    lista_especies = especies(lista_arboles)
    result = {}
    for e in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, e)
        result[e] = max(inclinaciones)
    result = list(zip(result.values(), result.keys()))
    result = max(result)
    return result


# max_inclinacion = especimen_mas_inclinado(lista_arboles)
# print(
#     f"\nEn el parque {parque} el especimen con mayor inclinación es un {max_inclinacion[1]} con una inclinación de {max_inclinacion[0]}º.\n"
# )


def especie_promedio_mas_inclinada(lista_arboles):
    """dada una lista de árboles devuelve la especie que en promedio tiene la mayor inclinación y el promedio calculado."""
    lista_especies = especies(lista_arboles)
    result = {}
    for e in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, e)
        result[e] = int(sum(inclinaciones) / len(inclinaciones))
    result = list(zip(result.values(), result.keys()))
    result = max(result)
    return result


# parque = "ANDES, LOS"
# lista_arboles = leer_parque(nombre_archivo, parque)
# max_inclinacion = especie_promedio_mas_inclinada(lista_arboles)
# print(
#     f"\nEn el parque {parque} el especimen con mayor promedio de inclinación es un {max_inclinacion[1]} con una inclinación promedio de {max_inclinacion[0]}º.\n"
# )


# ¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado de toda la ciudad y
# no solo de un parque? ¿Podrías dar la latitud y longitud de ese ejemplar? ¿Y dónde se encuentra
# (lat,lon) el ejemplar más alto? ¿De qué especie es?

# ---->>> Respuesta: dentro de la funcion leer_parque() hice que el parametro 'parque' sea optativo, luego en el
# ciclo for pregunto por la variable para agregar todas las filas a la lista o solo las que correspondan
# al parque argumentado.
# Por otro lado, una vez obtenido el especimen con mayor inclinación, lo busco en la lista general y traigo todos los datos

lista_arboles = leer_parque(nombre_archivo)  # <---no espec
max_inclinacion = especie_promedio_mas_inclinada(lista_arboles)
ejemplar = ""
for arbol in lista_arboles:
    if arbol["nombre_com"] == max_inclinacion[1] and arbol["inclinacio"] == str(
        max_inclinacion[0]
    ):
        ejemplar = arbol

print(ejemplar, type(ejemplar))
print("-" * 95)
print("\nEspecímen de arbolado con mayor inclinación en todo CABA:\n")
print("-" * 95)
for k, v in ejemplar.items():
    print(f"{k:<15s} {v:<15s}")
print("-" * 95)
