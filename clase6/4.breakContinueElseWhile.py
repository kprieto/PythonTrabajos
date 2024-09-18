# Programa que pide numero hasta que se ingrese un numero negativo

#Inicializamos la variable suma para acumular la suma de los 
# numeros positivos ingresados.
suma = 0

# Inicializamos un ciclo infinito usando while true
while True:
    #Solicitamos al usuario que introduzca un numero
    # la entrada se convierte en numero entero
    entrada = int(input("introduce un numero (negativo para terminar): "))
    
    # Verificamos si el numero ingresado es negativo
    if entrada < 0:
        # si el numero es negativo, salimos del ciclo usando break
        break
    
    #sumamamos el numero positivo ingresado a la variable suma
    suma += entrada
    
    # verificar si el numero ingresado es par
    if entrada % 2 == 0:
        # Si el numero es par, usamos continue para saltar la impresion
        # y pasar a la siguiente iteracion del ciclo
        continue
    
    # si el numero ingresado no es par (es impar), se ejecuta esta linea:
    print(f"Numero impar ingresado: {entrada}")
    
# else:
#     print(f"El ciclo ha terminado porque se ingreso un numero negativo.")

#Mensaje final
print(f"La suma de los numeros ingresados es: {suma}")