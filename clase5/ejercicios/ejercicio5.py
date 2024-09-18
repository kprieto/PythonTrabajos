# Ejercicio 5: Diccionario dentro de una Lista 
# 1. Crea una lista de diccionarios donde cada diccionario representa un 
# producto en una tienda, con claves: 
# o Nombre 
# o Precio 
# o Cantidad en stock 
# 2. Imprime el nombre y el precio del segundo producto en la lista.

producto = [{"nombre":"leche","precio":185,"cantidadStock": 15},
            {"nombre":"sabritas","precio":55,"cantidadStock": 25},
            {"nombre":"carne","precio":100,"cantidadStock": 10}]

nombre_producto = producto[1]["nombre"]
precio_producto = producto[1]["precio"]

print(f"El producto {nombre_producto} tiene un precio de {precio_producto} pesos.")