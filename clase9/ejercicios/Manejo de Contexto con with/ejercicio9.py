# Ejercicio 9: Usar with/as para manejar archivos 
# Crea un programa que abra un archivo notas.txt, lea su contenido, y lo 
# muestre en la consola. Usa el bloque with para asegurarte de que el 
# archivo se cierra automáticamente. 

nombre_archivo = "notas.txt"

with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
    linea = archivo.readline()
    
    while linea:
        print(linea.strip())
        linea = archivo.readline()