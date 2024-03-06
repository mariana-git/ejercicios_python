numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

numeros_format = "%4d " * 10

print(f"{'':>2s} {numeros_format % numeros}")

print("-" * 55)

for n in numeros:

    fila = []

    for i in range(len(numeros)):

        fila.append(i * n)

    fila = tuple(fila)
    print(f"{n}: {numeros_format % fila}")
