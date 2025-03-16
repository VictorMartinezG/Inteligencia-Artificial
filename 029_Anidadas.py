
# -------------------------------------------------
# Creación de una lista dentro de otra lista
# -------------------------------------------------
my_list = [1, 'a', ["lista", 64, [0, 1], False]]

# Accediendo al primer elemento de la sublista
print(my_list[2][0])  # Output: lista

# Accediendo al segundo elemento de la sublista anidada
print(my_list[2][2][1])  # Output: 1
