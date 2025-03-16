
# ==========================
# Comprensión de listas con condición
# ==========================

# Generar una lista con los primeros 10 números elevados al cuadrado si son pares
squared_evens = [num ** 2 for num in range(10) if num % 2 == 0]

# Imprimir la lista generada
print("Cuadrados de números pares:", squared_evens)


# ==========================
# Matriz 4x4 con valores alternos
# ==========================

# Crear una matriz 4x4 con 'X' y 'O' alternados
table = [["X" if (row + col) % 2 == 0 else "O" for col in range(4)] for row in range(4)]

# Recorrer la matriz e imprimir cada fila
for row in table:
    print(" | ".join(row))  # Se unen los elementos con " | " para mejor visualización


import random  # Se importa la librería para generar números aleatorios

# ==========================
# Generación de un cubo tridimensional (3x3x3)
# ==========================

# Crear un cubo 3x3x3 con valores aleatorios entre 1 y 9
cube = [[[random.randint(1, 9) for _ in range(3)] for _ in range(3)] for _ in range(3)]

# Recorrer cada capa del cubo y mostrarla en la consola
for layer_index, layer in enumerate(cube):  # Se itera sobre cada capa
    print(f"Capa {layer_index + 1}:")  # Se imprime el número de la capa
    for row in layer:
        print("  ", row)  # Se imprimen las filas de la capa con indentación
    print()  # Se deja un espacio entre capas
