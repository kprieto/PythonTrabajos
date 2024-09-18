import csv

#Definimos los nombres de las columnas para el archivo csv
fielnames = ["Nombre", "Edad", "Ciudad"]

#newline='' se utiliza para evitar lineas en blancoen algunos S.O.
with open("archivo.csv", 'w', newline='') as  file:
    #Creamos un objeto DictWriter
    #Se pasa el archivo y la lista de nombres de columnas (fielnames)
    writer = csv.DictWriter(file, fieldnames=fielnames)
    
    #escribir la fila de encabezados en el archivo csv
    #Esto crea la primera fila con los nombre de columnas
    writer.writeheader()
    
    #Escribir una fila con los datos de un archivo csv
    #cada diccionario debe tener claves que coincidan con los nombres de las columnas
    writer.writerow({"Nombre": "Ana", "Edad": "35", "Ciudad": "Neuquen"})
    
    #escribir multiples filas de datos en el archivo csv
    writer.writerows([
        {"Nombre": "Julia", "Edad": "35", "Ciudad": "Neuquen"},
        {"Nombre": "Mario", "Edad": "35", "Ciudad": "Neuquen"}
        ])
    