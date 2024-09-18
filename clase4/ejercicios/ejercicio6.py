# Ejercicio 3. Verificación de numeros pares e impares con operador ternario

numero = float(input("Introduce un número: "))
verificar_par_o_impar = "Par" if numero % 2 == 0 else "Impar"
print(f"El número {numero} es {verificar_par_o_impar}")