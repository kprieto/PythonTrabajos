# Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario 
# 1. Usando el diccionario del ejercicio anterior, actualiza el año de 
# publicación a 1968. 
# 2. Elimina el género del diccionario. 
# 3. Imprime el diccionario después de cada operación. 

libro = {
    "titulo": "El Instituto",
    "autor": "Stephen King",
    "año": 2022,
    "genero": "Terror"
}

print("Diccionario original: ")
for c, d in libro.items():
    print(c,":",d)
# Actualizar año de publicación
libro["año"] = 1968

print("Diccionario despues de la actualización: ")
for c, d in libro.items():
    print(c,":",d)
    
# Eliminar el genero del diccionario
del libro["genero"]

print("Diccionario despues de la eliminación: ")
for c, d in libro.items():
    print(c,":",d)