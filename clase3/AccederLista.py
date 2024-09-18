# Definimos una lista
mi_lista = ["a", "b", "c", "d", "e"]

# Acceso usando indices positivos
primer_elemento = mi_lista[0]
print("Primer elemento de la lista: ",primer_elemento)

segundo_elemento = mi_lista[1]
print("Segundo elemento de la lista: ", segundo_elemento)

# Acceso usuado indices negativos
ultimo_elemento = mi_lista[-1]
print("Ultimo elemento de la lista: ", ultimo_elemento)

penultimo_elemento = mi_lista[-2]
print("Penultimo elemento de la lista: ", penultimo_elemento)

# Acceso a la sublista (Slicing)
print("Sublista (indice 1 a 3): ", mi_lista[1:4])
print("Sublista (indice inicio a 3): ", mi_lista[:3])
print("Sublista (indice 2 a final): ", mi_lista[2:])
print("Sublista (todos): ", mi_lista[0:5])

print("////////////////////////////////////////////")
# Acceso con paso de slicing
print("Sublista con paso 2 ", mi_lista[::2])
print("Sublista con paso 2 en rango (1 a 4)", mi_lista[1:4:2])

# Iteracion a traves de una lista
print("Iteracion a traves de la lista: ")
for elemento in mi_lista:
    print(elemento)

