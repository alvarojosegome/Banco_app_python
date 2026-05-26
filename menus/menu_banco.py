from servicios.validaciones import cuenta_del_usuario, pedir_clave, pedir_monto
from servicios.persistencia import generador_de_numeros
from modelos.meta_ahorro import Meta_ahorro
from modelos.prestamo import Prestamo
from modelos.cuenta import CuentaAhorro, CuentaCorriente


def menu_banco(banco, usuario):

    while True:
        print("\n==========================================")
        print(f"  Hola, {usuario.get_nombre_usuario()}")
        print("  Que deseas hacer hoy?")
        print("------------------------------------------")
        print("  1. Crear cuenta ahorro")
        print("  2. Crear cuenta corriente")
        print("  3. Transferir")
        print("  4. Depositar")
        print("  5. Retirar")
        print("  6. Ver saldo")
        print("  7. Ver historial")
        print("  8. Crear meta de ahorro")
        print("  9. Ver metas de ahorro.")
        print(" 10. Ahorrar en meta.")
        print(" 11. Simular prestamo.")
        print(" 12. Cerrar sesion. ")
        print("==========================================")

        opcion = input("  Opcion: ")

        if opcion == "1":
            print("\n------------------------------------------")
            titular = usuario.get_nombre_usuario()
            clave = pedir_clave("  Clave de 4 digitos para la cuenta: ")
            numero = generador_de_numeros(banco.get_usuarios(), "ahorro")

            cuenta = CuentaAhorro(
                numero,
                titular,
                clave,
                "ID-" + numero
            )

            usuario.get_cuentas().append(cuenta)
            banco.agregar_cuenta(cuenta)
            print("  Cuenta ahorro creada!")
            print("  Titular:       ", usuario.get_nombre_usuario())
            print("  Numero de cuenta:", numero)

        elif opcion == "2":
            print("\n------------------------------------------")
            clave = pedir_clave("  Clave de 4 digitos para la cuenta: ")
            numero = generador_de_numeros(banco.get_usuarios(), "corriente")

            cuenta = CuentaCorriente(
                numero,
                usuario.get_nombre_usuario(),
                clave,
                "ID-" + numero
            )
            usuario.get_cuentas().append(cuenta)
            banco.agregar_cuenta(cuenta)
            print("  Cuenta corriente creada!")
            print("  Numero de cuenta:", numero)

        elif opcion == "3":
            print("\n------------------------------------------")
            origen_num = input("  Cuenta origen  : ")
            destino_num = input("  Cuenta destino : ")

            origen = banco.buscar_cuenta(origen_num)
            destino = banco.buscar_cuenta(destino_num)

            if origen and destino:
                if not cuenta_del_usuario(origen, usuario):
                    print("  La cuenta de origen no te pertenece")
                else:
                    monto = pedir_monto("  Monto          : ")
                    origen.transferir(destino, monto)
            else:
                print("  Una o ambas de las cuentas no fueron encontradas")

        elif opcion == "4":
            print("\n------------------------------------------")
            numero = input("  Numero de cuenta : ")
            cuenta = banco.buscar_cuenta(numero)
            if cuenta:
                monto = pedir_monto("  Monto a depositar: ")
                cuenta.depositar(monto)
            else:
                print("  Cuenta no encontrada.")
 
        elif opcion == "5":
            print("\n------------------------------------------")
            numero = input("  Numero de cuenta : ")
            cuenta = banco.buscar_cuenta(numero)
            if cuenta:
                monto = pedir_monto("  Monto a retirar  : ")
                cuenta.retirar(monto)
            else:
                print("  Cuenta no encontrada.")
 
        elif opcion == "6":
            print("\n------------------------------------------")
            numero = input("  Numero de cuenta : ")
            cuenta = banco.buscar_cuenta(numero)
            if cuenta:
                print(f"  Saldo actual: ${cuenta.get_saldo()}")
            else:
                print("  Cuenta no encontrada.")
 
        elif opcion == "7":
            print("\n------------------------------------------")
            numero = input("  Numero de cuenta : ")
            cuenta = banco.buscar_cuenta(numero)
            if cuenta:
                cuenta.mostrar_historial()
            else:
                print("  Cuenta no encontrada.")
 
        elif opcion == "8":

            nombre_meta = input("Nombre de la meta: ")
            objetivo = pedir_monto("Monto objetivo: ")

            meta = Meta_ahorro(nombre_meta, objetivo)
            usuario.get_metas().append(meta)

            print("Meta creada exitosamente")

        elif opcion == "9":

            if len(usuario.get_metas()) == 0:
                print("No tienes metas registradas")

            else:
                for meta in usuario.get_metas():
                    meta.mostrar_progreso()

        elif opcion == "10":

            if len(usuario.get_metas()) == 0:
                print("No tienes metas registradas")

            else:
                nombre = input("Nombre de la meta: ")

                encontrada = False

                for meta in usuario.get_metas():

                    if meta.get_nombre().lower() == nombre.lower():
                        monto = pedir_monto("Monto a ahorrar: ")
                        meta.ahorrar(monto)
                        print("Dinero agregado correctamente")
                        encontrada = True
                        break

                if not encontrada:
                    print("Meta no encontrada")

        elif opcion == "11":

            monto = pedir_monto("Monto del prestamo: ")
            interes = pedir_monto("Interes (%): ")
            
            try:
                cuotas = int(input("Numero de cuotas: "))
                if cuotas <= 0:
                    raise ValueError
            except ValueError:
                print(" Numero de cuotas invalido.")
            else:
                prestamo = Prestamo(monto, interes, cuotas)
                prestamo.calcular_prestamo()

        elif opcion == "12":
            print(f"Hasta pronto, {usuario.get_nombre_usuario()}")
            break

        else:
            print("Opcion invalida")