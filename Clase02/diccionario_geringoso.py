# Ejercicio 2.13: Diccionario geringoso.
# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso.
# Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus
# traducciones al geringoso (como en el Ejercicio 1.18).


vocales = ("a", "e", "i", "o", "u")


def geringoso(lista):
    dic_geringoso = {}
    for item in lista:
        papalapabrapa = ""
        for c in item:
            if c in vocales:
                c = c + "p" + c
            papalapabrapa += c
        dic_geringoso[item] = papalapabrapa
    return dic_geringoso


lista = ["banana", "manzana", "mandarina"]
print(geringoso(lista))
