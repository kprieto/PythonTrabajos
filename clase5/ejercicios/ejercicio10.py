# Ejercicio 10: Buscar y Actualizar la Información en un Diccionario 
# Anidado 
# 1. Crea un diccionario que represente una base de datos de empleados 
# de una empresa. El diccionario debe tener: 
# o nombre_empresa 
# o empleados, que es una lista de diccionarios, donde cada 
# diccionario representa un empleado con: 
# ▪ id_empleado 
# ▪ nombre 
# ▪ departamento 
# ▪ salario 
# 2. Escribe una función que busque y actualice el salario de un 
# empleado dado su id_empleado. La función debe: 
# o Buscar el empleado por su id_empleado. 
# o Actualizar el salario del empleado a un nuevo valor 
# proporcionado. 
# o Imprimir la información del empleado después de la 
# actualización. 

empresa = {
    "nombre": "MAITSOFT",
    "empleados": [{"id_empleado":125, "nombre": "Daniel Juarez", "departamento":"Finanzas", "salario": 2500.00},
                {"id_empleado":126, "nombre": "Martha Sanchez", "departamento":"Administración", "salario": 2800.00},
                {"id_empleado":127, "nombre": "Javier Rubio", "departamento":"Finanzas", "salario": 2500.00},
                {"id_empleado":128, "nombre": "Guadalupe Rivera", "departamento":"Recursos Humanos", "salario": 3500.00},
                {"id_empleado":129, "nombre": "Gustavo López", "departamento":"Administración", "salario": 2800.00},
                {"id_empleado":130, "nombre": "Fabiola Luna", "departamento":"Compras", "salario": 2700.00},                
                {"id_empleado":131, "nombre": "Alberto Gruel", "departamento":"Sistemas", "salario": 3000.00}
                
        
    ]
}

def mostrarDatosEmpresa(empresa):
    print("Datos de la empresa: \n")
    for c, d in empresa.items():
        
        if c == "empleados":
            print("EMPLEADOS \n")
            for empleado in d:
                print("Empleado: ",empleado.get("id_empleado"),"- Nombre: ",empleado.get("nombre"),"- Departamento: ",empleado.get("departamento"),"- Salario: ",empleado.get("salario"),"pesos","\n")
        else:
            print(c, ": ", d," \n")
            
def buscar_Actualizad_Datos_Empleado(id_empleado, empresa):
    for c, d in empresa.items(): 
        if c == "empleados":
            longitud = len(d)
            encontrado = False
            for i in range(longitud):
                idEmpleado = d[i]["id_empleado"]                
                if idEmpleado == id_empleado:
                    encontrado = True
                    actualizar = input(f"¿Desea actualizar el salario del empleado {d[i]["nombre"]}? (s/n): ").lower()
                    if actualizar == "s":
                        salario_nuevo = float(input(f"Introduce el nuevo salario del empleado {d[i]["nombre"]}: "))
                        d[i]["salario"] = salario_nuevo
                        print(f"Se actualizo el nuevo salario a {salario_nuevo} pesos.")
                        print("Empleado: ",d[i]["id_empleado"],"- Nombre: ",d[i]["nombre"],"- Departamento: ",d[i]["departamento"],"- Salario: ",d[i]["salario"],"pesos")
            if encontrado == False:
                print(f"No se encontro ningún empleado con el id {id_empleado}.")
        else:
            print(c,d)

id_empleado = int(input("Introduce el id del empleado: "))

mostrarDatosEmpresa(empresa)
buscar_Actualizad_Datos_Empleado(id_empleado,empresa)

