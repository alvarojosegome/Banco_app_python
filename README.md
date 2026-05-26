# Análisis del Proyecto – Aplicación Bancaria en Python

## 1. Descripción General del Proyecto

El presente proyecto consiste en el desarrollo de una aplicación bancaria en Python como proyecto final de programación. La aplicación será desarrollada en equipo de dos integrantes y tendrá como finalidad simular el funcionamiento básico de un banco digital mediante una interfaz en consola.

El sistema permitirá administrar usuarios, cuentas bancarias y transacciones, aplicando conceptos fundamentales de Programación Orientada a Objetos (POO), modularización, persistencia de datos y manejo de archivos.

Además, el proyecto será almacenado en un repositorio público de GitHub para facilitar la revisión y evaluación por parte del docente.



# 2. Problemática Identificada

Actualmente, muchas personas utilizan aplicaciones bancarias para realizar operaciones como depósitos, retiros, transferencias y consultas de saldo. Debido a esto, surge la necesidad de desarrollar un sistema que permita simular dichas funcionalidades con el propósito de aplicar conocimientos de programación en un caso práctico y realista.

El proyecto busca resolver la necesidad de crear una aplicación organizada, funcional y segura que permita gestionar operaciones bancarias de manera sencilla desde consola.



# 3. Objetivo General

Desarrollar una aplicación bancaria en Python que permita gestionar usuarios, cuentas y transacciones aplicando Programación Orientada a Objetos, estructuras modulares y almacenamiento de información.



# 4. Objetivos Específicos

* Implementar un sistema de registro e inicio de sesión de usuarios.
* Crear cuentas bancarias de ahorro y corriente.
* Permitir depósitos, retiros y transferencias.
* Registrar el historial de movimientos bancarios.
* Aplicar encapsulamiento, herencia y polimorfismo.
* Organizar el proyecto en módulos y paquetes.
* Mantener el repositorio público en GitHub para revisión.



# 5. Alcance del Proyecto

La aplicación permitirá:

* Registrar usuarios.
* Crear cuentas bancarias.
* Consultar saldo.
* Realizar depósitos.
* Realizar retiros.
* Transferir dinero entre cuentas.
* Visualizar historial de transacciones.
* Bloquear cuentas por intentos fallidos.
* Guardar información mediante archivos JSON.

El sistema funcionará desde consola y estará orientado a fines académicos.



# 6. Requerimientos Funcionales

## Gestión de Usuarios

* Registro de usuarios.
* Inicio de sesión.
* Validación de credenciales.

## Gestión Bancaria

* Creación de cuentas.
* Consulta de saldo.
* Depósitos.
* Retiros.
* Transferencias.

## Seguridad

* Bloqueo de cuenta.
* Validación de datos.
* Protección de atributos mediante encapsulamiento.

## Historial

* Registro de transacciones.
* Consulta de movimientos realizados.



# 7. Requerimientos No Funcionales

* El sistema debe ser organizado y modular.
* El código debe estar documentado.
* El repositorio debe permanecer público.
* El sistema debe ser fácil de usar.
* Debe implementarse utilizando Python.



# 8. Tecnologías Utilizadas

* Lenguaje de programación: Python.
* Programación Orientada a Objetos.
* Archivos JSON para persistencia.
* GitHub para control de versiones.
* Consola como interfaz principal.



# 9. Análisis de Clases

## Clase Usuario

Encargada de almacenar la información personal y credenciales del cliente del banco.

### Atributos

* numero_documento
* nombre_usuario
* celular
* correo
* clave

### Métodos

* iniciar_sesion()
* cerrar_sesion()



## Clase Banco

Administra las cuentas y usuarios registrados.

### Atributos

* id_banco
* usuarios
* cuentas

### Métodos

* registrar_usuario()
* crear_cuenta()
* buscar_cuenta()
* autenticar_usuario()



## Clase CuentaBancaria

Clase principal para las operaciones bancarias.

### Atributos

* numero_cuenta
* saldo
* historial
* estado

### Métodos

* depositar()
* retirar()
* transferir()
* mostrar_historial()



## Clase CuentaAhorro

Hereda de CuentaBancaria y administra cuentas de ahorro.

### Atributos

* tasa_interes

### Métodos

* calcular_interes()



## Clase CuentaCorriente

Hereda de CuentaBancaria y administra cuentas corrientes.

### Atributos

* limite_sobregiro

### Métodos

* validar_sobregiro()



## Clase Transaccion

Registra las operaciones realizadas por el usuario.

### Atributos

* tipo
* monto
* fecha

### Métodos

* registrar()



# 10. Diseño de la Solución

El sistema será desarrollado siguiendo una arquitectura modular, separando cada funcionalidad en diferentes carpetas y archivos.

## Organización del Proyecto


Banco_App/
│
├── data/
│   ├── historial_transacciones.json
│   ├── usuarios.json
|
├── menus/
│   ├── menu_banco.py
│   ├── menu_inicio.py
|
├── modelos/
│   ├── banco.py
│   ├── cuenta.py
│   ├── meta_ahorro.py
│   ├── prestamo.py
|   ├── transacciones.py
|   ├── usuario.py
│
│
├── servicios/
|   ├── persistencia.py
|   ├── validaciones.py
|
├── Diagrama.png
|   
├── main.py
│
└── README.md




# 11. Metodología de Desarrollo

El desarrollo del proyecto se realizará de manera incremental:

1. Diseño de clases.
2. Creación de estructura del proyecto.
3. Implementación de funcionalidades básicas.
4. Validación de operaciones.
5. Persistencia de datos.
6. Pruebas del sistema.
7. Publicación en GitHub.



# 12. Resultados Esperados

Se espera obtener una aplicación funcional capaz de simular operaciones básicas de un banco digital, demostrando el uso correcto de Programación Orientada a Objetos y buenas prácticas de desarrollo de software.



# 13. Conclusión

El proyecto de aplicación bancaria permitirá aplicar conocimientos adquiridos durante el curso de programación, fortaleciendo habilidades en diseño de software, trabajo colaborativo y organización de proyectos reales mediante herramientas como Python y GitHub.
