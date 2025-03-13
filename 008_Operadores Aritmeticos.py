
precio_unitario = 50
cantidad = 7
descuento = 10  # Porcentaje de descuento

# Cálculo del total sin descuento
subtotal = precio_unitario * cantidad  

# Aplicamos el descuento
descuento_aplicado = (subtotal * descuento) / 100  

# Total a pagar después del descuento
total = subtotal - descuento_aplicado  

print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${descuento_aplicado}")
print(f"Total a pagar: ${total}")
