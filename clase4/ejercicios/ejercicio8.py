#Ejercicio 5. Verificar el estado de un número con operador ternario. Si un 
# número es positivo, negativo o cero
numero = float(input("Introduce un número: "))

verificar_numero = f"El número {numero} es positivo." if numero > 0 else f"El número {numero} es negativo" if numero < 0 else f"El número es cero."
print(verificar_numero)
