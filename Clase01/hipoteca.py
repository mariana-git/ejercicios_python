# Ejercicio 1.11: Hipoteca ajustado
# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%.
# Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.# hipoteca.py
# El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1 + tasa / 12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print("Total pagado", round(total_pagado, 2))  # Total pagado 966279.6


# Ejercicio 1.8: Adelantos
# Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
# Modificá el programa para incorporar estos pagos extra y para que imprima el monto total pagado
#  junto con la cantidad de meses requeridos.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0

while saldo > 0:
    meses += 1
    saldo = saldo * (1 + tasa / 12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if meses <= 12:
        saldo -= 1000
        total_pagado += 1000

print("Total pagado:", round(total_pagado, 2), "Meses requeridos:", meses)
