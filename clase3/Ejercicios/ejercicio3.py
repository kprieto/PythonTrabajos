# Ejercicio 3: Suma de Sublistas
# Crea un programa que tome una lista de números y calcule la suma de una sublista especificada por el usuario.
# Instrucciones:

# Define una lista de números predefinida.

# Pide al usuario que ingrese el índice de inicio y el índice de fin para la sublista.

# Usa slicing para obtener la sublista.

# Suma los elementos de la sublista.

# Muestra la suma.

mi_lista = [10,20,30,40,50,60,70,80]
suma = 0
indice_inicio = int(input("Ingrese el índice de inicio de la sublista: "))
indice_fin = int(input("Ingrese el índice de fin de la sublista: "))

sublista = mi_lista[indice_inicio:indice_fin]
suma = sum(sublista)

print(f"La suma de la sublista {sublista} es: ", suma)