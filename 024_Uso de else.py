
# -------------------------------------------------
# Uso de else en bucles
# -------------------------------------------------

# Bucle while con else: permite 3 intentos para ingresar una clave correcta
intentos = 3
while intentos > 0:
    clave = input("Ingresa la clave secreta: ")
    if clave == "Victor":  # Si la clave es correcta, termina el bucle
        print("Acceso concedido.")
        break
    intentos -= 1  # Reduce el número de intentos disponibles
else:
    print("Acceso denegado. Se agotaron los intentos.\n")  # Se ejecuta si no se ingresó la clave correcta

# Bucle for con else: busca el número 5 en una lista
print("Buscando el número 5 en la lista...")
lista = [1, 2, 3, 4, 6, 7, 8]
for num in lista:
    if num == 5:  # Si el número 5 se encuentra, termina el bucle
        print("Número 5 encontrado.")
        break
else:
    print("Número 5 no encontrado en la lista.")  # Se ejecuta si el bucle termina sin encontrar el número 5
