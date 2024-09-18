# Ejercicio 2: Verificación de Elementos en una Tupla
# Crea una tupla llamada mi_tupla con los siguientes elementos: (3, 6, 9, 12, 15).
# Verifica si el número 6 está en la tupla y muestra un mensaje indicando si está presente o no
# Verifica si el número 7 está en la tupla y muestra un mensaje indicando si está presente o no.

mi_tupla = (3, 6, 9, 12, 15)

numero_a_verificar = 7

if numero_a_verificar in mi_tupla:
    print(f"El número {numero_a_verificar} se encuentra en la tupla.")
else:
    print(f"El número {numero_a_verificar} no se encuentra en la tupla.")
