#Cuenta Bancaria

class Persona:
    def __init__(self, nombre:str, documento:str):
        self.nombre = nombre
        self.documento = documento
    
    def __str__(self) -> str:
        return f"{self.nombre}, se creo esta persona con documento {self.documento}"

class CuentaBancaria:
    def __init__(self, titular: Persona, saldo: int = 0):
        self.titular = titular
        self._saldo = saldo #saldo privado
    
    def saldo(self) -> int:
        return self.saldo
    
    def depositar(self, monto: float) -> None:
        if monto > 0:
            self._saldo += monto
            print(f"Se deposito {monto} y el saldo actual es {self._saldo}")
        else:
            print("El monto es invalido")

    def retirar(self, monto: float) -> None:
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"se retiro {monto} y su saldo actual es {self._saldo}")
        else:
            print("No puede retirar un monto mayor al saldo")

    def __str__(self) -> str:
        return f"Cuenta de {self.titular.nombre}, documento {self.titular.documento}, saldo {self._saldo}"
    
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo = 0, interes: float = 0.02):
        super().__init__(titular, saldo)
        self.interes = interes

    def calcular_interes(self):
        ganancia = self._saldo * self.interes
        self._saldo += ganancia
        print(f"interes aplicado su saldo es {self._saldo}")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo = 0, limite_sobregiro: float = 500):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro
    
    def retirar(self, monto: float):
        if monto <= self._saldo + self.limite_sobregiro:
            self._saldo -= monto
            print(f"se retiro {monto} y su saldo actual es {self._saldo}")
        else:
            print("No puede retirar un monto mayor al saldo")

class Banco:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cuentas = []
    
    def crear_cuenta(self, titular: Persona, tipo = "ahorros" ) -> list:
        if tipo == "ahorros":
            cuenta = CuentaAhorro(titular)
        elif tipo == "corriente":
            cuenta = CuentaCorriente(titular)
        else:
            print("Cuenta invalida")
            return None
        self.cuentas.append(cuenta)# aca se guardaran las cuentas
        print(f"Cuenta bancaria {tipo} para {titular.nombre}")
        return cuenta
    
    def mostrar_cuentas(self):
        if not self.cuentas:
            print("No hay cuentas registradas")
        else:
            for i, cuenta in enumerate(self.cuentas, 1):
                print(f"{i}.{cuenta}")

banco = Banco("x")

while True:
    print("---MENU---")
    print("1. Crear una persona y cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Aplicar intereses (Cuenta De Ahorros)")
    print("5. Mostrar cuentas")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        documento = input("Ingrese su documento: ")
        persona = Persona(nombre=nombre, documento=documento)

        print("Tipo de cuenta")
        tipo = input("Ahorros o Corriente: ").lower()
        cuenta = banco.crear_cuenta(persona,tipo)
    
    elif opcion == "2":
        if not banco.cuentas:
            print("No hay cuentas registradas")
        else:
            for i, cuenta in enumerate(banco.cuentas, 1):
                print(f"{i}.{cuenta}")
            
            indice = int(input("Seleccione el numero de cuenta: ")) - 1
            monto = float(input("Ingrese el monto a depositar: "))

            banco.cuentas[indice].depositar(monto)

    elif opcion == "3":
        if not banco.cuentas:
            print("No hay cuentas registradas")
        else:
            for i, cuenta in enumerate(banco.cuentas, 1):
                print(f"{i}.{cuenta}")
            
            indice = int(input("Seleccione el numero de cuenta: ")) - 1
            monto = float(input("Ingrese el monto a retirar: "))

            banco.cuentas[indice].retirar(monto)
    
    elif opcion == "4":
        if not banco.cuentas:
            print("No hay cuentas registradas")
        else:
            for i, cuenta in enumerate(banco.cuentas, 1):
                print(f"{i}.{cuenta}")
            
            indice = int(input("Seleccione el numero de cuenta: ")) - 1
            cuenta = banco.cuentas[indice]

            if isinstance(cuenta, CuentaAhorro):
                cuenta.calcular_interes()
            else:
                print("La cuenta selecciona no es de ahorros")
              
    elif opcion == "5":
        if not banco.cuentas:
            print("No hay cuentas registradas")
        else:
            print("--LISTA DE CUENTAS--")
            for i, cuenta in enumerate(banco.cuentas, 1):
                print(f"{i}.{cuenta}")
            
    elif opcion == "6":
        print("Finalizando operacion")
        break
    else:
        print("Opcion invalida")
    