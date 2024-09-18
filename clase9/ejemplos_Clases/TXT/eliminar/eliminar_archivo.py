import os #importamos modulo

# Definimos el nombre del archivo
nombre_archivo = 'archivo.txt'

#Comprobar si el archivo existe en la ruta especificada
#La funcion os.path.exists() devuelve True en caso si el archivo existe
#False en caso contrario
if os.path.exists(nombre_archivo):
    #Si el archivo existe, procedera a eliminarlo 
    #Y la función os.remove() elimina el archivo en la ruta especificada
    os.remove(nombre_archivo)
    print(f"Archivo {nombre_archivo} eliminado")
else:
    # Si el archivo no existe, informar al usuario que no se encontro nada
    print(f"El Archivo {nombre_archivo} no existe.")