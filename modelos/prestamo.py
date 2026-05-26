class Prestamo:
    def __init__(self, monto, interes, cuotas ):
       self.__monto = monto
       self.__interes = interes
       self.__cuotas = cuotas
    
    def calcular_prestamo(self):

        total = self.__monto + (self.__monto * self.__interes / 100)
        cuota_mensual = total / self.__cuotas
    
        print("\n========== SIMULADOR DE PRESTAMO ==========")
        print(f"Monto solicitado : ${self.__monto}")
        print(f"Interes aplicado : {self.__interes}%")
        print(f"Cuotas           : {self.__cuotas}")
        print(f"Total a pagar    : ${total}")
        print(f"Cuota mensual    : ${cuota_mensual:.2f}")
        print("===========================================")
    
    def get_monto(self):
        return self.__monto
    def get_interes(self):
        return self.__interes
    def get_cuotas(self):
        return self.__cuotas
    
    