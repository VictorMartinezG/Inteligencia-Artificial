
# TEMA: Funciones Recursivas en Python

# ========================================
# 1. Definición de Recursividad
# ========================================

# Una función recursiva es aquella que se llama a sí misma.
# Debe incluir una condición de terminación para evitar un bucle infinito.

# ========================================
# 2. Implementación de Factorial con Recursividad
# ========================================

def factorial(n):
    """Calcula el factorial de un número utilizando recursividad."""
    if n == 1:  # Condición de terminación
        return 1
    else:
        return n * factorial(n - 1)

# Probamos la función con un número
print(factorial(5))  # salida: 120 (5 * 4 * 3 * 2 * 1)


# ========================================
# 3. Función Recursiva para la Serie de Fibonacci
# ========================================

def fibonacci(n):
    """Calcula el término n de la serie de Fibonacci utilizando recursividad."""
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamadas recursivas

# Probamos la función con varios valores
print(fibonacci(6))  # salida: 8 (0, 1, 1, 2, 3, 5, 8)


# ========================================
# 4. Función Recursiva para Calcular la Suma de una Lista
# ========================================

def sum_list(lst):
    """Suma los elementos de una lista utilizando recursividad."""
    if not lst:  # Caso base: lista vacía
        return 0
    else:
        return lst[0] + sum_list(lst[1:])  # Suma el primer elemento y llama a la función con el resto

# Probamos la función con una lista de números
numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))  # salida: 15 (1+2+3+4+5)


# ========================================
# 5. Función Recursiva para Invertir una Cadena
# ========================================

def reverse_string(s):
    """Invierte una cadena de texto usando recursividad."""
    if len(s) == 0:  # Caso base: cadena vacía
        return s
    else:
        return s[-1] + reverse_string(s[:-1])  # Última letra + recursión del resto de la cadena

# Probamos la función con una palabra
print(reverse_string("Victor"))  # salida: "nohtyP"