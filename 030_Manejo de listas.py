
# -------------------------------------------------
# Eliminando elementos de una lista
# -------------------------------------------------
my_list = [1, 2, 3, 4]

# Eliminando el tercer elemento (índice 2)
del my_list[2]
print(my_list)  # Output: [1, 2, 4]

# Eliminando la lista por completo
del my_list

# Intentar acceder a la lista después de eliminarla causará un error
# print(my_list)  # Esto generaría un NameError


# -------------------------------------------------
# Recorriendo una lista con un bucle for
# -------------------------------------------------
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]

# Imprimiendo cada elemento de la lista
for color in my_list:
    print(color)


# -------------------------------------------------
# Uso de len() para conocer la cantidad de elementos de una lista
# -------------------------------------------------
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]

# Obtener la cantidad de elementos en la lista
print(len(my_list))  # Output: 5

# Eliminar un elemento de la lista
del my_list[2]

# Obtener la nueva cantidad de elementos
print(len(my_list))  # Output: 4


# -------------------------------------------------
# Diferencia entre función y método en listas
# -------------------------------------------------

# Definiendo una lista
my_list = [3, 1, 4, 1, 5, 9]

# Función: se llama de forma independiente
longitud = len(my_list)  # Función que obtiene la longitud de la lista
print("Longitud de la lista:", longitud)

# Método: se llama sobre un objeto (en este caso, la lista)
my_list.sort()  # Método que ordena la lista en su lugar
print("Lista ordenada:", my_list)
