# Ejercicio 8: Usar raise 
# Crea un programa que solicite el ingreso de un número entre 1 y 10. Si el 
# número no está en ese rango, genera una excepción con raise. 

def verificar_numero(numero):
    if numero < 1 or numero > 10:
        raise ValueError("El número ingresado debe estar en el rango del 1 al 10.")
    print(f"El número {numero} ingresado esta entre el rango del 1 al 10.")

numero = int(input("Ingresa un numero entre 1 y 10: "))
verificar_numero(numero)