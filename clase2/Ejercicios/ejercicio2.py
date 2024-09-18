# Ejercicio 2: Categoría de Edad con Operadores Lógicos
# Escribe un programa que clasifique a una persona en
# una categoría según su edad. Usa un condicional 
# if tradicional con operadores lógicos (and, or)
# para las siguientes categorías:
# "Niño" si la edad está entre 0 y 12 años.
# "Adolescente" si la edad está entre 13 y 19 años.
# "Adulto" si la edad está entre 20 y 64 años.
# "Adulto Mayor" si la edad es 65 o más.

edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad <= 12:
    categoria = "Niño"
elif edad >= 13 and edad <= 19:
    categoria = "Adolescente"
elif edad >= 20 and edad <= 64:
    categoria = "Adulto"
elif edad >= 65:
    categoria = "Adulto Mayor"
else:
    categoria = "Edad no definida"

print(f"Tu clasificación según tu edad es: {categoria}")
