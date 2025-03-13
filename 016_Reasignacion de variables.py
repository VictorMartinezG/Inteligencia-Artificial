

# Cálculo de impuestos con distintas tasas según el producto

precio_base = 1000
print(f"Precio base: ${precio_base}")

# Reasignamos según la categoría del producto
categoria = "Electrónico"

if categoria == "Alimento":
    impuesto = 0.08  # 8% de IVA
elif categoria == "Electrónico":
    impuesto = 0.16  # 16% de IVA
elif categoria == "Ropa":
    impuesto = 0.12  # 12% de IVA
else:
    impuesto = 0.10  # Tarifa estándar

precio_final = precio_base * (1 + impuesto)
print(f"Precio con impuestos ({impuesto*100}%): ${precio_final:.2f}")
