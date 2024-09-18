# 3. Ejercicio con range, enumerate, y break/continue 
# Escribe un programa que: 
# 1. Itere sobre una lista de cadenas usando enumerate para mostrar el 
# índice y el valor. 
# 2. Utilice continue para saltar cadenas vacías. 
# 3. Utilice break para detener la iteración si se encuentra una cadena 
# con más de 5 caracteres.

def cadenas(lista_cadenas):

    for clave,cadena in enumerate(lista_cadenas):
        
        if len(cadena) == 0:
            continue
        if len(cadena) > 5:
            break
        else:
            print(f"Clave: {clave} - Cadena: {cadena} - Caracteres: {len(cadena)}")
            
cadenas(["Hola","","" "Mundo"," ","!","Programador","Python"," ",""])