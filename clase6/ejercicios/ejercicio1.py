# 1. Ejercicio de Sets y for 
# Crea un programa que reciba una lista de números y realice las siguientes 
# operaciones: 
# 1. Crear un set a partir de la lista para eliminar duplicados. 
# 2. Iterar sobre el set e imprimir cada número. 
# 3. Contar cuántos números son mayores que un valor dado y 
# almacenarlos en un nuevo set. 

def contarNumeroMayores(set_numeros):
    numero = int(input("Introduce un número: "))
    contador = 0
    set_mayores = set()
    for i in set_numeros:
        if i > numero:
            contador += 1
            set_mayores.add(i)
    return set_mayores,numero

def crearSet(lista_numeros):
    set_numeros = set((lista_numeros))
    set_numeros_mayores = set()
    numero = 0
    print("Lista de numeros:")
    for n in set_numeros:
        print(n)
    set_numeros_mayores,numero = contarNumeroMayores(set_numeros)
    return set_numeros_mayores,numero

set_numeros_mayores,numero = crearSet([1,25,45,85,25,69,152,148,65,258,69,13,354])

if set_numeros_mayores != set():        
    print(f"El número ingresado fue {numero}, los numeros mayores de la lista son:{set_numeros_mayores}")    
else:
    print(f"El número ingresado fue {numero}, no existen numeros mayores en la lista.")    

