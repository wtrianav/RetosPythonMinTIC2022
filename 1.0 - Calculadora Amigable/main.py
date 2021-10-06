""" Programa calculadora aritmética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al módulo calculadora_aritmética.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------

import calculadora_aritmetica as calc



#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


#----------Definición de Funciones (Dividir)------------
def menu_operaciones():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("| 4. Calcular división: (4)")
  print("==================================================")
   
  opcion = int(input("¿Cuál es la operación que deseas ejecutar?\n"))
  return opcion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion = menu_operaciones()

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

numero_uno=float(input("Digite el numero 1:\n"))
numero_dos=float(input("Digite el numero 2:\n"))

if operacion==1:
  resultado_suma = calc.sumar_numeros(numero_uno, numero_dos)
  print(f"La suma entre numero 1 y numero 2 es: {resultado_suma}")

elif operacion==2:
  resultado_resta = calc.restar_numeros(numero_uno, numero_dos)
  print(f"La resta entre numero 1 y numero 2 es: {resultado_resta}")

elif operacion==3:
  resultado_multiplicacion = calc.multiplicar_numeros(numero_uno, numero_dos)
  print(f"La multiplicación entre numero 1 y numero 2 es: {resultado_multiplicacion}")

elif operacion==4 and numero_dos !=0:
  resultado_division = calc.dividir_numeros(numero_uno, numero_dos)
  print("La división entre numero 1 y numero 2 es:",round(resultado_division,2),)

else:
  print("El numero 2 no puede ser cero")


