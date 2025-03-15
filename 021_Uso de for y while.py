

# -------------------------------------------------
# Uso de bucles while y for
# -------------------------------------------------

# Bucle while que cuenta hacia atrás desde 10 hasta 1
contador = 10
while contador > 0:
    print(f"Cuenta regresiva: {contador}")  # Imprime el número actual
    contador -= 1  # Reduce el contador en 1 en cada iteración

    # Mensaje especial cuando el contador llega a 3
    if contador == 3:
        print("Advertencia: quedan pocos números antes de llegar a cero.")

print("Despegue exitoso\n")  # Mensaje final cuando el bucle termina

# Bucle for que recorre una lista y convierte cada nombre a mayúsculas
nombres = ["Ana", "Luis", "Pedro", "Marta"]
for i, nombre in enumerate(nombres):  
    nombres[i] = nombre.upper()  # Convierte el nombre a mayúsculas
    print(f"Nombre {i + 1}: {nombres[i]}")  # Muestra el nombre modificado
    
print("\nRecorrido de la lista finalizado.")  # Mensaje de finalización
