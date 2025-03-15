# -------------------------------------------------
# Ejemplo: Uso de comentarios en Python
# -------------------------------------------------

# 1. Comentarios de una sola línea:
# Se usan para explicar partes específicas del código.

nombre = "Carlos"  # Almacenamos el nombre del usuario
edad = 25  # Edad del usuario en años

# 2. Comentarios para desactivar código temporalmente:
# print("Este mensaje no se mostrará")  # Línea desactivada

# 3. Comentarios en bloques:
# Se usan para explicar secciones completas del código.

"""
Este bloque de código calcula el año de nacimiento del usuario
restando su edad al año actual.
"""

anio_actual = 2025  # Año en curso
anio_nacimiento = anio_actual - edad  # Cálculo del año de nacimiento

print(f"{nombre} nació en el año {anio_nacimiento}.")

# 4. Comentarios en funciones usando docstrings:
def suma(a, b):
    """
    Esta función recibe dos números y retorna su suma.
    
    Parámetros:
    a (int o float) - Primer número
    b (int o float) - Segundo número
    
    Retorna:
    int o float - Resultado de la suma
    """
    return a + b

# Llamando a la función
resultado = suma(10, 5)
print(f"La suma es: {resultado}")
