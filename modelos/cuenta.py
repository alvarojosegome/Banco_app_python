from modelos.transacciones import Transaccion

class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, clave):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__clave = clave
        self.__saldo = 0
        self.__historial = []



    def depositar(self, monto):
        self.__saldo += monto
        self.__historial.append(Transaccion("Deposito", monto, self.__numero_cuenta))
        print("Depósito exitoso. Saldo actual: $", self.__saldo)


    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            self.__historial.append(Transaccion("Retiro", monto, self.__numero_cuenta))
            print("Retiro exitoso. Saldo actual: $", self.__saldo)
        else:
            print("Saldo insuficiente. Su saldo  es: $", self.__saldo)

    def transferir( self, destino, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            destino.set_saldo(destino.get_saldo() + monto)

            self.__historial.append(
                Transaccion("Transferencia enviada", monto, self.__numero_cuenta, destino.get_numero_cuenta())
            )

            destino.get_historial().append(
                Transaccion("Transferencia recibida", monto, self.__numero_cuenta, destino.get_numero_cuenta())
            )

            print("Transferencia exitosa")
        else:
            print("Saldo insuficiente")


    def mostrar_historial(self):
        if len(self.__historial) == 0:
            print("Sin movimientos")
        else:
            for t in self.__historial:
                print(t.mostrar())


    def get_numero_cuenta(self):
            return self.__numero_cuenta
    def get_titular(self):
            return self.__titular
    def get_clave(self):
         return self.__clave
    def get_saldo(self):
            return self.__saldo
    def set_saldo(self, valor):
         self.__saldo = valor     
    def get_historial(self):
            return self.__historial

class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta,  titular, clave, id_cuenta_ahorro):
        super().__init__(numero_cuenta, titular, clave)
        self.id_cuenta_ahorro = id_cuenta_ahorro

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, clave, id_cuenta_corriente):
        super().__init__(numero_cuenta, titular, clave)
        self.id_cuenta_corriente = id_cuenta_corriente
