# 1. Sistema de Gestión de Estudiantes 
# o Crea una clase Estudiante con atributos como nombre, edad, y 
# notas. Implementa métodos para calcular el promedio de notas 
# y determinar si el estudiante ha aprobado o no. Agrega una 
# clase Curso que contenga una lista de estudiantes y un método 
# para mostrar todos los estudiantes aprobados. 

class Estudiantes:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
    
    #Permite calcular el promedio de un estudiante
    def calcular_promedio(self):
        promedio = sum(self.notas) / len(self.notas)
        return promedio
    
    #Permite determinar si un estudiante esta Aprobado o Reprobado
    def determinar_status_estudiante(self):
        return "Aprobado" if self.calcular_promedio() >= 6  else "Reprobado"

class Curso:
    lista_estudiantes = [
        Estudiantes("Javier",22,[6,8,5]),
        Estudiantes("Ana",23,[5,5,5]),
        Estudiantes("Marcos",23,[7,8,9])]
    
    #Permite mostrar la información de los estudiantes que aprobaron
    @classmethod
    def mostrar_info_estudiantes_aprobados(cls):
        datos = ""
        for estudiante in cls.lista_estudiantes:
            if estudiante.determinar_status_estudiante() == "Aprobado":
                datos += f"Estudiante {estudiante.nombre} - Edad {estudiante.edad} - Promedio {estudiante.calcular_promedio():.2f}\n"
        return datos

#Muestra la informacion de un curso de un estudiante aprobado
print(Curso.mostrar_info_estudiantes_aprobados()) 
        