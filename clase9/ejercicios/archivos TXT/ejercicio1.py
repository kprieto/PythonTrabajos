# Ejercicio 1: Leer un archivo TXT 
# Crea un programa en Python que lea el contenido de un archivo 
# mi_archivo.txt y muestre cada línea en la consola. El archivo tiene varias 
# líneas de texto. Usa el método que prefieras para leer el archivo. 

nombre_archivo = "mi_archivo.txt"
with open(nombre_archivo, 'r') as archivo:
    print("Leyendo el archivo linea por linea: ")
    linea = archivo.readline()
    while linea:
        print(linea.strip())
        linea = archivo.readline()
