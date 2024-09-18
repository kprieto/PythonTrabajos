# 4. Ejercicio de while con Condiciones y Contadores 
# Desarrolla un programa que: 
# 1. Use un bucle while para generar números de la serie de Fibonacci. 
# 2. Continúe generando números hasta que el número actual sea mayor 
# o igual a 100. 
# 3. Imprima la serie de Fibonacci generada. 


print("¡Serie de Fibonacci!")
fibonacci = [0,1]
while True:  
    resultado = fibonacci[-1] + fibonacci[-2]  
    if resultado >= 100:
        break

    fibonacci.append(resultado)
    
    
print(fibonacci)   