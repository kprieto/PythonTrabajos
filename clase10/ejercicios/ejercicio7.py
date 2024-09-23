# 7. Juego de Animales 
# o Define una clase Animal con un método hacer_sonido(). Crea 
# subclases Perro y Gato que implementen este método de 
# manera diferente. Usa polimorfismo para crear una función que 
# acepte una lista de animales y haga que todos emitan su 
# sonido.

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Mu"
    
class Leon(Animal):
    def hacer_sonido(self):
        return "Raa"

class Cerdo(Animal):
    def hacer_sonido(self):
        return "Oink"
    
class Rana(Animal):
    def hacer_sonido(self):
        return "Croac"

def hacer_sonido_animal():
    lista_animales = [
                    Perro(),
                    Gato(),
                    Vaca(),
                    Leon(),
                    Cerdo(),
                    Rana()
                    ]
    animales = ""
    for a in lista_animales:
        animales += f"{a.__class__.__name__}: {a.hacer_sonido()}\n"
    return animales

print(hacer_sonido_animal())