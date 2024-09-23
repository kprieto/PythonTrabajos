# 4. Sistema de Inventario 
# o Define una clase Producto con atributos como nombre, precio, 
# y cantidad. Agrega métodos para aumentar o disminuir la 
# cantidad de productos. Luego, crea una clase Inventario que 
# contenga una lista de productos y métodos para agregar y 
# mostrar productos. 

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    #Aumentar la cantidad de un producto
    @staticmethod
    def aumentar_producto(nombre, cantidad_aumentar, lista_productos):
        print("--- AUMENTAR CANTIDAD DE UN PRODUCTO ---")
        for producto in lista_productos:
            if nombre.title() == producto.nombre.title():
                if cantidad_aumentar > 0:
                    producto.cantidad += cantidad_aumentar
                    return f"Se han agregado {cantidad_aumentar} unidades de {nombre.title()}. Nueva cantidad: {producto.cantidad}"
                else:
                    return f"La cantidad a aumentar deber ser mayor a 0."
        return f"El producto {nombre.title()} no esta registrado."
    
    #Disminuir la cantidad de un producto
    @staticmethod
    def disminuir_producto(nombre, cantidad_disminuir, lista_productos):
        print("--- DISMINUIR CANTIDAD DE UN PRODUCTO ---")
        for producto in lista_productos:
            if nombre.title() == producto.nombre.title():
                if cantidad_disminuir > 0:
                    if producto.cantidad >= cantidad_disminuir:
                        producto.cantidad -= cantidad_disminuir
                        return f"Se han reducido {cantidad_disminuir} unidades de {nombre.title()}. Nueva cantidad: {producto.cantidad}"
                    else:
                        return f"No hay suficiente stock del producto {nombre.title()} para retirar {cantidad_disminuir} unidades."
                else:
                    return f"La cantidad a disminuir deber ser mayor a 0."
        return f"El producto {nombre.title()} no esta registrado."

class Inventario:
    lista_productos = [Producto("Jabón",25.50,5),
                    Producto("Cepillo Dental",45.50,10),
                    Producto("Carne",180.36,8),
                    Producto("Tortillas",20.00,11),
                    Producto("Arroz",35.45,4),
                    Producto("Plátano",30.25,20),
                    Producto("Cerezas",100.25,25)]
    
    @classmethod
    def agregar_producto(cls, nombre, precio, cantidad):
        print("--- AGREGAR PRODUCTO ---")
        for producto in cls.lista_productos:
            if nombre.title() == producto.nombre.title():
                return f"El producto {nombre.title()} ya se encuentra registrado."
        
        cls.lista_productos.append(Producto(nombre.title(),precio,cantidad))
        return f"El producto {nombre.title()} fue registrado exitosamente."
    
    @classmethod
    def mostrar_productos(cls):
        print("--- LISTA DE PRODUCTOS ---")
        productos = ""
        for producto in cls.lista_productos:
            productos += f"Producto: {producto.nombre} - Precio: {producto.precio} - Cantidad en Stock: {producto.cantidad}\n"
        return productos

#Lista de productos antes de ser manipulada
print(Inventario.mostrar_productos())
print()

#Aumentar la cantidad de un producto
print(Producto.aumentar_producto("Cepillo dental", 8, Inventario.lista_productos))
print()

#Disminuir la cantidad de un producto
print(Producto.disminuir_producto("arroz", 5, Inventario.lista_productos))
print()

#Agregar un producto
print(Inventario.agregar_producto("Pollo", 58.63, 20 ))
print()

print(Inventario.agregar_producto("papel higiénico", 48.25, 30 ))
print()

#Agregar un producto que ya existe
print(Inventario.agregar_producto("Pollo", 58.63, 20 ))
print()

#Lista de productos despues de ser manipulada
print(Inventario.mostrar_productos())
