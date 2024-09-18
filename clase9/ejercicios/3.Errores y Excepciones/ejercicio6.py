# Ejercicio 6: Manejo básico de errores con try/except 
# Crea un programa que solicite al usuario que ingrese un número. Si el 
# usuario ingresa algo que no es un número, muestra un mensaje de error 
# usando try/except. 

try:
    numero = float(input("Introduce un número: "))
    print(f"El número {numero} que ingresaste es válido.")
except ValueError:
    print("Error: Información no válida. Introduce un número.")