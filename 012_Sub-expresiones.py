

precio_original = 200
descuento_porcentaje = 20

# Aplicamos descuento con paréntesis para controlar la jerarquía
precio_final = precio_original - (precio_original * (descuento_porcentaje / 100))

print(f"Precio con descuento aplicado: ${precio_final}")
# Salida: Precio con descuento aplicado: $160.0
