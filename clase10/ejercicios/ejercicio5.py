# 5. Clases de Vehículos 
# o Crea una clase base Vehiculo que tenga atributos marca y 
# modelo. Luego, crea subclases Coche y Motocicleta que 
# hereden de Vehiculo. Implementa el método mostrar_info() en 
# cada subclase que utilice super() para mostrar la información 
# básica y luego la específica de cada vehículo. 

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, ruedas):
        super().__init__(marca, modelo)
        self.ruedas = ruedas
    
    def mostrar_info(self):         
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Ruedas: {self.ruedas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ruedas):
        super().__init__(marca, modelo)
        self.ruedas = ruedas
    
    def mostrar_info(self):         
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Ruedas: {self.ruedas}"


#Lista de coches
lista_coches = [Coche("Toyota", "Corolla",4),
            Coche("Ford", "Mustang",4),
            Coche("Honda", "Civic",4),
            Coche("Tesla", "Model S",4) ]

#Mostrar información de coches
print("--- MOSTRAR INFORMACIÓN DE COCHES ---")
for coche in lista_coches:
    print(Coche.mostrar_info(coche))

print()

#Lista de motocicletas
lista_motocicletas = [
        Motocicleta("Yamaha", "MT-07",2),
        Motocicleta("Honda", "CBR600RR",2),
        Motocicleta("Kawasaki", "Ninja 650",2),
        Motocicleta("Ducati", "Panigale V4",2)
    ]

#Mostrar información de moticicletas
print("--- MOSTRAR INFORMACIÓN DE COCHES ---")
for motocicleta in lista_motocicletas:
    print(Motocicleta.mostrar_info(motocicleta))