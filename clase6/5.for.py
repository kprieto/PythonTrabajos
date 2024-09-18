# Programa para imprimir cuadrados de numeros y calcular la suma

# lista de numeros
numeros = [1,2,3,4,5]

# Iniciamos variable
suma_cuadrado = 0

#Iterar sobre cada numero en la lista
for numero in numeros:
    # Calcular el cuadrado del numero
    cuadrado = numero ** 2
    # Imprimir el cuadrado
    print(f"El cuadrado de {numero} es {cuadrado}")
    # agregar el cuadrado a la suma
    suma_cuadrado += cuadrado

#Imprimir 
print(f"La suma de los cuadrados es: {suma_cuadrado}")
