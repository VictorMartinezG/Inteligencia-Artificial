

# -------------------------------------------------
# Práctica: Uso de operadores de comparación y sentencias condicionales
# -------------------------------------------------

# Definir variables
edad = int(input("Ingresa tu edad: "))  # Convertimos la entrada a número entero
ingresos = float(input("Ingresa tus ingresos mensuales en USD: "))  # Convertimos a float

# Evaluar si la persona es mayor de edad y tiene ingresos suficientes
if edad >= 18:  # Condición para ser mayor de edad
    print("Eres mayor de edad.")
    
    # Condición anidada: Evaluar ingresos
    if ingresos >= 1000:
        print("Tienes ingresos suficientes para aplicar a una tarjeta de crédito.")
    else:
        print("Tus ingresos no alcanzan el mínimo para aplicar a una tarjeta de crédito.")
    
else:
    print("Eres menor de edad, no puedes solicitar una tarjeta de crédito.")

# Uso de if-elif-else para clasificar a la persona según su edad
if edad < 12:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")

# Comparación con múltiples operadores
if 18 <= edad <= 30 and ingresos > 1500:
    print("Puedes acceder a beneficios para jóvenes emprendedores.")
elif 31 <= edad <= 50 and ingresos > 2000:
    print("Puedes acceder a planes de inversión para adultos.")
else:
    print("Consulta otras opciones según tu perfil.")

# Fin del programa
print("\nPrograma finalizado.")
