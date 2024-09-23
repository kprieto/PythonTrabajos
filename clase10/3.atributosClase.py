# 3.Atributos de Clase

#Definimos la clase coche
class Coche:
    ruedas = 4 #Atributo de clase: Todas las instancias de coche tiene 4 ruedas.
    
    def __init__(self, marca, modelo):
        self.marca = marca # Atributo de instancia
        self.modelo = modelo # Atributo de instancia

# Imprimir el atributo de clase
print(Coche.ruedas)

# Crear instancias de la clase coche
coche1 = Coche("Toyata", "Corolla")
coche2 = Coche("Honda", "Civic")

# Acceder al atributo de clase de las instancias
print(coche1.ruedas)
print(coche2.ruedas)

# En la clase coche, el atributo ruedas es una atributo de clase que se aplica a todas
# las instancias de la clase, estableciendo que cada coche tiene 4 ruedas.
# Este atributo que se puede acceder tanto desde las clases como desde las instancias, lo
# que permite compartir datos comunes entre todos los objetos de esa clase.

