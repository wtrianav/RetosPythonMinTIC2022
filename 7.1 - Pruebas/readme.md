# Billetera
He tenido la percepción de que no manejo bien el dinero que traigo en mi billetera. Por lo tanto, he desarrollado una pequeña aplicación que me permite registrar cuando ingreso o saco dinero de la misma y así poder validar que el dinero coincida con lo que el programa reporta.

# Requisitos de software
Vamos a probar los siguientes requisitos funcionales
  

| Código                | RS-01                                                        |
|-----------------------|-------------------------------------------------------------|
| Propósito             | Crear una billetera vacía                                   |
| Parámetros de entrada | Ninguno                                                     |
| Valores de retorno    | Una billetera  inicializada con efectivo y monedas en cero  |
| Firma                 | ``def crear_billetera()``                                       |

| Código                | RS-02                                                               |
|-----------------------|---------------------------------------------------------------------|
| Propósito             | Ingresar dinero en efectivo a la billetera                          |
| Parámetros de entrada | billetera  
||  total efectivo a ingresar                  |
| Valores de retorno    | El saldo de la billetera se actualiza sumando el efectivo ingresado |
| Firma                 | ingresar_efectivo(billetera,efectivo)                               |


| Código                | RS-03                                                                                                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Propósito             | Retirar dinero en efectivo a la billetera                                                                                                                                                                                                                          |
| Parámetros de entrada | billetera
||total efectivo a retirar                                                                                                                                                                                                                      |
| Valores de retorno    | caso 1: Si tiene efectivo suficiente: el saldo de la billetera se actualiza restando el efectivo ingresado 
||caso 2: Si tiene menos efectivo: el saldo queda en cero y se retira el dinero que tenía 
||caso 3: No tiene dinero: se debe generar una excepción un error |
| Firma                 | def retirar_efectivo(billetera,efectivo)     


# Casos de prueba
Vamos a diseñar los casos de prueba para cada Requisito

| Identificación       | CP-RS01-01  |
|----------------------|---|
| Descripción          |Crear un nueva billetera sin dinero   |
| Precondiciones       |   Ninguna|
| Valores de entrada   | Ninguno  |
| Resultados esperados |  Se crea una nueva billetera sin dinero |

| Identificación       | CP-RS02-01  |
|----------------------|---|
| Descripción          |Ingresa dinero a una billetera sin dinero  |
| Precondiciones       | el dinero en la billetera es $0 |
| Valores de entrada   | se ingresan $100.000 a la billetera  |
| Resultados esperados | El saldo en la billetera es $100.000 |


| Identificación       | CP-RS02--02  |
|----------------------|---|
| Descripción          |Ingresa dinero a una billetera con dinero  |
| Precondiciones       | el dinero en la billetera es $500.000 |
| Valores de entrada   | se ingresan $80.000  a la billetera|
| Resultados esperados | El saldo en la billetera es $580.000 |

| Identificación       | CP-RS03-01  |
|----------------------|---|
| Descripción          |Retirar menos dinero que el efectivo en la billetera    |
| Precondiciones       | el dinero en la billetera es $400.000 |
| Valores de entrada   | valor a retirar $120.000  |
| Resultados esperados | El saldo en la billetera es $280.000 y el valor retirado es $120.000 |

| Identificación       | CP-RS03-02  |
|----------------------|---|
| Descripción          |Retirar mas dinero que el efectivo en la billetera    |
| Precondiciones       | el dinero en la billetera es $200.000 |
| Valores de entrada   | valor a retirar 300.000  |
| Resultados esperados | El saldo en la billetera es $0 y el valor retirado es $200.000 |

| Identificación       | CP-RS03-03  |
|----------------------|---|
| Descripción          |Retirar  dinero sin efectivo en la billetera    |
| Precondiciones       | el dinero en la billetera es $0 |
| Valores de entrada   | valor a retirar 300.000  |
| Resultados esperados | El saldo en la billetera es $0 y el valor retirado es $200.000 |
# ¿Que debo hacer?
*   Lo primero es editar y analizar las pruebas ya implementadas, luego ejecutarlas y hacer algunos cambios en las funciones para que genere valores no válidos y no pase algunas de las pruebas.

*  Completar el programa implementando las funciones que:
   *   manejen el ingreso y retiro de monedas
   *   Retorne el saldo de dinero total en la billetera
   *   Implementar una función retiro general que al dar una cantidad a retirar permita el manejo de efectivo y monedas en caso de que no alcance con el efectivo en a billetera

* Diseñar e Implementar los casos de prueba para estas nuevas funciones


