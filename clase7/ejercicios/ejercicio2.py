# 2. Ejercicio Integrador 
# Desarrolla un programa que haga lo siguiente: 
# 1. Usar un bucle for con range para iterar sobre los números del 1 al 
# 20. 
# 2. Usar continue para saltar los números divisibles por 3. 
# 3. Usar break para detener la iteración si se encuentra un número 
# mayor que 15. 
# 4. Crear un set con los números restantes y verificar si algún número 
# es par. 

set_numeros_restantes = set()
lista_numeros = [num for num in range(1,21)]
for num in lista_numeros:
    
    if num % 3 == 0:
        continue
    
    if num > 15:
        break
    
    set_numeros_restantes.add(num)
    
pares = any(numero % 2 == 0 for numero in set_numeros_restantes)
verificar_si_hay_par = 'Si' if pares else 'No'

print(f"Lista de números del 1 al 20: {lista_numeros}")
print(f"Lista de números restantes: {set_numeros_restantes}")
print(f"¿Existe algún número par? {verificar_si_hay_par}")