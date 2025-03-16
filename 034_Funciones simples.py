
# ==========================
# Definición y uso de funciones
# ==========================

# Definición de una función sin parámetros
def message():
    print("Hola, esta es una función simple.")

# Llamado de la función
message()


# ==========================
# Función con un parámetro
# ==========================

# Definición de una función que recibe un nombre como parámetro
def hello(name):
    print("Hola,", name)

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")

# Llamar a la función con el valor ingresado
hello(nombre)


# ==========================
# Función con múltiples parámetros
# ==========================

# Definir una función que suma dos números
def sumar(a, b):
    resultado = a + b
    return resultado  # Se devuelve el resultado

# Llamado de la función con valores específicos
suma = sumar(5, 3)

# Imprimir el resultado
print("La suma es:", suma)


# ==========================
# Función con valores por defecto
# ==========================

# Función que imprime un saludo con un nombre y mensaje opcional
def saludo(nombre, mensaje="¡Bienvenido!"):
    print(nombre + ", " + mensaje)

# Llamado de la función con y sin argumento opcional
saludo("Ana")  # Usa el mensaje por defecto
saludo("Carlos", "¡Qué bueno verte!")  # Mensaje personalizado


# ==========================
# Función que retorna múltiples valores
# ==========================

# Función que devuelve el doble y el triple de un número
def operaciones(num):
    doble = num * 2
    triple = num * 3
    return doble, triple  # Retorna dos valores

# Llamar a la función y recibir los valores
doble_val, triple_val = operaciones(4)

# Imprimir los valores obtenidos
print("Doble:", doble_val)
print("Triple:", triple_val)
