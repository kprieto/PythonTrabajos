import datetime

#Petición de fecha de nacimiento al usuario
def peticion_fecha_nacimiento():    
    return input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")

#Calcular la edad del usuario
def calcular_edad(fecha_nacimiento):
    año_actual = datetime.datetime.now().year
    fecha = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y').date()
    edad = año_actual - fecha.year    
    return edad