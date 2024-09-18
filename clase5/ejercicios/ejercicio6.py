# Ejercicio 6: Anidación Compleja de Diccionarios y Listas 
# 1. Crea un diccionario que contenga información sobre una escuela. La 
# escuela tiene: 
# o Nombre 
# o Año de fundación 
# o Lista de clases, donde cada clase es un diccionario con: 
# ▪ Nombre de la clase 
# ▪ Lista de estudiantes, donde cada estudiante es un 
# diccionario con: 
# ▪ Nombre 
# ▪ Edad 
# 2. Imprime el nombre del primer estudiante de la primera clase. 

escuela = {
    "nombre":"UABC",
    "añoFundacion": 1965,
    "clases":[{"nombreClase":"Programación"},
            {"nombreClase":"Calculo diferencial"},
            {"nombreClase":"Sistemas Operativos"}
            ],
    "estudiantes":[{"nombreEstudiante":"Salvador", "edad": 25},
                {"nombreEstudiante":"Elena", "edad": 28},
                {"nombreEstudiante":"Cristobal", "edad": 24}
                ]
}

print("Datos de la escuela: \n")
for clave,datos in escuela.items():
    
    if clave == "clases":
        print("CLASES \n")
        for d in datos:
            print("Clase: ",d.get("nombreClase"),"\n")    
    elif clave == "estudiantes":
        print("ESTUDIANTES \n")
        for d in datos:
            print("Estudiante: ",d.get("nombreEstudiante"),"- Edad: ",d.get("edad"),"\n")
    else:
        print(clave, ": ", datos,"\n")

# Imprime el nombre del primer estudiante de la primera clase

nombre_estudiante = escuela["estudiantes"][0]["nombreEstudiante"]
nombre_clase = escuela["clases"][0]["nombreClase"]

print(f"El estudiante {nombre_estudiante} esta cursando la clase de {nombre_clase}.")

