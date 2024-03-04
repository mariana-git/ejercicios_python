# Ejercicio 1.5: La pelota que rebota

# Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de
# la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las alturas
# que alcanza en cada uno de sus primeros diez rebotes.

altura_alcanzada = 100

for _ in range(10):
    altura_alcanzada = altura_alcanzada * 3 / 5
    print(_, altura_alcanzada)
