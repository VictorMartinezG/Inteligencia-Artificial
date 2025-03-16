

# TEMA: Alcance de Variables en Funciones

# ===========================
# 1. Alcance de una variable global dentro de una función
# ===========================

# Definimos una variable global
var = 10  

def mult_by_var(x):
    """Multiplica el número x por la variable global var."""
    return x * var  

# Llamamos a la función con un valor de prueba
print(mult_by_var(5))  # salida: 50

# ===========================
# 2. Alcance de una variable local dentro de una función
# ===========================

def mult(x):
    """Multiplica x por una variable local dentro de la función."""
    var = 6  # Variable local, solo existe dentro de la función
    return x * var  

print(mult(5))  # salida: 30

# ===========================
# 3. Cuando una variable global y una local tienen el mismo nombre
# ===========================

var = 4  # Variable global

def mult(x):
    """Multiplica x por una variable local, ignorando la variable global."""
    var = 8  # Variable local, oculta la global dentro de la función
    return x * var  

print(mult(5))  # salida: 40
print(var)  # salida: 4 (la variable global no cambia)

# ===========================
# 4. Alcance de una variable dentro de una función
# ===========================

def adding(x):
    """Suma x con una variable local dentro de la función."""
    var = 3  
    return x + var  

print(adding(7))  # salida: 10

# La siguiente línea generaría un error porque var es una variable local
# print(var)  # NameError: name 'var' is not defined

# ===========================
# 5. Uso de la palabra clave global
# ===========================

var = 15  # Variable global

def modify_global():
    """Modifica la variable global var usando 'global'."""
    global var  
    var = 20  # Modifica la variable global
    return var  

print(var)  # salida: 15 (valor antes de modificar)
print(modify_global())  # salida: 20 (modificada dentro de la función)
print(var)  # salida: 20 (la variable global se ha actualizado)

# ===========================
# 6. Uso de variables globales y locales combinadas
# ===========================

count = 0  # Variable global

def counter():
    """Incrementa la variable global count."""
    global count  
    count += 1  # Modifica la variable global
    return count  

print(counter())  # salida: 1
print(counter())  # salida: 2
print(counter())  # salida: 3
