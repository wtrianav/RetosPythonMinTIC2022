import numpy as np

""" Modulo ModuleNotFoundError
    Funciones para el manejo de las lineas de metro
    con matrices
    Oscar Franco-Bedoya
    Mayo 10-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
conexiones = {1:[1,2], 2:[1,2,3,8,9], 3:[2,3,4], 4:[3,4,5,7], 5:[4,5,6,11], 6:[5,6,7,14], 7:[4,6,7,8], 8:[2,7,8], 9:[2,9,10,11], 10:[9,10], 11:[5,9,11,12,13], 12:[11,12], 13:[11,13,14], 14:[6,13,14]}

def leer_numero_estaciones():
   
  n = int(input("Ingrese la cantidad de estaciones: "))
  estaciones = np.array([[False]*n]*n)
  return estaciones,n

def leer_conexiones(numero_estaciones, estaciones):
  for codigo, conex in conexiones.items():
    if codigo <= numero_estaciones:
      for j in conex:
        if j <= numero_estaciones:
          # print(codigo,' - ', j)
          estaciones[codigo-1,j-1]=True
          estaciones[j-1,codigo-1]=True
  
  return estaciones
  
def obtener_lista_conexiones_estacion(matriz_conexiones,numero_estacion,n):
  estaciones_In = list()
  for i in range (0,n):
    # print(i)
    if ((i != numero_estacion-1) and (matriz_conexiones[numero_estacion-1][i] == True)):
      estaciones_In.append(i+1)
  return estaciones_In

def obtener_wstacion_mas_conectada(matriz_conexiones,n):
  con_estaciones = {}
  # con_estaciones = namedtuple('con_estaciones', ['estacion', 'cantidad'])
  for i in range (0,n):
    contador = 0
    for j in range (0,n):
      if ((i != j) and (matriz_conexiones[i][j] == True)):
        contador+=1
    #suma_con_estaciones = con_estaciones(i+1, contador)
    con_estaciones[i+1] = contador
  print(con_estaciones)

  x = sorted(con_estaciones.items(), key=lambda x: x[1], reverse=True)
  print(x)
  print(x[0])
  print(f'La estación con más conexiones es la: {x[0][0]} y tiene {x[0][1]} conexiones')


  #import operator
  #operator.itemgetter(1)
  

  return "No implementada aún"
