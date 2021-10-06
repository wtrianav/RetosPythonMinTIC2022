""" Modulo Ciclos
    Funciones para practicas con ciclos
    Oscar Franco-Bedoya
    Mayo 10-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def simulador_caida_libre (altura):
  #TODO Comentar código
  distancia = 0
  segundos = 1
  while (distancia+9.8)<=altura:
    distancia=(9.8*segundos)
    print(f'En el segundo {segundos} la distancia recorrida es:{round(distancia ,1)} y la altura actual es:{round(altura-distancia,1)} metros')
    segundos=segundos+1 ##segundos+=segundo
  print(f'En el segundo {segundos} la esfera recorre {round(altura-distancia ,1)} metros')
  #TODO Implementar la función
  return "No implementada aún"


def generador_generaciones(generacion):
  #TODO Comentar código
  contador=0
  numero_personas=0
  while contador<=generacion:
    personas_generacion=2**contador
    numero_personas=numero_personas+personas_generacion
    print(f'En la generacion {contador} el numero de personas es {personas_generacion}')
    contador=contador+1

  #TODO Implementar la función
  print(f'La cantidad de personas en la famila es: {numero_personas}')

def constructor_triangulos(pisos):
  cont=0
  for x in range(1,pisos+1):
    for y in range(1,x+1):
      cont=cont+1
      print(cont,end=" ")
    print(" ")
  #TODO Implementar la función
  return "No implementada aún"

def constructor_tableros(longitud):
  #TODO Comentar código
  indice=longitud.index('x')
  filas=int(longitud[0:indice])
  columnas=int(longitud[indice+1:len(longitud)])
  x=1
  while x<=filas:
    if x%2==0:
      band=1
    else:
      band=0
    imprimir_fila_uno(columnas,band)
    x=x+1

  #TODO Implementar la función
  return "No implementada aún"

def imprimir_fila_uno(columnas,band):
  cont=1
  cadena=""
  n=1
  while n<=3:
    while cont<=columnas:
      if band==0:
        cadena=cadena+"   "
        band=1
      else:
        cadena=cadena+"***"
        band=0
      cont=cont+1
    print(cadena)
    n=n+1
