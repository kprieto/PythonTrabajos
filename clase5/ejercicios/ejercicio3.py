# Ejercicio 3: Anidación Básica de Diccionarios 
# 1. Crea un diccionario que represente una persona con las siguientes 
# claves: 
# o Nombre 
# o Edad 
# o Dirección (donde la dirección es otro diccionario con claves: 
# Calle, Ciudad, Código postal) 
# 2. Imprime la ciudad de la dirección. 

persona = {
    "nombre": "Ana Karen",
    "edad": 35,
    "direccion": {"calle": "Sotero", "ciudad":"Ensenada", "codigoPostal": 22785}
}

ciudad = persona["direccion"]["ciudad"]
print("La ciudad es: ", ciudad)