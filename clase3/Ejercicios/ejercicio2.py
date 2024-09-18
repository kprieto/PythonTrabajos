# Ejercicio 2: Contador de Números Específicos
# Escribe un programa que cuente cuántas veces aparece un número específico en una lista.
# Instrucciones:

# Define una lista de números predefinida o pídele al usuario que ingrese los números.

# Pide al usuario que ingrese un número a buscar.

# Usa el método count() para determinar cuántas veces aparece el número en la lista.

# Muestra el resultado.

mi_lista = [1,2,3,4,2,5,2,6,2,6,8,4]

numero = int(input("Ingrese el número a buscar:"))

num_repetido = mi_lista.count(numero)

print(f"El número {numero} aparece {num_repetido} veces en la lista.")