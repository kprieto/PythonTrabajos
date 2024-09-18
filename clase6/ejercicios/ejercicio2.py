# 2. Ejercicio de while y for 
# Desarrolla un programa que haga lo siguiente: 
# 1. Usar un bucle while para pedir al usuario que ingrese números 
# hasta que se ingrese el número 0. 
# 2. Usar un bucle for para calcular la suma de los números ingresados, 
# excluyendo el 0. 

def programa_Peticion_Y_Suma_De_Numeros():
    lista_numeros = [] 
    
    while True:
        numero = int(input("Introduce un número: "))        
        if numero == 0:
            break
        else:
            lista_numeros.append(numero)
    suma = 0
    for n in lista_numeros:        
        suma += n
    
    return suma

suma = programa_Peticion_Y_Suma_De_Numeros()
print(f"La suma de los numeros ingresados es: {suma}")