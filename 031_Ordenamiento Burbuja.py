
# Programa para ordenar e invertir una lista ingresada por el usuario

# Solicitar al usuario que ingrese números separados por espacios
numeros = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada en una lista de enteros
lst = [int(num) for num in numeros.split()]

print("\nLista original:")
print(lst)

# Ordenar la lista de menor a mayor
lst.sort()
print("\nLista ordenada de menor a mayor:")
print(lst)

# Invertir la lista (mayor a menor)
lst.reverse()
print("\nLista ordenada de mayor a menor:")
print(lst)
