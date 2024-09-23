# 8. Sistema de Cuentas Bancarias 
# o Crea una clase CuentaBancaria con atributos como titular y 
# saldo. Implementa métodos para depositar y retirar dinero, y 
# asegúrate de manejar excepciones si se intenta retirar más de 
# lo que hay en la cuenta. Luego, crea una clase Banco que 
# maneje múltiples cuentas. 

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    #Permite hacer un deposito
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"El deposito $ {monto} fue realizado exitosamente. Nuevo saldo: $ {self.saldo}"
        return "El monto deber ser mayor a 0 "
    
    #Permite realizar un retiro
    def retirar(self, saldo_retirar):
        if saldo_retirar > self.saldo:
            raise ValueError (f"No puedes retirar el saldo de $ {saldo_retirar} de la cuenta, sobrepasa el Saldo Actual: $ {self.saldo}")
        else:
            self.saldo -= saldo_retirar
            return f"Se retiro la cantidad $ {saldo_retirar}. Nuevo saldo: $ {self.saldo}"

class Banco:
    
    def __init__(self):
        self.cuentas = []

    #Permite crear una cuenta bancaria
    def crear_cuenta(self, titular, saldo_inicial=0):
        print("--- CREAR CUENTA ---")
        nueva_cuenta = CuentaBancaria(titular, saldo_inicial)
        self.cuentas.append(nueva_cuenta)
        return "Cuenta creada exitosamente."

    #Permite buscar una cuenta bancaria por nombre
    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                return cuenta
        return None

    #Permite hacer el deposito a una cuenta bancaria
    def depositar_en_cuenta(self, titular, monto):
        cuenta = self.buscar_cuenta(titular)
        if cuenta:
            return cuenta.depositar(monto)
        else:
            return "Cuenta no encontrada."

    #Permite hacer el retiro a una cuenta bancaria
    def retirar_de_cuenta(self, titular, monto):
        cuenta = self.buscar_cuenta(titular)
        if cuenta:
            try:
                return cuenta.retirar(monto)
            except ValueError as e:
                return e
        else:
            return "Cuenta no encontrada."

# Ejemplo de uso
banco = Banco()
#Crear cuentas de bancarias
print(banco.crear_cuenta("Juan Pérez", 1000))
print()
print(banco.crear_cuenta("María López", 500))
print()

#Crear un deposito a una cuenta
print("--- DEPOSITAR A CUENTA ---")
print(banco.depositar_en_cuenta("Juan Pérez", 200))
print()

#Crear un deposito a una cuenta no encontrada
print("--- DEPOSITAR A CUENTA ---")
print(banco.depositar_en_cuenta("Lorena Rojas", 300))
print()

#Retirar un saldo a una cuenta
print("--- RETIRAR A CUENTA ---")
print(banco.retirar_de_cuenta("María López", 200))  
print()

#Retirar un saldo a una cuenta que se sobrepasa
print("--- RETIRAR A CUENTA ---")
print(banco.retirar_de_cuenta("Juan Pérez", 1300))  
print()

#Retirar un saldo a una cuenta no encontrada
print("--- RETIRAR A CUENTA ---")
try:
    print(banco.retirar_de_cuenta("Pedro Gómez", 100))  
except ValueError as e:
    print(e)
    