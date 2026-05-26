def pedir_documento(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and len(valor) > 0:
            return valor
        print("  El documento solo debe contener numeros.")
 
def pedir_clave(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and len(valor) == 4:
            return valor
        print("  La clave debe ser exactamente 4 digitos numericos.")
 
def pedir_solo_texto(mensaje):
    while True:
        valor = input(mensaje)
        if valor.replace(" ", "").isalpha() and len(valor) > 0:
            return valor
        print("  Solo se aceptan letras.")


def pedir_celular(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and len(valor) == 10:
            return valor
        print("  El celular debe tener exactamente 10 digitos numericos.")
 
def pedir_correo(mensaje):
    while True:
        valor = input(mensaje)
        if "@" in valor and "." in valor and len(valor) > 5:
            return valor
        print("  Ingrese un correo valido (ejemplo: nombre@correo.com).")

def cuenta_del_usuario(cuenta, usuario):
    return any(c.get_numero_cuenta() == cuenta.get_numero_cuenta() for c in usuario.get_cuentas())

def pedir_monto(mensaje):
    while True:
        try:
            valor_str = input(mensaje)
            valor = float(valor_str)
            if valor > 0:
                return valor
            print("  El monto debe ser mayor a cero.")
        except ValueError:
            print("  Ingrese un numero valido.")