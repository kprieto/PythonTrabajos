# Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices
# Crea una tupla llamada frutas con los siguientes elementos: ("manzana", "banana", "cereza").
# Usa el método index para encontrar la posición de la fruta "banana".
# Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente.

frutas = ("manzana", "banana", "cereza")

fruta_a_buscar = "banana"
valor_index = frutas.index(fruta_a_buscar)
print(f"La fruta {fruta_a_buscar} se encuentra en la posición {valor_index} en la tupla.")

fruta_a_verificar = "naranja"

if fruta_a_verificar in frutas:
    print(f"La fruta {fruta_a_verificar} se encuentra en la tupla.")
else:
    print(f"La fruta {fruta_a_verificar} no se encuentra en la tupla.")
    
    
