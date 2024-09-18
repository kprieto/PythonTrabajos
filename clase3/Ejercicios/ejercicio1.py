lista_compras = []
salir = True

while salir:
    articulo = input("Ingrese un artículo para la lista de compras (o 'done' para finalizar): ").lower()
    
    if articulo != "done":
        lista_compras.append(articulo)
        print("Artículos añadidos a la lista de compras. ", lista_compras)
        eliminar = input("¿Desea eliminar el último artículo añadido? (s/n): ").lower()
        if eliminar == "s" and len(lista_compras) != 0:
            articulo_eliminado = lista_compras.pop()
            print(f"El artículo {articulo_eliminado} fue eliminado.")   
        
    
    if articulo == "done":
        salir = False

print("Lista de compras final:", lista_compras)
    