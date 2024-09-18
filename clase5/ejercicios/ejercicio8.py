# Ejercicio 8: Modificar un Valor en un Diccionario Anidado 
# 1. Crea un diccionario que contenga información sobre una tienda de 
# libros, con las siguientes claves: 
# o nombre_tienda 
# o libros, que es una lista de diccionarios, donde cada diccionario 
# representa un libro con claves titulo y precio. 
# 2. Cambia el precio del segundo libro en la lista a un nuevo valor (por 
# ejemplo, 15.99). 
# 3. Imprime el título y el precio del segundo libro después de la 
# modificación. 

tienda_libros = {"nombre": "Librerías gandhi",
                "libros": [{"nombre": "Si te gusta la oscuridad", "precio": 549},
                        {"nombre": "La larga marcha", "precio": 299},
                        {"nombre": "Misery", "precio": 349},
                        {"nombre": "El resplandor", "precio": 519},
                        {"nombre": "El visitante", "precio": 469}                        
                        ]
    
}

def mostrarTiendaLibros(tienda_libros):
    print("Tienda de libros: \n")
    for c, l in tienda_libros.items():
        
        if c == "libros":
            print("LIBROS \n")
            for libro in l:
                print("Libro: ",libro.get("nombre"),"- Precio: ",libro.get("precio"),"\n")
        else:
            print(c, ": ", l," \n")

mostrarTiendaLibros(tienda_libros)
# Cambia el precio del segundo libro en la lista a un nuevo valor
tienda_libros["libros"][1]["precio"] = 400

print(f"Se cambio el precio del libro {tienda_libros["libros"][1]["nombre"]} por {tienda_libros["libros"][1]["precio"]} pesos. ")

mostrarTiendaLibros(tienda_libros)