# Ejercicio 2: Generador de Números Aleatorios con el Módulo 
# random 
# • Objetivo: Trabajar con funciones de generación de números 
# aleatorios del módulo random. 
# • Descripción: Simula el lanzamiento de un dado y genera una 
# lista de números aleatorios. 
# • Instrucciones: 
# ✓ Simula el lanzamiento de un dado de 6 caras (números 
# del 1 al 6) cinco veces. 
# ✓ Genera una lista de 10 números aleatorios entre 1 y 100. 
# ✓ Selecciona aleatoriamente un número de la lista 
# generada. 

import random

#Simulación de lanzamiento de un dado
for lanzamiento in range(1,6):
    print(f"--- {lanzamiento} LANZAMIENTO DEL DADO ---")
    print(f"Cara : {random.randint(1,6)}")
print()

#Generar una lista de 10 números aleatorios entre 1 y 100
lista_numeros_aleatorios = []

for num in range(10):
    lista_numeros_aleatorios.append(random.randint(1,100))
print(f"Lista de números aleatorios entre 1 y 100 es: {lista_numeros_aleatorios}")
print()

#Generar un número aleatorio de la lista anterior
numero_elegido = random.choice(lista_numeros_aleatorios)
print(f"Número eligido: {numero_elegido}")
