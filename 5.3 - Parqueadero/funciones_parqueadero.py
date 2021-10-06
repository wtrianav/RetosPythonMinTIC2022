from collections import namedtuple
import stack_puestos as stack
import typing

Puesto = namedtuple('Puesto','nivel numero')

def crear_parqueadero(numero_niveles,cantidad_puestos):
  parqueadero=stack.Stack()
  cont_niveles=1
  while cont_niveles <= numero_niveles:
    cont_vehiculos=1
    while cont_vehiculos <= cantidad_puestos:
      parqueadero.push(Puesto(cont_niveles,cont_vehiculos))
      cont_vehiculos+=1
    cont_niveles+=1 
  return parqueadero

def obtener_puesto_libre(parqueadero):
  cant=parqueadero.length()
  if cant>0:

    puesto= parqueadero.top()
    parqueadero.pop()
    return puesto
  else:
    return None

def ingresar_puesto_libre(parqueadero,puesto):
  parqueadero.push(puesto)

def ocupar_puesto_parqueadero(placa,parqueadero,vehiculos_en_parqueadero): 
  if vehiculos_en_parqueadero.get(placa)==None:
    puesto_libre=obtener_puesto_libre(parqueadero)
    vehiculos_en_parqueadero[placa]=puesto_libre
    return placa,puesto_libre
  else:
    return None
 
def liberar_puesto_parqueadero(placa,parqueadero,vehiculos_en_parqueadero):
  if vehiculos_en_parqueadero.get(placa)!=None:
    puesto_libre=vehiculos_en_parqueadero[placa]
    del vehiculos_en_parqueadero[placa]
    ingresar_puesto_libre(parqueadero,puesto_libre)
    return "eliminado"
  else:
    return None


def dibujar_parqueadero(nivel_1, nivel_2,placa,accion) -> str:

 
  bandera=0
  if accion=="I":
    for n in reversed(nivel_2):
      #print(n)
      if nivel_2[n]=="|       ":
        nivel_2[n]="|" + placa
        bandera=1
        break
    if bandera==0:
      for n in reversed(nivel_1.keys()):
        if nivel_1[n]=="|       ":
          nivel_1[n]="|" + placa
          break
  else:
    for n in nivel_2:
      if nivel_2.get(n)== "|" + placa:
        nivel_2[n] = "|       "
        break
    for n in nivel_1:
      if nivel_1.get(n)=="|" + placa:
        nivel_1[n] = "|       "
        break

  lista1=""
  lista2=""
  for valor in nivel_2.keys(): 
    lista2=lista2 + " " + nivel_2[valor]
  for valor in nivel_1.keys(): 
    lista1=lista1 + " " + nivel_1[valor]

  
  print("")
  print("=============================================")
  print("Nivel 2 ", lista2)
  print("---------------------------------------------")
  print("Nivel 1 ", lista1)
  print("=============================================")
    

#====================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# ===================================================================

vehiculos_en_parqueadero=typing.Dict[str, str]
