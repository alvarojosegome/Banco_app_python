class Banco:
    def __init__(self, id_banco):
        self.__id_banco = id_banco
        self.__cuentas = [] 
        self.__usuarios = []

    def agregar_cuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def buscar_cuenta(self, numero):
        for cuenta in self.__cuentas:
            if cuenta.get_numero_cuenta() == numero:
                return cuenta
        return None
    
    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        for cuenta in usuario.get_cuentas():
            self.__cuentas.append(cuenta)

    def buscar_usuario(self, numero_documento):
        for u in self.__usuarios:
            if u.get_numero_documento() == numero_documento:
                return u
        return None
    
    def get_id_banco(self):
        return self.__id_banco
    def get_cuentas(self):
        return self.__cuentas
    def get_usuarios(self):
        return self.__usuarios