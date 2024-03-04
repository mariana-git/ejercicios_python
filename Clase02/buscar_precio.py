# Ejercicio 2.3: Precio de la naranja
# Escribí un código que abra el archivo ../Data/precios.csv, busque el precio de la naranja y lo imprima en pantalla.

with open("./Data/precios.csv", "rt") as f:
    for line in f:
        row = line.split(",")
        if row[0] == "Naranja":
            print("El precio de la naranja es: ", row[1])


# Ejercicio 2.7: Buscar precios
# A partir del ejercicio anterior, escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv
# el precio de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura en el listado de precios,
# debe imprimir un mensaje que lo indique.


def buscar_precio(fruta):
    with open("./Data/precios.csv", "rt") as f:
        for line in f:
            row = line.split(",")
            if row[0] == fruta:
                precio_fruta = f"(f) El precio de {fruta} es: {row[1]} "
                return precio_fruta
        precio_fruta = f"(f){fruta} no figura en el listado de precios."
        return precio_fruta


print(buscar_precio("Frambuesa"))
