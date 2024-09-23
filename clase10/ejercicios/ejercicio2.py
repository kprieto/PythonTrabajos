# 2. Clases de Formas Geométricas 
# o Define una clase base Forma con un método area(). Luego, 
# crea subclases Rectangulo, Circulo, y Triangulo que 
# implementen el método area() de manera específica. Usa 
# polimorfismo para crear una lista de formas y calcular el área 
# de cada una. 
import math
class Forma:
    def area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return f"{(math.pi * (self.radio)**2):.2f}"

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base * self.altura)/2

def calcular_areas(forma): 
    area = ""
    for f in forma:        
        area += f"El área de {f.__class__.__name__ } : {f.area()} \n"
    return area
    
formas = [Rectangulo(5, 10),
            Circulo(9),          
            Triangulo(6, 20)      
            ] 
print(calcular_areas(formas))