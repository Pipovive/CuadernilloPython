# Triángulo de Pascal - Primeras 10 filas

filas = 10  # número de filas a generar
triangulo = []  # lista principal que contendrá todas las filas

for i in range(filas):
    fila = [1] * (i + 1)  # cada fila empieza y termina en 1
    
    # Calcula los valores intermedios (si los hay)
    for j in range(1, i):
        fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
    
    triangulo.append(fila)

# Mostrar el triángulo
for fila in triangulo:
    print(fila)
