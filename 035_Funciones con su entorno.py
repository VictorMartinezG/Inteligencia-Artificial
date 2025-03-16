# ==========================
# 1. Uso de parámetros en funciones
# ==========================

def hi(name):
    print("Hola,", name)

hi("Greg")

# ==========================
# 2. Función con dos parámetros
# ==========================

def hi_all(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)

hi_all("Sebastián", "Konrad")

# ==========================
# 3. Función con tres parámetros
# ==========================

def address(street, city, postal_code):
    print("Tu dirección es:", street, "St.,", city, postal_code)

s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")

address(s, c, p_c)

# ==========================
# 4. Argumentos posicionales
# ==========================

def subtra(a, b):
    print(a - b)

subtra(5, 2)
subtra(2, 5)

# ==========================
# 5. Argumentos con palabras clave
# ==========================

def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)
subtra(b=2, a=5)

# ==========================
# 6. Mezcla de argumentos posicionales y palabras clave
# ==========================

def subtra(a, b):
    print(a - b)

subtra(5, b=2)  # Correcto
# subtra(a=5, 2)  # Incorrecto: SyntaxError

# ==========================
# 7. Valores predefinidos en parámetros
# ==========================

def name(first_name, last_name="Pérez"):
    print(first_name, last_name)

name("Andy")  # Usa "Pérez" por defecto
name("Bety", "Rodríguez")  # Reemplaza "Pérez"
