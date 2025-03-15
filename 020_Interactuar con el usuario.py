

# -------------------------------------------------
# Práctica: Uso de print() e input()
# -------------------------------------------------

# 1. Solicitar datos al usuario con input()
nombre = input("Ingresa tu nombre: ")  # El usuario ingresa su nombre
edad = input("Ingresa tu edad: ")  # El usuario ingresa su edad

# 2. Mostrar los datos con print()
print("\nHola, " + nombre + ". ¡Un gusto conocerte!")  # Concatenación
print("Tienes " + edad + " años.")  # Concatenación con datos ingresados

# 3. Convertir la edad a entero y hacer una operación
edad_futura = int(edad) + 5  # Convertimos edad a número y sumamos 5
print(f"En 5 años tendrás {edad_futura} años.")  # Usamos f-string para formateo

# 4. Replicación de cadenas
print("\nTu nombre repetido 3 veces:")
print(nombre * 3)  # Multiplicación de cadena

# 5. Detener el programa hasta que el usuario presione Enter
print("\nPresiona Enter para terminar el programa.")
input()  # Espera una entrada vacía
print("FIN.")  # Indica el final del programa
