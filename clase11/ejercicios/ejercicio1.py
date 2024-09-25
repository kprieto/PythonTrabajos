# Ejercicio 1: Operaciones Matemáticas con el Módulo math 
# • Objetivo: Practicar con las funciones matemáticas básicas del 
# módulo math. 
# • Descripción: Utiliza las funciones del módulo math para realizar 
# operaciones matemáticas avanzadas. 
# • Instrucciones: Solicita al usuario que ingrese un número 
# decimal. 
# Usa las siguientes funciones del módulo math para realizar diferentes 
# cálculos: 
# ✓ math.ceil(): Redondear al entero superior. 
# ✓ math.floor(): Redondear al entero inferior. 
# ✓ math.sqrt(): Obtener la raíz cuadrada. 
# ✓ math.factorial(): Calcular el factorial (solo si es un 
# número entero no negativo). 
# ✓ math.pow(): Elevar el número a la potencia de otro 
# número. 

import math

def peticion_usuario():
    try:
        # Convertir la entrada del usuario a float
        num = float(input("Introduce un número: "))
        return num
    except ValueError:
        print("Por favor, introduce un número válido.")
        return peticion_usuario()

numero_usuario = peticion_usuario()

#Valida para el tipo raiz cuadrada y factorial si el numero es positivo
def validar_numero(num,tipo):
    if num < 0:
        print("El número ingresado debe ser positivo.")
        return validar_numero(peticion_usuario(),tipo)
    elif isinstance(num, float) and tipo == "factorial": 
        return int(num)
    else:
        return num

#Redondear un numero entero hacia arriba
numero_ceil = math.ceil(numero_usuario)
print(f"Número entero {numero_usuario} redondeado hacia arriba es: {numero_ceil}")

#Redondear un numero entero hacia abajo
numero_floor = math.floor(numero_usuario)
print(f"Número entero {numero_usuario} redondeado hacia abajo es: {numero_floor}")

# Obtener la raiz cuadrada de un numero
numero_raiz_cuadrada = validar_numero(numero_usuario,"raiz")
raiz_cuadrada = math.sqrt(numero_raiz_cuadrada)

print(f"La raiz cuadrada {numero_raiz_cuadrada} es: {raiz_cuadrada}")

# Calcular el factorial de un numero
numero_floor = validar_numero(numero_floor,"factorial")
print(f"El factorial del numero {numero_floor} es: {math.factorial(numero_floor)}")

# Elevar un numero a la pontencia de otro numero
potencia = math.pow(numero_usuario,4)
print(f"La potencia del numero {numero_usuario} es: {potencia}")


