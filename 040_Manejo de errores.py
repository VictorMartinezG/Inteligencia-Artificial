
# Ejemplo 1: Error de sintaxis (comentado para evitar que detenga la ejecución)
# print("Hola, ¡Mundo!)  # Falta una comilla al final, generará un SyntaxError

# Ejemplo 2: Excepción por división entre cero
try:
    print(1/0)  # Genera una excepción ZeroDivisionError
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

# Ejemplo 3: Manejo de excepciones con entrada de usuario
while True:
    try:
        number = int(input("Ingresa un número entero: "))  # Intenta convertir la entrada en un entero
        print(number/2)  # Divide el número ingresado entre 2
        break  # Sale del bucle si la entrada es válida
    except ValueError:  # Captura el error si el usuario no ingresa un número entero
        print("Advertencia: el valor ingresado no es válido. Intenta de nuevo...")

# Ejemplo 4: Manejo de múltiples excepciones específicas
while True:
    try:
        number = int(input("Ingresa un número entero: "))  # Pide un número entero
        print(5/number)  # Intenta dividir 5 entre el número ingresado
        break  # Sale del bucle si no hay error
    except ValueError:  # Captura error si se ingresa un dato no numérico
        print("Valor incorrecto.")
    except ZeroDivisionError:  # Captura error si se intenta dividir entre cero
        print("Lo siento. No puedo dividir entre cero.")
    except Exception as e:  # Captura cualquier otro error inesperado
        print(f"Error inesperado: {e}")

# Ejemplo 5: Manejo de múltiples excepciones en un solo bloque
while True:
    try:
        number = int(input("Ingresa un número entero: "))  # Pide un número entero
        print(5/number)  # Intenta dividir 5 entre el número ingresado
        break  # Sale del bucle si no hay error
    except (ValueError, ZeroDivisionError):  # Captura errores de valor o división por cero
        print("Valor incorrecto o se ha roto la regla de división entre cero.")
    except Exception as e:  # Captura cualquier otro error inesperado
        print(f"Error inesperado: {e}")

# Ejemplo 6: Captura de KeyboardInterrupt
try:
    input("Presiona Ctrl+C o Ctrl+D para interrumpir: ")  # Espera una entrada del usuario
except KeyboardInterrupt:  # Captura la interrupción del usuario (Ctrl+C)
    print("\nInterrupción detectada. Saliendo del programa...")
