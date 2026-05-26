from modelos.usuario import Usuario
from modelos.banco import Banco

from menus.menu_banco import menu_banco

from servicios.validaciones import pedir_documento, pedir_solo_texto, pedir_celular, pedir_correo, pedir_clave

from servicios.persistencia import cargar_usuarios, guardar_usuarios


def login(banco):
    print("\n==========================================")
    print("\n==========================================")
    print("      BANCO PICHINCHA - Iniciar sesion   ")
    print("==========================================")
    documento = pedir_documento("  Documento : ")
    clave      = pedir_clave("  Clave     : ")
    print("==========================================")
     
    usuario = banco.buscar_usuario(documento)
 
    if usuario and usuario.validar_login(clave):
        print(f"\n  Bienvenido/a, {usuario.get_nombre_usuario()}!")
        return usuario
    else:
        print("\n  Documento o clave incorrectos.")
        return None



def registrar_usuario(banco):
    print("\n==========================================")
    print("      BANCO PICHINCHA - Registro         ")
    print("==========================================")
    
    documento = pedir_documento("  Documento     : ")
    
    if banco.buscar_usuario(documento):
       print("\n  Ya existe un usuario con ese documento.")
       return
    
    nombre  = pedir_solo_texto("  Nombre        : ")
    celular = pedir_celular("  Celular       : ")
    correo  = pedir_correo("  Correo        : ")
    clave   = pedir_clave("  Clave         : ")
    print("==========================================")
    
    usuario = Usuario(documento, nombre, celular, correo, clave)
    banco.agregar_usuario(usuario)
    guardar_usuarios(banco.get_usuarios())
    print("  Usuario registrado correctamente.")

 
def menu_inicio():
    banco = Banco(1)
    usuarios_cargados = cargar_usuarios()
    if usuarios_cargados:
        for usuario in usuarios_cargados:
            banco.agregar_usuario(usuario)
 
    while True:
        print("\n==========================================")
        print("        BANCO PICHINCHA                  ")
        print("==========================================")
        print("  1. Iniciar sesion")
        print("  2. Registrarse")
        print("  3. Salir")
        print("==========================================")
 
        opcion = input("  Opcion: ")
 
        if opcion == "1":
            usuario = login(banco)
            if usuario:
                menu_banco(banco, usuario)
 
        elif opcion == "2":
            registrar_usuario(banco)
 
        elif opcion == "3":
            print("\n  Gracias por preferirnos. Hasta pronto!")
            break
 
        else:
            print("  Opcion invalida.")

