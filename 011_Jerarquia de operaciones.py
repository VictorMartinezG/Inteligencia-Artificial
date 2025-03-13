# Sin paréntesis, la multiplicación tiene prioridad sobre la suma
resultado1 = 5 + 3 * 2  # 3 * 2 se calcula primero, luego se suma 5

# Con paréntesis, se altera la jerarquía de operaciones
resultado2 = (5 + 3) * 2  # Se suma primero y luego se multiplica

print(f"Sin paréntesis: {resultado1}")  # 11
print(f"Con paréntesis: {resultado2}")  # 16
