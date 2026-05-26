import json
import os

from modelos.usuario import Usuario
from modelos.transacciones import Transaccion
from modelos.cuenta import CuentaAhorro, CuentaCorriente
 
ARCHIVO_USUARIOS = "data/usuarios.json"
ARCHIVO_TRANSACCIONES = "data/historial_transacciones.json"


def guardar_usuarios(usuarios):

    datos = []
    for u in usuarios:
        cuentas_guardadas = []
        for c in u.get_cuentas():
            tipo = "ahorro" if isinstance(c, CuentaAhorro) else "corriente"
            historial_guardado = [t.to_dict() for t in c.get_historial()]
            cuentas_guardadas.append({
                "tipo":          tipo,
                "numero_cuenta": c.get_numero_cuenta(),
                "titular":       c.get_titular(),
                "clave":         c.get_clave(),
                "saldo":         c.get_saldo(),
                "historial":     historial_guardado
            })
        datos.append({
            "numero_documento": u.get_numero_documento(),
            "nombre_usuario":   u.get_nombre_usuario(),
            "celular":          u.get_celular(),
            "correo":           u.get_correo(),
            "clave":            u.get_clave(),
            "cuentas":          cuentas_guardadas
        })
    os.makedirs(os.path.dirname(ARCHIVO_USUARIOS), exist_ok=True)
    with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
 
def cargar_usuarios():
    if not os.path.exists(ARCHIVO_USUARIOS):
        return []
    with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as f:
        datos = json.load(f)
    usuarios = []
    for d in datos:
        u = Usuario(

            d["numero_documento"], 
            d["nombre_usuario"], 
            d["celular"], 
            d["correo"], 
            d["clave"]
        )
        
        for c in d.get("cuentas", []):
            if c["tipo"] == "ahorro":
                cuenta = CuentaAhorro(

                    c["numero_cuenta"], 
                    c["titular"], 
                    c["clave"], "ID-" + c["numero_cuenta"])
            else:
                cuenta = CuentaCorriente(

                    c["numero_cuenta"], 
                    c["titular"], 
                    c["clave"], "ID-" + c["numero_cuenta"])
                
            cuenta.set_saldo(c.get("saldo", 0))
            for t in c.get("historial", []):
                cuenta.get_historial().append(Transaccion(

                    t.get("tipo"),
                    t.get("monto"),
                    t.get("origen"),
                    t.get("destino", "")
                ))
            u.get_cuentas().append(cuenta)
        usuarios.append(u)
    return usuarios

def guardar_transacciones(transacciones):
    datos = [t.to_dict() for t in transacciones]
    os.makedirs(os.path.dirname(ARCHIVO_TRANSACCIONES), exist_ok=True)
    with open(ARCHIVO_TRANSACCIONES, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


guardar_transacciones = guardar_transacciones


def cargar_transacciones():
    if not os.path.exists(ARCHIVO_TRANSACCIONES):
        return []

    with open(ARCHIVO_TRANSACCIONES, "r", encoding="utf-8") as f:
        datos = json.load(f)

    transacciones = []
    for t in datos:
        transacciones.append(Transaccion(
            t.get("tipo"),
            t.get("monto"),
            t.get("origen"),
            t.get("destino", ""),
            t.get("fecha")
        ))
    return transacciones


# generador de numero de cuentas

def generador_de_numeros(usuarios, tipo):
    if tipo == "ahorro":
       base = 4600000001
    else:
        base = 2200000001

    maximo = base - 1
    for usuario in usuarios:
        for cuenta in usuario.get_cuentas():
            if isinstance(cuenta, CuentaAhorro) and tipo == "ahorro":
                try:
                    numero = int(cuenta.get_numero_cuenta())
                    if numero > maximo:
                        maximo = numero 
                except (ValueError, TypeError):
                    continue
            elif isinstance(cuenta, CuentaCorriente) and tipo == "corriente":
                try:
                    numero = int(cuenta.get_numero_cuenta())
                    if numero > maximo:
                        maximo = numero 
                except (ValueError, TypeError):
                    continue
    return str(maximo + 1)
