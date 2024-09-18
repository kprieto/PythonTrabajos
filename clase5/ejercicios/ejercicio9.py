# Ejercicio 9: Buscar y Imprimir la Edad de un Estudiante en un 
# Diccionario Anidado 
# 1. Crea un diccionario que represente una clase con los siguientes 
# datos: 
# o nombre_clase 
# o estudiantes, que es una lista de diccionarios con información 
# de cada estudiante (nombre y edad). 
# 2. Escribe una función que busque la edad de un estudiante dado su 
# nombre usando el índice de la lista en lugar de bucles (suponiendo 
# que conoces el índice). 
# 3. Imprime la edad del estudiante buscado. 

clase = {"nombre": "Programación",
        "estudiantes": [{"nombre": "Javier", "edad": 25},
                        {"nombre": "Daniela", "edad": 28},
                        {"nombre": "María", "edad": 24},
                        {"nombre": "Alberto", "edad": 27},
                        {"nombre": "Lourdes", "edad": 23}
                        ]
}
def obtener_Edad(nombre, indice, clase):
    estudiante = clase["estudiantes"]
    if 0 <= indice < len(estudiante) and estudiante[indice]["nombre"] == nombre:
        return estudiante[indice]["edad"]
    
indice = int(input("Introduce un índice a buscar: "))
nombre = input("Introduce el nombre del estudiante: ").capitalize()

edad = obtener_Edad(nombre,indice,clase)
if edad is not None:
    print(f"La edad del estudiante {nombre} es de {edad} años.")
else:
    print(f"No se encontro la edad del estudiante {nombre}.")
