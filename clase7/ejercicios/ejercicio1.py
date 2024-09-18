# 1. Ejercicio de List Comprehension con range y for 
# Crea un programa que: 
# 1. Genere una lista de números del 1 al 10 usando range. 
# 2. Cree una nueva lista que contenga el cuadrado de cada número 
# solo si el número es impar. 

lista_numeros = [n for n in range(1,11)]

cuadrados = [x ** 2 for x in lista_numeros if x % 2 != 0]

print(f"Lista de numeros: {lista_numeros}")
print(f"Los cuadrados de los numeros impares de la lista son: {cuadrados}")