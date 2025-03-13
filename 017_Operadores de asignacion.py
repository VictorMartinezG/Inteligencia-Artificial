
# Simulación de una cuenta bancaria con transacciones dinámicas

saldo = 5000.0  # Saldo inicial
print(f"Saldo inicial: ${saldo}")

# Depósito de nómina
deposito = 2500
saldo += deposito
print(f"Depósito de nómina (+${deposito}): ${saldo}")

# Pago de renta
renta = 1800
saldo -= renta
print(f"Pago de renta (-${renta}): ${saldo}")

# Compra con tarjeta de crédito (pagos a meses con interés)
compra = 3200
interes = 1.03  # 3% de interés
saldo -= compra * interes
print(f"Compra a crédito (-${compra} con {int((interes-1)*100)}% de interés): ${saldo:.2f}")

# Inversión con tasa de retorno
rendimiento = 1.05  # 5% de retorno
saldo *= rendimiento
print(f"Inversión (+5%): ${saldo:.2f}")
