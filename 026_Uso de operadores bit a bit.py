
# -------------------------------------------------
# Uso de operadores bit a bit en Python
# -------------------------------------------------

# Definimos las variables en decimal
x = 15  # Representación binaria: 0000 1111
y = 16  # Representación binaria: 0001 0000

# AND bit a bit: solo los bits que son 1 en ambos números permanecen 1
resultado_and = x & y  # 0000 0000 → 0
print(f"{x} & {y} = {resultado_and} (bin: {bin(resultado_and)})")

# OR bit a bit: si al menos un bit es 1, el resultado es 1
resultado_or = x | y  # 0001 1111 → 31
print(f"{x} | {y} = {resultado_or} (bin: {bin(resultado_or)})")

# NOT bit a bit: invierte todos los bits (complemento a dos en Python)
resultado_not_x = ~x  # -16 (porque en complemento a dos, invierte y suma 1)
print(f"~{x} = {resultado_not_x} (bin: {bin(resultado_not_x)})")

# XOR bit a bit: si los bits son diferentes, el resultado es 1
resultado_xor = x ^ y  # 0001 1111 → 31
print(f"{x} ^ {y} = {resultado_xor} (bin: {bin(resultado_xor)})")

# Desplazamiento a la derecha: y se divide por 2
resultado_shift_right = y >> 1  # 0000 1000 → 8
print(f"{y} >> 1 = {resultado_shift_right} (bin: {bin(resultado_shift_right)})")

# Desplazamiento a la izquierda: y se multiplica por 2^3 (8)
resultado_shift_left = y << 3  # 1000 0000 → 128
print(f"{y} << 3 = {resultado_shift_left} (bin: {bin(resultado_shift_left)})")
