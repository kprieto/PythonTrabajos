import random

def trivia():
    # Definir las preguntas y respuestas de la trivia utilizando tuplas
    preguntas_respuestas = (
        ("¿Es Python un programa de lenguaje de alto nivel?", 
        ("A) True", 
        "B) False"),
        "A"),
        
        ("¿Cómo se define una tupla vacía en Python?", 
        ("A) []", 
        "B) ()", 
        "C) {}", 
        "D) Tupla()"),
        "B"),
        
        ("¿Es posible modificar los elementos de una tupla después de su creación?", 
        ("A) Sí, usando el índice del elemento.",
        "B) No, porque las tuplas son inmutables.",
        "C) Sí, usando el método update().",
        "D) Solo si la tupla está vacía."),
        "B"),
        
        ("¿Cuál es el resultado de `len((1, 2, (3, 4)))`?", 
        ("A) 2", 
        "B) 3", 
        "C) 4", 
        "D) Error"),
        "B"),
        
        ("¿Cómo se puede acceder al segundo elemento de una tupla `mi_tupla = (10, 20, 30)`?", 
        ("A) mi_tupla[2]", 
        "B) mi_tupla[1]", 
        "C) mi_tupla[-1]", 
        "D) mi_tupla[0]"),
        "B"),
        
        ("¿Qué operador se utiliza para concatenar dos tuplas?", 
        ("A) +", 
        "B) &", 
        "C) *", 
        "D) |"),
        "A"),
        
        ("¿Cuál es el resultado de `3 * (1, 2)`?", 
        ("A) (1, 2, 1, 2, 1, 2)", 
        "B) (3, 6)", 
        "C) (1, 2, 3)", 
        "D) Error"),
        "A"),
        
        ("¿Cuál es la sintaxis correcta para crear una tupla de un solo elemento en Python?", 
        ("A) (1,)", 
        "B) (1)", 
        "C) [1]", 
        "D) Tupla(1)"),
        "A")
    )

    # Mezclar las preguntas para aleatoriedad
    preguntas_aleatorias = list(preguntas_respuestas)
    random.shuffle(preguntas_aleatorias)

    # Iniciar la trivia
    print("¡Bienvenido a la trivia de Tuplas en Python!")
    puntaje = 0
    
    for i, pregunta in enumerate(preguntas_aleatorias):
        print(f"\nPregunta {i + 1}: {pregunta[0]}")
        for opcion in pregunta[1]:
            print(opcion)
        
        respuesta_usuario = input("Tu respuesta (A, B, C, D): ").strip().upper()

        if respuesta_usuario == pregunta[2]:
            print("¡Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {pregunta[2]}")

    print(f"\nTu puntaje final es: {puntaje} de {len(preguntas_respuestas)}")
    if puntaje > len(preguntas_respuestas) / 2:
        print("¡Buen trabajo!")
    else:
        print("Sigue practicando, puedes mejorar.")

# Ejecutar la trivia
trivia()