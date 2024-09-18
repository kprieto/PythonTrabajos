# Ejercicio 1: Operaciones Básicas con Tuplas
# Crea una tupla llamada mi_tupla con los siguientes elementos: (5, 10, 15, 20, 25).
# Usa el método count para contar cuántas veces aparece el número 10 en la tupla.
# Usa el método index para encontrar la posición del número 20 en la tupla.
# Muestra los resultados de las operaciones anteriores.

mi_tupla = (5,10,15,20,25)

valor_contar = 10
contar_num = mi_tupla.count(valor_contar)
print(f"El número {valor_contar} se repite {contar_num} veces en la tupla.")

valor_index = 20
index_valor = mi_tupla.index(valor_index)
print(f"El número {valor_index} se encuentra en la posición {index_valor} de la tupla.")