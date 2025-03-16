
# -------------------------------------------------
# Accediendo a elementos de una lista usando índices
# -------------------------------------------------
my_list = [1, None, True, "Soy una cadena", 256, 0]

# Acceder a un elemento usando su índice positivo
print(my_list[3])  # Output: Soy una cadena

# Acceder al último elemento usando índice negativo
print(my_list[-1])  # Output: 0

# Modificar un elemento de la lista
my_list[1] = '?'
print(my_list)  # Output: [1, '?', True, 'Soy una cadena', 256, 0]

# Insertar un elemento en la primera posición
my_list.insert(0, "primero")

# Agregar un elemento al final de la lista
my_list.append("último")

# Mostrar la lista actualizada
print(my_list)  # Output: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']
