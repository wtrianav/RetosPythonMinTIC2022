""" Modulo para la codificación y decodificación de
    mensajes con la técnica saltando al 5
    Oscar Franco-Bedoya
    Mayo 20-2021 """

#=======================================================
# E S P A C I O    D E    T R A B A J O     A L U M N O
# ======================================================

#----------Definición de Funciones (Dividir)------------

codigo = {"1":"9", "9":"1","2":"8","8":"2","3":"7","7":"3","4":"6","6":"4","5":"0","0":"5"}

def codificar_mensaje(mensaje_original):
  mensaje_codificado = ""
  for n in mensaje_original:
    if n in codigo:
      mensaje_codificado = mensaje_codificado+codigo[n]
    else:
      mensaje_codificado = mensaje_codificado + n

  return mensaje_codificado

def decodificar_mensaje(mensaje_codificado):
  mensaje_codificado1 = ""
  for n in mensaje_codificado:
    if n in codigo:
      mensaje_codificado1 = mensaje_codificado1 + codigo[n]
    else:
      mensaje_codificado1 = mensaje_codificado1 + n
      
  return mensaje_codificado1
