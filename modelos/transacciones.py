from datetime import datetime


class Transaccion:
    def __init__(self, tipo, monto, origen, destino="", fecha=None):
        self.__id_transaccion = id(self)
        self.__tipo = tipo
        self.__monto = monto
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mostrar(self):
        if self.__destino:
            return f"{self.__fecha} {self.__tipo}: ${self.__monto} | De {self.__origen} a {self.__destino}"
        else:
            return f"[{self.__fecha}] {self.__tipo}: ${self.__monto} | Cuenta: {self.__origen}"

    def to_dict(self):
        return {
            "id_transaccion": self.__id_transaccion,
            "tipo": self.__tipo,
            "monto": self.__monto,
            "origen": self.__origen,
            "destino": self.__destino,
            "fecha": self.__fecha,
        }

    def get_id_transaccion(self):
        return self.__id_transaccion

    def get_tipo(self):
        return self.__tipo

    def get_monto(self):
        return self.__monto

    def get_origen(self):
        return self.__origen

    def get_destino(self):
        return self.__destino

    def get_fecha(self):
        return self.__fecha