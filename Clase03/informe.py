# Supongamos que los precios en camion.csv son los precios pagados al productor de frutas
# mientras que los precios en precios.csv son los precios de venta en el lugar de descarga
#  del camión. Ahora vamos calcular el balance del negocio: juntá todo el trabajo que
# hiciste recién en tu programa informe.py (usando las funciones leer_camion() y leer_precios())
# y completá el programa para que con los precios del camión (Ejercicio 3.2) y los de
# venta en el negocio (Ejercicio 3.3) calcule lo que costó el camión, lo que se recaudó con
# la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla
# un balance con estos datos. Ayuda: hubo una ganancia de algo más de quince mil pesos.


from leer_camion import *
from leer_precios import *


def balance(archivo_camion, archivo_precios):
    costo = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    costo_camion = 0
    recaudacion_camion = 0

    for producto, cajones, precio in costo:
        costo_camion += precio * cajones
        recaudacion_camion += precios[producto] * cajones

    diferencia = round(recaudacion_camion - costo_camion, 2)
    resultado = "GANANCIA" if diferencia > 0 else "PÉRDIDA"

    data = {
        "costo": costo_camion,
        "recaudacion": recaudacion_camion,
        "diferencia": diferencia,
        "resultado": resultado,
    }
    return data


data = balance("./Data/camion.csv", "./Data/precios.csv")

print(
    f"\n Costo del camión: {data['costo']} \n Recaudación: {data['recaudacion']} \n a diferencia fue de: {data['diferencia']} \n \n El balance dió {data['resultado']}. \n"
)
