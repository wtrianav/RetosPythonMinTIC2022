""" Modulo para el manejo de datos de dispositivos IoT 
    Oscar Franco-Bedoya
    Mayo 20-2021 """

#================================================================
#     E S P A C I O    D E    T R A B A J O     A L U M N O
# ===============================================================

#----------Definición de Funciones (Dividir)------------
from collections import namedtuple

def separar_cadenas(dispositivos_hogar):  
  dispositivos_hogar = dispositivos_hogar.split('@',-1)
  
  print(dispositivos_hogar)
  
  IoT = namedtuple('IoT', ['tipo_dispositivo', 'identificador', 'estado'])
  for n in dispositivos_hogar:
    n = n.split(",",-1)
    IoT = tuple(n)
    print(IoT)
  return dispositivos_hogar


def calcular_estadisticas(lista_IoT):
  contON = 0
  contOFF = 0
  for n in lista_IoT:
    n = n.split(",",-1)
    if n[2] == "ON":
      contON = contON + 1
    else:
      contOFF = contOFF + 1
  
  contadorON = (f"Dispositivos encendidos (ON): {contON}")
  contadorOFF = (f"Dispositivos apagados (OFF): {contOFF}")

  return contadorON, contadorOFF
