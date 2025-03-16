# Definición y uso de funciones en Python

# 1. Uso de la palabra clave return para devolver valores

def multiply(a, b):
    return a * b  # Retorna el producto de a y b

print(multiply(3, 4))  # Salida: 12

# Si no se especifica un valor de retorno, la función devuelve None

def multiply(a, b):
    return  # No devuelve nada explícitamente

print(multiply(3, 4))  # Salida: None


# 2. Asignación del resultado de una función a una variable

def wishes():
    return "¡Feliz Cumpleaños!"  # Retorna una cadena de texto

w = wishes()  # Asigna el valor retornado a la variable w
print(w)  # Salida: ¡Feliz Cumpleaños!

# Diferencias en la salida al invocar la función directamente o imprimir su retorno

# Ejemplo 1: solo se ejecuta el print dentro de la función

def wishes():
    print("Mis deseos")
    return "Feliz Cumpleaños"

wishes()  # Salida: Mis deseos

# Ejemplo 2: se imprimen tanto el mensaje dentro de la función como el valor retornado

def wishes():
    print("Mis deseos")
    return "Feliz Cumpleaños"

print(wishes())  
# Salida: 
# Mis deseos
# Feliz Cumpleaños


# 3. Pasar una lista como argumento a una función

def hi_everybody(my_list):
    for name in my_list:  # Itera sobre los elementos de la lista
        print("Hola,", name)

hi_everybody(["Adán", "Juan", "Lucía"])
# Salida:
# Hola, Adán
# Hola, Juan
# Hola, Lucía


# 4. Devolver una lista como resultado de una función

def create_list(n):
    my_list = []  # Inicializa una lista vacía
    for i in range(n):
        my_list.append(i)  # Agrega valores de 0 a n-1 a la lista
    return my_list  # Retorna la lista generada

print(create_list(5))  # Salida: [0, 1, 2, 3, 4]
