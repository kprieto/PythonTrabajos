# Ejercicio 3: Fechas y Tiempos con el Módulo datetime 
# • Objetivo: Trabajar con fechas y tiempos utilizando el módulo 
# datetime. 
# • Descripción: Calcula la edad de una persona y muestra la fecha 
# actual en diferentes formatos. 
# • Instrucciones: 
# ✓ Solicita al usuario su fecha de nacimiento en formato 
#     DD/MM/AAAA. 
# ✓ Calcula su edad. 
# ✓ Muestra la fecha actual en los siguientes formatos: 
#     Día-Mes-Año. 
#     Mes/Día/Año. 
#     Año/Mes/Día. 

import datetime
import fechayedad

#Funcion que muestra la fecha actual en diferentes formatos
def mostrar_formatos_fechas():
    fecha_actual = datetime.datetime.now()
    formato_fecha = fecha_actual.strftime('%d-%m-%Y')
    print(f"Fecha en formato Día-Mes-Año : {formato_fecha}")
    formato_fecha2 = fecha_actual.strftime('%m/%d/%Y')
    print(f"Fecha en formato Mes/Día/Año : {formato_fecha2}")
    formato_fecha3 = fecha_actual.strftime('%Y/%m/%d')
    print(f"Fecha en formato Año/Mes/Día : {formato_fecha3}")

#Petición de fecha de nacimiento al usuario
fecha_nacimiento = fechayedad.peticion_fecha_nacimiento()

#Muestra la edad actual del usuario
print(f"Tu edad es: {fechayedad.calcular_edad(fecha_nacimiento)} años")
print()

#Muestra la fecha actual en diferentes formatos
mostrar_formatos_fechas()



