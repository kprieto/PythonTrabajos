# Los tres ejemplos de escritura (TXT)

#Modo 'w': Sobreescribe el archivo
with open("modo_w.txt", 'w') as file:
    file.write("Este archivo fue sobreescrito por el modo \'w\'.\n'")
    file.write("Todo el contenido previo fue eliminado.")
print("Archivo 'modo_w.txt' creado con exito.")

#Modo 'a': Agrega contenido al archivo existente
with open("modo_a.txt", 'a') as file:
    file.write("A Este archivo  se le agrego el final con  \'a\'.\n")
    file.write("Todo el contenido previo no fue eliminado.")
print("Archivo 'modo_a.txt' creado / modificado con exito.")

#Modo 'x': Crea un nuevo archivo
with open("modo_x.txt", 'a') as file:
    file.write("A Este archivo  fue creado con exito usando  \'x\'.\n")
    file.write("Falla si ya existe el archivo.")
print("Archivo 'modo_x.txt' creado con exito.")