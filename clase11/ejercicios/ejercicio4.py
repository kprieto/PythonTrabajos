# Ejercicio 4: Combina math, random y datetime 
# • Objetivo: Usar los tres módulos en un solo ejercicio para hacer 
# un mini programa de predicción de edad futura con un valor 
# aleatorio. 
# • Descripción: Calcula la edad de una persona y predice su edad 
# dentro de un número aleatorio de años entre 1 y 10. 
# • Instrucciones: 
# ✓ Solicita la fecha de nacimiento. 
# ✓ Calcula la edad actual. 
# ✓ Genera un número aleatorio entre 1 y 10. 
# ✓ Predice la edad de la persona en ese número aleatorio 
# de años. 

import fechayedad
import random

#Solicitar fecha de nacimiento al usuario
fecha_nacimiento = fechayedad.peticion_fecha_nacimiento()

#Calcular la edad actual del usuario
print(f"Tu edad es: {fechayedad.calcular_edad(fecha_nacimiento)} años.")

#Generar un número aleatorio entre 1 y 10
num_aleatorio = random.randint(1,10)

#Predecir la edad del usuario con el número aleatorio anterior
edad = fechayedad.calcular_edad(fecha_nacimiento) + num_aleatorio
print(f"En {num_aleatorio} años tendras la edad de {edad} años.")