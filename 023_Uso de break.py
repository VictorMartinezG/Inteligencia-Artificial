


# -------------------------------------------------
# Uso de break y continue
# -------------------------------------------------

# Bucle for que busca un número negativo en una lista y detiene el bucle
numeros = [4, 8, 3, -1, 7, 2]
for num in numeros:
    if num < 0:  # Si el número es negativo, termina el bucle con break
        print(f"Número negativo encontrado: {num}. Deteniendo el bucle.")
        break
    print(f"Número positivo: {num}")  # Se imprimen los números positivos

print("\n")

# Bucle for que imprime solo los números pares del 1 al 10
print("Lista de números pares:")
for num in range(1, 11):  
    if num % 2 != 0:  # Si el número es impar, usa continue para saltarlo
        continue
    print(num, end=" ")  # Solo se imprimen los números pares
