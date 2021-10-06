""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    Oscar Franco-Bedoya
    Mayo 10-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(distancia_uno, distancia_dos,tiempo):
  #TODO: Documentar función
  distancia = ((distancia_dos - distancia_uno)/1000)
  velocidad = (distancia/(tiempo/3600))


  if (velocidad >= 1 and velocidad <= 20):
    texto_multa = "llamado de atención por baja velocidad"
  
  elif (velocidad >= 21 and velocidad <= 60):
    texto_multa = "Normal"
  
  elif (velocidad >= 61 and velocidad <= 80):
    texto_multa = "llamado de atención por alta velocidad"
  
  elif (velocidad >= 81 and velocidad <= 120):
    texto_multa = "Multa tipo I"

  elif velocidad > 120:
    texto_multa = "Multa tipo II e inmovilización del vehículo"

  else:
    texto_multa = "Datos inválidos"

  #TODO: Implementar función
  return texto_multa

def multar_alcoholemia(grado_alcohol):
#TODO: Documentar función

  if (grado_alcohol >= 20 and grado_alcohol <= 39):
    texto_multa = "Suspensión de la licencia de conducción entre seis (6) y doce (12) meses."

  elif (grado_alcohol >= 40 and grado_alcohol <= 99):
    texto_multa = "Suspensión de la Licencia de Conducción entre uno (1) y tres (3) años."

  elif (grado_alcohol >= 100 and grado_alcohol <= 149):
    texto_multa = "Suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas."

  elif (grado_alcohol >= 150):
    texto_multa = "Suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas."
  
  else:
    texto_multa = "El conductor no se encuentra en estado de embriaguez"

  #TODO: Implementar función
  return texto_multa