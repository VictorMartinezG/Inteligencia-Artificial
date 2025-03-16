# Programa para demostrar la asignación, copias y operaciones con listas

# 1. Asignación de listas (referencia en memoria)
vehicles_one = ['coche', 'bicicleta', 'motor']
vehicles_two = vehicles_one  # Ambas variables apuntan a la misma lista

print("\nLista original:")
print(vehicles_one)

# Eliminamos un elemento de la lista original
del vehicles_one[0]
print("\nLista después de eliminar 'coche':")
print("vehicles_one:", vehicles_one)
print("vehicles_two (también cambia):", vehicles_two)

# 2. Copia de listas usando slicing
colors = ['rojo', 'verde', 'naranja']
copy_whole_colors = colors[:]  # Copia completa
copy_part_colors = colors[0:2]  # Copia parcial

print("\nCopia de listas:")
print("Copia completa:", copy_whole_colors)
print("Copia parcial:", copy_part_colors)

# 3. Uso de índices negativos en slicing
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]  # Copia de "C" a "D"
print("\nRebanada con índices negativos:", new_list)

# 4. Slicing con parámetros opcionales
my_list = [1, 2, 3, 4, 5]
print("\nEjemplo de slicing:")
print("Desde índice 2 hasta el final:", my_list[2:])
print("Desde el inicio hasta el índice 2 (sin incluirlo):", my_list[:2])
print("Últimos dos elementos:", my_list[-2:])

# 5. Eliminación de rebanadas
del my_list[0:2]  # Elimina los primeros dos elementos
print("\nLista después de eliminar primeros dos elementos:", my_list)

del my_list[:]  # Vacía la lista completamente
print("Lista vacía:", my_list)

# 6. Verificación de existencia de elementos
my_list = ["A", "B", 1, 2]

print("\nVerificación de elementos en la lista:")
print("¿'A' está en la lista?", "A" in my_list)
print("¿'C' no está en la lista?", "C" not in my_list)
print("¿2 no está en la lista?", 2 not in my_list)
