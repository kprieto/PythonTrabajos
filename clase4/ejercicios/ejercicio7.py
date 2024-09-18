# Ejercicio 4. Calcular el precio final con descuento 15%

precio = float(input("Introduce el precio de un producto: "))

precio_final = precio - (precio * 0.15) if precio >= 200 else precio
print(f"El precio final es $ {precio_final}")