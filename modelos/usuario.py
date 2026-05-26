class Usuario:
    def __init__(self, numero_documento, nombre_usuario, celular, correo, clave):
    
        self.__numero_documento = numero_documento
        self.__nombre_usuario = nombre_usuario
        self.__celular = celular
        self.__correo = correo 
        self.__clave = clave
        self.__metas = []
        self.__cuentas = []
        self.__intentos_fallidos = 0
        self.__cuenta_bloqueada = False

    def validar_login(self, clave_ingresada):
        if self.__cuenta_bloqueada:
            print("Cuenta bloqueada por seguridad.")
            return False

        if clave_ingresada == self.__clave:
            self.__intentos_fallidos = 0
            return True
        else:
            self.__intentos_fallidos += 1
            print("Clave incorrecta")

        if self.__intentos_fallidos >= 3:
            self.__cuenta_bloqueada = True
            print("Cuenta bloqueada por demasiados intentos fallidos")

        return False

    def get_numero_documento(self):
        return self.__numero_documento  
    def get_nombre_usuario(self):
        return self.__nombre_usuario  
    def get_celular(self):
        return self.__celular   
    def get_correo(self):
        return self.__correo  
    def get_clave(self):
        return self.__clave 
    def get_metas(self):
        return self.__metas
    def get_cuentas(self):
        return self.__cuentas 
    def get_intentos_fallidos(self):
        return self.__intentos_fallidos  
    def get_cuenta_bloqueada(self):
        return self.__cuenta_bloqueada
        
