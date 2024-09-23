# 6. Sistema de Biblioteca 
# o Crea una clase Libro con atributos titulo, autor, y paginas. 
# Luego, crea una clase Biblioteca que contenga una lista de 
# libros. Agrega métodos para añadir libros, buscar por autor y 
# mostrar todos los libros. Implementa encapsulamiento para 
# proteger la lista de libros. 

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        

class Biblioteca:
    def __init__(self):
        self._lista_libros =  [
        Libro("Cien años de soledad", "Gabriel García Márquez", 471),
        Libro("El Instituto", "Stephen King", 624),
        Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863),
        Libro("El señor de los anillos", "J.R.R. Tolkien", 1216),
        Libro("Matar a un ruiseñor", "Harper Lee", 281),
        Libro("La Odisea", "Homero", 543)
    ]
    
    # Permite agregar un libro a la biblioteca
    def agregar_libro(self, titulo, autor, paginas):
        print("--- AGREGAR LIBRO ---")
        for libro in self._lista_libros:        
            if titulo.title() == libro.titulo.title():
                return f"El libro {titulo.title()} ya está registrado."
    
        self._lista_libros.append(Libro(titulo.title(),autor.title(),paginas))
        return f"El libro {titulo.title()} fue registrado exitosamente."
    
    # Permite buscar un libro por autor
    def buscar_por_autor(self, autor):
        print("--- BUSCAR POR AUTOR ---")
        print(f"AUTOR: {autor.title()}")
        libro_autor = ""
        for libro in self._lista_libros:
            if autor.title() == libro.autor.title():                
                libro_autor += f"Libro: {libro.titulo} - Páginas: {libro.paginas} \n"
        return libro_autor
    
    #Permite mostrar la información de todos los libros de la biblioteca
    def mostrar_info_libros(self):
        print("--- MOSTRAR LIBROS ---")
        libros = ""
        for libro in self._lista_libros:
            libros += f"Libro: {libro.titulo} - Autor: {libro.autor} - Páginas: {libro.paginas}\n"
        return libros
    
biblioteca = Biblioteca()

#Agregar un nuevo libro
print(biblioteca.agregar_libro("por amor a mí", "alma lozano", 174))
print()
print(biblioteca.agregar_libro("It(eso)", "stephen king", 1503))
print()

#Agregar un libro ya existente
print(biblioteca.agregar_libro("por amor a mí", "alma lozano", 174))
print()

#Buscar libros por autor
print(biblioteca.buscar_por_autor("stephen king"))
print()

#Mostrar libros de la biblioteca
print(biblioteca.mostrar_info_libros())

