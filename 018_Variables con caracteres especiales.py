
# Generación de nombres de usuario dinámicamente
_nombre = "Luis"
apellido = "Martínez"
edad = 27

# Creación de un identificador único basado en datos personales
usuario_id = f"{_nombre.lower()}{apellido[:3].lower()}{edad}"

# Verificación del formato
print(f"Usuario generado: {usuario_id}")

# Intento de usar una variable no válida (esto generaría un error)
# 1usuario = "Error"  # Esto no es permitido
