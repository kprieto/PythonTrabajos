# Ejercicio 2: Escribir en un archivo TXT 
# Crea un programa que escriba un texto en un archivo nuevo_archivo.txt. Si 
# el archivo ya existe, debe sobrescribir su contenido.
nombre_archivo = "nuevo_archivo.txt"
with open(nombre_archivo, 'w', encoding="utf-8") as file:
    file.write("Este archivo fue sobreescrito con la siguiente información: \n")
    file.write("Hola Chicas!, Sigamos aprendiendo Python! ")
print("Archivo 'nuevo_archivo.txt' creado con exito.")
