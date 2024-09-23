# 3. Sistema de Reservas de Hotel 
# o Crea una clase Habitacion con atributos como numero, tipo, y 
# precio. Luego, crea una clase Hotel que contenga una lista de 
# habitaciones y métodos para reservar, cancelar y mostrar 
# habitaciones disponibles. 

class Habitacion:
    def __init__(self, numero, tipo, precio, disponibilidad):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponibilidad = disponibilidad
    
class Hotel:
    lista_habitaciones = [Habitacion(20,"Indivual", 850.50,True),
                        Habitacion(24,"Doble", 1525.36,True),
                        Habitacion(34,"Triple",2566.52,True),
                        Habitacion(50,"Suite principal",3856.65,True)
                        ]
    
    #Permite crear la reservación de una habitación
    @classmethod
    def reservar_habitacion(cls, numero_habitacion):
        print("--- Reservación ---")
        for habitacion in cls.lista_habitaciones:
            if numero_habitacion == habitacion.numero:
                if habitacion.disponibilidad:
                    habitacion.disponibilidad = False
                    return f"La habitación {habitacion.numero} tipo {habitacion.tipo} con un precio {habitacion.precio}, fue reservada con éxito."
                else:
                    return f"La habitación {habitacion.numero} ya estaba ocupada."
        return f"La habitación {numero_habitacion} no existe en el hotel"
    
    #Permite cancelar la reservación de una habitación
    @classmethod
    def cancelar_habitacion(cls, numero_habitacion):
        print("--- Cancelación ---")
        for habitacion in cls.lista_habitaciones:
            if numero_habitacion == habitacion.numero:
                if not habitacion.disponibilidad:
                    habitacion.disponibilidad = True
                    return f"La habitación {habitacion.numero} tipo {habitacion.tipo} con un precio {habitacion.precio} ha sido cancelada."
                else:
                    return f"La habitación {habitacion.numero} ya estaba disponible."
        return f"La habitación {numero_habitacion} no existe en el hotel"

    #Permite mostrar las habitaciones que estan estado disponible
    @classmethod
    def mostrar_habitaciones_disponibles(cls):
        print("--- Habitaciones Disponibles ---")
        habitaciones = ""
        for habitacion in cls.lista_habitaciones:            
            if habitacion.disponibilidad == True:
                habitaciones += f"Habitación {habitacion.numero} \nTipo {habitacion.tipo} \nPrecio {habitacion.precio} \n "
        return habitaciones

#Mostrar las habitaciones disponibles antes de reservar o cancelar
print(Hotel.mostrar_habitaciones_disponibles())

#Reservar una habitación
print(Hotel.reservar_habitacion(50))
print(Hotel.reservar_habitacion(24))

#Intentar reservar la misma habitación
print(Hotel.reservar_habitacion(50))

#Cancelar una habitación
print(Hotel.cancelar_habitacion(50))

#Mostrar las habitaciones disponibles
print()
print(Hotel.mostrar_habitaciones_disponibles())