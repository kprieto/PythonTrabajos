# 7. Ejercicio Combinado 
# Desarrolla un programa que: 
# 1. Genere una lista de números aleatorios entre 1 y 20. 
# 2. Usa un bucle for con range para iterar sobre la lista. 
# 3. Usar continue para saltar números menores de 10. 
# 4. Usar break para detener la iteración si se encuentra un número 
# divisible por 15. 
# 5. Imprimir todos los números que cumplen las condiciones. 
# 6. Utilizar list comprehension para filtrar los números que no cumplen 
# ninguna condición. 
import random

numeros = [random.randint(1, 20) for _ in range(20)]
numeros_que_cumplen = []
for i in range(len(numeros)):
    
    if numeros[i] < 10:
        continue
    if numeros[i] % 15 == 0:
        break
    numeros_que_cumplen.append(numeros[i])

filtrar_numeros_no_cumplen = [x  for x in numeros if x < 10 or x % 15 == 0]

print(f"La lista de números aleatorios entre 1 al 20 es: {numeros}")
print(f"Los números que si cumplen con las condiciones son: {numeros_que_cumplen}")
print(f"Los números que no cumple con las condicciones son: {filtrar_numeros_no_cumplen}")