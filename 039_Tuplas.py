# ========================================
# 1. INTRODUCCIÓN A LAS TUPLAS
# ========================================

# Una tupla es una colección ordenada e inmutable de elementos.
# Se definen usando paréntesis y pueden contener distintos tipos de datos.

my_tuple = (1, 2.5, "Hola", (3, 4), [5, 6], None, True)
print(my_tuple)  # salida: (1, 2.5, 'Hola', (3, 4), [5, 6], None, True)

# Comparación con listas (que sí son mutables)
my_list = [1, 2.5, "Hola", (3, 4), [5, 6], None, True]
print(my_list)

# ========================================
# 2. CREACIÓN DE TUPLAS
# ========================================

# Tupla vacía
empty_tuple = ()
print(type(empty_tuple))  # salida: <class 'tuple'>

# Tupla de un solo elemento (se requiere la coma)
one_elem_tuple_1 = ("elemento",)
one_elem_tuple_2 = "elemento",  # También válido sin paréntesis
print(type(one_elem_tuple_1))  # salida: <class 'tuple'>
print(type(one_elem_tuple_2))  # salida: <class 'tuple'>

# Si se omite la coma, no es una tupla:
not_a_tuple = ("elemento")  
print(type(not_a_tuple))  # salida: <class 'str'>

# ========================================
# 3. ACCESO A ELEMENTOS DE UNA TUPLA
# ========================================

# Se puede acceder a los elementos de una tupla mediante índices
example_tuple = (10, 20.5, "Python", [1, 2], (3, 4))
print(example_tuple[2])  # salida: 'Python'
print(example_tuple[-1])  # salida: (3, 4) (índice negativo)

# ========================================
# 4. INMUTABILIDAD DE LAS TUPLAS
# ========================================

# Las tuplas no permiten modificación de elementos
immutable_tuple = (1, 2, 3, 4)

# Este código generará un error:
# immutable_tuple[1] = 10  # TypeError: 'tuple' object does not support item assignment

# Sin embargo, las listas dentro de una tupla sí pueden modificarse:
mutable_inside_tuple = (1, [2, 3], 4)
mutable_inside_tuple[1][0] = 99
print(mutable_inside_tuple)  # salida: (1, [99, 3], 4)

# ========================================
# 5. ELIMINACIÓN DE UNA TUPLA
# ========================================

# No se pueden eliminar elementos individuales de una tupla,
# pero se puede eliminar la tupla completa con 'del'

temp_tuple = (1, 2, 3)
del temp_tuple
# print(temp_tuple)  # Esto generaría un NameError

# ========================================
# 6. OPERACIONES CON TUPLAS
# ========================================

# Recorrer una tupla con un bucle
loop_tuple = (10, 20, 30)
for elem in loop_tuple:
    print(elem)

# Verificar si un elemento está en la tupla
search_tuple = (1, 2, 3, 4)
print(3 in search_tuple)  # salida: True
print(5 not in search_tuple)  # salida: True

# Obtener la longitud de una tupla
length_tuple = (5, 10, 15, 20)
print(len(length_tuple))  # salida: 4

# Concatenación de tuplas
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)  # salida: (1, 2, 3, 4, 5, 6)

# Repetición de tuplas
repeated_tuple = (7, 8) * 3
print(repeated_tuple)  # salida: (7, 8, 7, 8, 7, 8)

# ========================================
# 7. CONVERSIÓN ENTRE LISTAS Y TUPLAS
# ========================================

# Convertir una lista en una tupla
list_data = [100, 200, 300]
tuple_from_list = tuple(list_data)
print(tuple_from_list)  # salida: (100, 200, 300)

# Convertir una tupla en una lista
tuple_data = (400, 500, 600)
list_from_tuple = list(tuple_data)
print(list_from_tuple)  # salida: [400, 500, 600]

# ========================================
# 8. DESEMPAQUETADO DE TUPLAS
# ========================================

# Se pueden asignar los valores de una tupla a variables individuales
data_tuple = (10, "Python", 3.14)
num, text, pi = data_tuple
print(num)   # salida: 10
print(text)  # salida: 'Python'
print(pi)    # salida: 3.14

# Desempaquetado con valores ignorados
data_tuple_2 = (1, 2, 3, 4, 5)
a, b, *rest = data_tuple_2
print(a)  # salida: 1
print(b)  # salida: 2
print(rest)  # salida: [3, 4, 5]

# ========================================
# 9. USO DE TUPLAS EN RETORNOS DE FUNCIÓN
# ========================================

# Las funciones pueden devolver múltiples valores usando tuplas
def min_max(numbers):
    """Devuelve el mínimo y el máximo de una lista en una tupla."""
    return min(numbers), max(numbers)

values = [5, 8, 2, 10, 3]
result = min_max(values)
print(result)  # salida: (2, 10)

# También se pueden desempaquetar directamente:
min_val, max_val = min_max(values)
print(min_val)  # salida: 2
print(max_val)  # salida: 10