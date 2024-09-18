# Ejemplo 1 - Basico funcion anidad
def funcion_externa(x):
    def funcion_interna(y):
        return y + 10
    return funcion_interna(x) #Llamada a la funcion interna con el valor x

#Llamda a la funcion externa
resultado = funcion_externa(5)
print(f"Resultado de la funcion_externa(5): {resultado}")

# Ejemplo 2 - Closure
def crear_multiplicador(factor):
    def multiplicar(x):
        return x *  factor
    return multiplicar
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)
print(f"Duplicar 10: {duplicar(10)}")
print(f"Triplicar 10: {triplicar(10)}")