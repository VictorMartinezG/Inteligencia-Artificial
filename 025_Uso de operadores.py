# -------------------------------------------------
# Uso de operadores lógicos en Python
# -------------------------------------------------

# Definimos variables booleanas
a = True
b = False

# Operador AND: devuelve True solo si ambos valores son True
resultado_and = a and b  # False porque b es False
print(f"{a} and {b} → {resultado_and}")

# Operador OR: devuelve True si al menos un valor es True
resultado_or = a or b  # True porque a es True
print(f"{a} or {b} → {resultado_or}")

# Operador NOT: invierte el valor booleano
resultado_not_a = not a  # False porque a es True
resultado_not_b = not b  # True porque b es False
print(f"not {a} → {resultado_not_a}")
print(f"not {b} → {resultado_not_b}")

# Uso en una condición práctica
edad = 20
tiene_identificacion = False

if edad >= 18 and tiene_identificacion:
    print("Puedes entrar al club.")
else:
    print("No puedes entrar al club. Verifica si tienes identificación.")
