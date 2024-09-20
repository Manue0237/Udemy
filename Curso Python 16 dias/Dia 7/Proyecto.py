class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_de_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_de_cuenta = numero_de_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_de_cuenta}\nBalance: {self.balance}"

    def Depositar(self, cantidad):
        self.balance += cantidad
        print(f"Depósito exitoso. Nuevo balance: {self.balance}")

    def Retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= cantidad
            print(f"Retiro exitoso. Nuevo balance: {self.balance}")

def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_de_cuenta = input("Ingrese su número de cuenta: ")
    balance_inicial = float(input("Ingrese su balance inicial: "))
    cliente = Cliente(nombre, apellido, numero_de_cuenta, balance_inicial)
    return cliente

def inicio():
    cliente = crear_cliente()
    print("\nBienvenido/a al sistema bancario.\n")
    while True:
        print("¿Qué desea hacer?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == '1':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.Depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.Retirar(cantidad)
        elif opcion == '3':
            print("Gracias por usar el sistema bancario. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        print(f"Balance actual: {cliente.balance}")

inicio()
