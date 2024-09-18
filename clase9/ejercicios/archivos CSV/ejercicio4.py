# Ejercicio 4: Leer un archivo CSV 
# Crea un programa que lea los datos de un archivo CSV datos.csv y 
# muestre cada fila en la consola. 
import csv

nombre_archivo = "datos.csv"

with open(nombre_archivo, 'r', encoding="utf-8") as file:
    reader_dic = csv.DictReader(file)
    
    for fila in reader_dic:
        print(fila)