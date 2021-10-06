""" Modulo calculadora artimética #
    Realiza las 4 operaciones (+,-,* /) 
    Oscar Franco-Bedoya
    Mayo 3-2021 """
# Definición de Funciones
def sumar_numeros(numero_uno, numero_dos):
  """ 
  Parameters
  ----------
  numero_uno:float
     operando uno para la suma
  numero_dos:float
     operando dos para la suma
  Returns
  -------
  suma:float
    el resultado de la suma     
  """  
  suma=numero_uno+numero_dos
  return suma

# completa las demás operaciones
def restar_numeros(numero_uno, numero_dos):
  """   
  Parameters
  ----------
  numero_uno:float
     operando uno para la rest
  numero_dos:float
     operando dos para la resta
  Returns
  -------
  resta:float
    el resultado de la resta     
  """ 
  resta=numero_uno-numero_dos
  return resta 

def multiplicar_numeros(numero_uno, numero_dos):
  """   
  Parameters
  ----------
  numero_uno:float
     operando uno para la multiplicación
  numero_dos:float
     operando dos para la multiplicación
  Returns
  -------
  resta:float
    el resultado de la multiplicación 
  """ 
  multiplicacion=numero_uno*numero_dos
  return multiplicacion

def dividir_numeros(numero_uno, numero_dos):
  """   
  Parameters
  ----------
  numero_uno:float
     operando uno para la división
  numero_dos:float
     operando dos para la division
  Returns
  -------
  resta:float
    el resultado de la division 
  """ 
  division= numero_uno/numero_dos
  return division