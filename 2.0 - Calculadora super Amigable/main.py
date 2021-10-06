""" Programa calculadora artimética super amigable#
    Realiza las 4 operaciones (+,-,* /)
    dada como entrada una cadena de caracteres 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc
import re

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def parser_cadena(cadena_entrada):
  
  numeros = re.findall(r"\d+\.\d+" ,cadena_entrada)
  if numeros == []:
    numeros = re.findall(r"\d+" ,cadena_entrada)

  numero_uno = float(numeros[0])
  numero_dos = float(numeros[1])

  #TODO: codigo que obtiene los numeros y el operando
  
  return numero_uno, numero_dos

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
#TODO: Leer cadena de entrada
#num_1,num_2,op= parser_cadena(cadena_entrada)
#TODO: terminar programa 
cadena_entrada = str(input("Ingresa la operacion que deseas ejecutar: "))
numero_uno, numero_dos = parser_cadena(cadena_entrada) 

if "+" in cadena_entrada:
  resultado_suma = calc.sumar_numeros(numero_uno, numero_dos)
  print(f"El resultado de la suma es: {resultado_suma}")

elif "-" in cadena_entrada:
  resultado_resta = calc.restar_numeros(numero_uno, numero_dos)
  print(f"El resultado de la resta es: {resultado_resta}")

elif "*" in cadena_entrada:
  resultado_multiplicacion = calc.multiplicar_numeros(numero_uno, numero_dos)
  print(f"El resultado de la multiplicación es: {resultado_multiplicacion}")

elif "/" in cadena_entrada:
  if numero_dos != 0:
    resultado_division = calc.dividir_numeros(numero_uno, numero_dos)
    print(f"El resultado de la división es: {resultado_division}")
  else:
    print("El valor no puede ser cero")

else:
  print("El operador es inválido, solo se permite +, -, *, /")


# Para identificar el tipo de variable, print ( typ(variable)) o algo asi....