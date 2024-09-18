# Ejercicio 1: Crear y Acceder a un Diccionario Básico 
# 1. Crea un diccionario que contenga la siguiente información sobre un 
# libro: 
# o Título 
# o Autor 
# o Año de publicación 
# o Género 
# 2. Accede e imprime cada uno de estos valores usando las claves 
# correspondientes. 

libro = {
    "titulo": "El Instituto",
    "autor": "Stephen King",
    "año": 2022,
    "genero": "Terror"
}

titulo = libro["titulo"]
autor = libro.get("autor")
anio = libro["año"]
genero = libro.get("genero")

print("Titulo: ", titulo)
print("Autor: ", autor)
print("Año de publicacion: ", anio)
print("Genero: ", genero)