# Ejercicio 4: Lista de Diccionarios 
# 1. Crea una lista de diccionarios, donde cada diccionario representa un 
# estudiante con las siguientes claves: 
# o Nombre 
# o Edad 
# o Calificaciones (que es una lista de números) 
# 2. Imprime el nombre y las calificaciones del primer estudiante en la 
# lista. 

estudiante = [{
    "nombre": "Alberto",
    "edad": 36,
    "calificaciones": [78,90,86,98]
},
{
    "nombre": "Daniela",
    "edad": 30,
    "calificaciones": [67,78,85,90]
},
{
    "nombre": "Jorge",
    "edad": 34,
    "calificaciones": [58,66,75,91]
},
{
    "nombre": "Lorena",
    "edad": 32,
    "calificaciones": [74,85,95,91]
}]

nombre = estudiante[0]["nombre"]
calificaciones = estudiante[0]["calificaciones"]

print(f"El estudiante {nombre} tiene estas calificaciones: {",".join(map(str,calificaciones))}")

