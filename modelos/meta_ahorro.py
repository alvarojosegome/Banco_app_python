
class Meta_ahorro:
    def __init__(self, nombre, objetivo):
        self.__nombre_meta = nombre 
        self.__objetivo = objetivo
        self.__ahorrado = 0
    
    def ahorrar(self, monto):
        self.__ahorrado += monto
    
    def mostrar_progreso(self):
        faltante = self.__objetivo - self.__ahorrado
        if self.__objetivo == 0:
            porcentaje = 0.0
        else:
            porcentaje = (self.__ahorrado / self.__objetivo) * 100

        print("\n============== META DE AHORRO ==============") 
        print(f"Meta              : {self.__nombre_meta}")
        print(f"Objetivo          : {self.__objetivo}")
        print(f"Dinero ahorrado   : {self.__ahorrado}")
        print(f"Dinero faltante   : {faltante}")
        print(f"Completado        : {porcentaje:.2f}%")
        print("==============================================")


    def get_nombre(self):
        return self.__nombre_meta
    
    def get_objetivo(self):
        return self.__objetivo
    
    def get_ahorrado(self):
        return self.__ahorrado

