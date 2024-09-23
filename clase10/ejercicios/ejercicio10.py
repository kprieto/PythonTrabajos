# 10. 
# Sistema de Notas 
# o Define una clase Materia que contenga atributos como nombre 
# y una lista de notas. Implementa métodos para añadir notas y 
# calcular el promedio. Luego, crea una clase Estudiante que 
# contenga una lista de materias y un método para calcular el 
# promedio general del estudiante. 

class Materia:
    def __init__(self, nombre, lista_notas):
        self.nombre = nombre
        self.lista_notas = lista_notas

    # Permite agregar notas a una materia
    def agregar_notas(self,notas):  
        print("--- AGREGAR NOTAS ---")   
        print(f"Materia: {self.nombre}") 
        for n in notas:
            self.lista_notas.append(n)
        return f"Se agregaron las notas {notas} a la materia {self.nombre}."
    
    #Permite calcular el promedio de una materia
    def calcular_promedio(self):
        print("--- OBTENER PROMEDIO ---")
        promedio = sum(self.lista_notas) / len(self.lista_notas)
        return f"Materia {self.nombre}: {promedio:.2f}" 

class Estudiante:
    def __init__(self):
        self.lista_materias = [Materia("Matemáticas", [10,8,9,10]),
                            Materia("Física", [9,8,7,8]),
                            Materia("Química", [10,7,9,10]),
                            Materia("Sistemas Operativos", [10,10,9,10]),
                            Materia("Ciencias Sociales", [8,8,9,10]),
                            ]
    
    #Permite calcular el promedio general de las materias de un estudiante
    def calcular_promedio_general(self):
        print("--- PROMEDIO GENERAL ---")
        promedio = 0.0
        materias = ""
        for nota in self.lista_materias:
            materias += nota.nombre + ","
            promedio += sum(nota.lista_notas) / len(nota.lista_notas)
        promedio_general = promedio / len(self.lista_materias)
        return f"Materias  {materias.rstrip(materias[-1])}: {promedio_general:.2f}"
    
materia = Materia("Programación", [6,8,9,10,5])
materia2 = Materia("Filosofía", [8,7,8,10,9])
estudiante = Estudiante()

# Permite agregar notas a la materia
print(materia.agregar_notas([10,9]))
print()

print(materia2.agregar_notas([8,9]))
print()

#Muestra el promedio de una materia de sus notas
print(materia.calcular_promedio())
print()

print(materia2.calcular_promedio())
print()

#Muestra el promedio general de las materias de un estudiante
print(estudiante.calcular_promedio_general())


