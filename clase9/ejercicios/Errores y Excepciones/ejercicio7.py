# Ejercicio 7: Usar assert 
# Crea un programa que pida al usuario ingresar su edad. Usa assert para 
# verificar que la edad ingresada es mayor o igual a 18. Si no es así, 
# muestra un mensaje de error. 

def verificar_edad(edad):
    
    assert edad >= 18, "Error: Eres menor de edad no puedes ingresar al programa."
    return "Eres mayor de edad puedes ingresar al programa."

edad = int(input("Ingresa tu edad: "))
print(verificar_edad(edad))