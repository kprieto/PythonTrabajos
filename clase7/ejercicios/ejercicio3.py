# 3. Ejercicio de Sets y Operaciones Básicas 
# Escribe un programa que: 
# 1. Cree dos sets de números. 
# 2. Realice operaciones de unión, intersección y diferencia entre estos 
# sets. 
# 3. Imprima los resultados de cada operación. 

conjunto_1 = {1,2,3,4}
conjunto_2 = {4,5,6,7}

#Unión
union = conjunto_1 | conjunto_2
print(f"La unión entre conjunto_1 {conjunto_1} y conjunto_2 {conjunto_2} es: {union}")

#Intersección
interseccion = conjunto_1 & conjunto_2
print(f"La intersección entre conjunto_1 {conjunto_1} y conjunto_2 {conjunto_2} es: {interseccion}")

#Diferencia
diferencia = conjunto_1 - conjunto_2
print(f"La diferencia entre conjunto_1 {conjunto_1} y conjunto_2 {conjunto_2} es: {diferencia}")
