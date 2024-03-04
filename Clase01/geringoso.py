# Ejercicio 1.18: Geringoso rústico
# Usá una iteración sobre el string cadena para agregar la sílaba
# 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.


vocales = ("a", "e", "i", "o", "u")


def geringoso(palabra):
    papalapabrapa = ""
    for c in palabra:
        if c in vocales:
            c = c + "p" + c
        papalapabrapa += c
    return papalapabrapa


print(geringoso("mandarina"))
