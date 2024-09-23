#2. Propiedades de un Objeto

#Definir la clase persona:
class Persona:
    def __init__(self, nombre, edad):
        #Inicializar las propiedades del objeto
        self.nombre = nombre #Propiedad nombre
        self.edad = edad #Propiedad edad
        
# Crear un objeto de la clase persona
persona1 = Persona("Karen", 35)
persona2 = Persona("Luis", 30)


#Acceder a las propiedades del objeto
print(persona1.nombre)
print(persona1.edad)

#Acceder a las propiedades del objeto
print(persona2.nombre)
print(persona2.edad)

# La clase persona define un objeto que tiene propiedades como nombre y edad.
# Al instanciar persona1 con valores especificos, se crean atributos unicos que representa
# el estado de ese objeto.
# Se puede acceder a estas propiedades utilizando la notacion de punto, lo que permite
# obtener informacion sobre las instancia creada.