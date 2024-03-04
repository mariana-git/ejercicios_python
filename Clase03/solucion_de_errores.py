# En los siguientes ejercicios te proponemos que uses las técnicas que mencionamos arriba para 
# resolver los problemas que aparecen a continuación. Determiná los errores de los siguientes 
# códigos y corregilos en un archivo solucion_de_errores.py comentando brevemente los errores. 
# ¿Qué tipo de errores tiene cada uno?
# En el archivo solucion_de_errores.py separá las correcciones de los distintos códigos con una
#  línea que contenga solamente los símbolos #%% seguido de una o varias líneas comentadas 
# indicando el ejercicio y el problema que tenía. Al terminar, debería verse así tu archivo:

# Ejercicio 3.5: Semántica

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

# Respuesta: tendria que pasarlo a lower() para comparar

#%%

# Ejercicio 3.6: Sintaxis

def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i < n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

# Respuesta: le falta los dos puntos al finalizar la declaración de la funcion, 
# y en lugar de retornar "Falso" debe retornar False

#%%

# Ejercicio 3.7: Tipos

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

# Respuesta: ese while nunca se ejecuta, porque tiene siempre es False al arrancar

#%%

# Ejercicio 3.8: Alcances

def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# Respuesta: la variable c esta solo dentro del ambito de la funcion

#%%

# Ejercicio 3.9: Pisando memoria
# El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, 
# ¿podés determinar por qué y explicarlo brevemente en la versión corregida?

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)


# Respuesta: el problema es que todos los elementos de la lista camion apuntan 
# al mismo registro, que va cambiando su valor en cada iteracion, pero al final 
# del bucle todos los elementos de la lista aputnan al mismo registro, ende tienen
#  el ultimo valor que este adopto

