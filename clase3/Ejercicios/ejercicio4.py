# Ejercicio 4: Clasificación de Alumnos
# Escribe un programa que clasifique a los alumnos en dos listas: aprobados y desaprobados, según sus calificaciones.
# Instrucciones:
# Define una lista con las calificaciones de los alumnos.
# Define dos listas vacías: aprobados y desaprobados.
# Usa un bucle para recorrer la lista de calificaciones.
# Si la calificación es 60 o más, añade el nombre del alumno a la lista de aprobados, si no, añádelo a desaprobados.
# Muestra las listas de aprobados y desaprobados.

lista_alumnos = ["Ana", "Juan", "María","Luis","Carmen"]
lista_calificaciones = [35,55,90,40,70]
lista_aprobados = []
lista_reprobados = []

for calificacion in lista_calificaciones:
    i = lista_calificaciones.index(calificacion)    
    if calificacion >= 60:
        lista_aprobados.append(lista_alumnos[i])
    else:
        lista_reprobados.append(lista_alumnos[i])


print("Aprobados: ", lista_aprobados)
print("Reprobados: ", lista_reprobados)