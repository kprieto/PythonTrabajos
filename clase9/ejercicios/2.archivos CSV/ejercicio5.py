# Crea un programa que guarde los siguientes datos en un archivo CSV 
# alumnos.csv: ["Nombre", "Edad"], ["Ana", 23], ["Luis", 25].
import csv

fieldnames = ["Nombre", "Edad"]

nombre_archivo = "alumnos.csv"

with open(nombre_archivo,'w', newline='') as  file:
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()

    writer.writerow({"Nombre": "Ana", "Edad": "35"})
    
    writer.writerows([
        {"Nombre": "Luis", "Edad": "35"},
        {"Nombre": "Daniela", "Edad": "31"}
        ])