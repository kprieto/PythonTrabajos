# 9. Sistema de Compras 
# o Crea una clase Producto que contenga nombre, precio, y 
# cantidad. Luego, crea una clase Carrito que permita añadir 
# productos, calcular el total y aplicar descuentos. Implementa 
# métodos de clase para manejar descuentos generales en 
# productos.

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
class Carrito:
    def __init__(self):
        self.lista_productos = [Producto("Jabón", 25.50, 10),
                    Producto("Shampoo", 45.00, 5),
                    Producto("Pasta dental", 30.00, 15),
                    Producto("Papel higiénico", 25.50, 10),
                    Producto("Cepillo dental", 35.50, 10)]
        self.carrito_compra = {}
        
    #Permite validar la disponibilidad de un producto    
    def validar_disponibilidad(self,producto):
        cantidad = int(input(f"¿Cuántos(as) {producto} quieres?: "))
        for prod in self.lista_productos:
            if prod.nombre == producto:
                if cantidad > prod.cantidad:
                    print(f"La cantidad supera la disponibilidad ({prod.cantidad}) del producto.")
                    return self.validar_disponibilidad(producto)
                elif cantidad < 0:
                    print(f"Ya no hay {producto} disponibles.")
                    return 0
        return cantidad
    
    #Permite aplicar el descuento a los productos
    def aplicar_descuento(self, porcentaje_descuento, precio):
        if 0 < porcentaje_descuento < 100:
            descuento = precio * (porcentaje_descuento / 100)
            precio -= descuento            
            return precio
        else:
            print("Porcentaje de descuento inválido. Debe ser mayor que 0 y menor que 100.")
            return 0
        
    #Permite agregar un producto al carrito de compra        
    def añadir_producto(self):
        #Permite al usuario elegir el producto que quiere agregar al carrito de compra
        print("Elige una producto del menú para tu carrito de compra: ")
        i = 1
        for prod in self.lista_productos:
            print(f"{i}) {prod.nombre} - Precio: ${prod.precio} - Disponible: {prod.cantidad} ")
            i += 1
        producto = int(input("Agregar: ")) 

        #Permite obtener el nombre y el precio del producto seleccionado
        i = 1
        precio = 0
        for prod in self.lista_productos:
            if producto == i:
                producto = prod.nombre
                precio = prod.precio
            i += 1   
        cantidad = self.validar_disponibilidad(producto)
        
        #Disminuye la disponibilidad del producto 
        i = 1
        for prod in self.lista_productos:
            if prod.nombre ==  producto:
                prod.cantidad -= cantidad
            i += 1  
        
        #Verifica si el producto ya fue agregado al carrito de compra
        #para aumentar la cantidad de productos    
        if producto in self.carrito_compra:
            self.carrito_compra[producto]["cantidad"] += cantidad            
        else:
            self.carrito_compra[producto]={"precio":precio,"cantidad":cantidad}
        cesta = f"Agregaste {cantidad} {producto} - ${precio} c/u "
        return cesta
    
    #Permite mostrar la lista de productos agregados al carrito de compra
    def mostrar_carrito(self):
        print("--- CARRITO DE COMPRA ---")
        for producto in self.carrito_compra:
            print(f"({self.carrito_compra[producto]["cantidad"]}) {producto}  precio ${self.carrito_compra[producto]["precio"]}")
    
    #Permite pagar todos los productos agregados al carrito de compra y aplicar un descuento si quiere el usuario
    def pagar_carrito(self):
        print("--- PAGAR CARRITO DE COMPRA ---")
        cobro = 0.0
        respuesta = input("¿Quieres aplicar el descuento del 20% a sus productos? S/N: ").upper()
        descuento = 0.0     
            
        print("--- PRODUCTOS ---")
        for productos in self.carrito_compra:            
            cobro += self.carrito_compra[productos]["precio"] * self.carrito_compra[productos]["cantidad"]
            if respuesta == "S":
                descuento = self.aplicar_descuento(20,cobro)
                print(f"{productos} {self.carrito_compra[productos]["cantidad"]} x ${self.carrito_compra[productos]["precio"]} = ${descuento} con descuento 20%")
            else:
                print(f"{productos} {self.carrito_compra[productos]["cantidad"]} x ${self.carrito_compra[productos]["precio"]} = ${self.carrito_compra[productos]["cantidad"] * self.carrito_compra[productos]["precio"] }")
        self.carrito_compra = {}
        return f"Se pagó un total de ${cobro} por la compra. Gracias por comprar."

carrito = Carrito()

#Permite agregar varios productos, mostrar los productos y pagar los productos del carrito de compras
while True:
    opcion = int(input("¿Quieres 1) Agregar productos 2) Mostrar carrito compra 3) Pagar carrito compras?: "))
    if opcion == 1:        
        #Agregar productos al carrito de compras
        print(carrito.añadir_producto())    
        print()
    elif opcion == 2:
        #Mostrar la lista del carrito de compras
        carrito.mostrar_carrito()
        print()
    else:
        #Pagar los productos guardados en el carrito de compras
        print(carrito.pagar_carrito())
        break
        
