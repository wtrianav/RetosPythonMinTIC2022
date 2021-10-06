import matplotlib.pyplot as plt

# Definición de Funciones
#==================================================================
#      E S P A C I O    D E    T R A B A J O     A L U M N O
# ==================================================================

def leer_ventas_empleados_mes(M):
  ventas = {}

  for i in M:
    # print(i[0])
    suma = 0
    bandera = False
    for j in i:
      if bandera:
        # print(j)
        suma+=j
      bandera = True
    # print(suma)
    ventas[i[0]]=suma
    # ventas = {i[0]:suma}
  # print(ventas)
  return ventas

def ordenar_vendedores_por_ventas(ventas):
  ventas_ord = sorted(ventas.items(),key=lambda ventas_ord: ventas_ord[1], reverse=True)
  print('Los vendedores organizados de acuerdo a sus ventas de mayor a menor son:\n')
  for i in ventas_ord:
    print(f'{i[0]}: {i[1]}')
  
  return "No implementada aún"


def calcular_cinco_vendedores(ventas):
  ventas_ord = sorted(ventas.items(),key=lambda ventas_ord: ventas_ord[1], reverse=True)
  print('Los cinco mejores vendedores, organizados de acuerdo a sus ventas de mayor a menor, son:\n')
  cont=1
  for i in ventas_ord:
    if cont < 6: 
      print(f'{i[0]}: {i[1]}')
    cont+=1

  return "No implementada aún"

def calcula_mes_mas_ventas(M, meses):
  ventas_mes = {}
  cont = 1
  
  while cont <= 12:
    # print(i[0])
    suma = 0
    columna = [fila[cont] for fila in M]
    #print(columna)
    for i in columna:
      suma = suma + i
    ventas_mes[meses[cont-1]]=suma
    cont+=1
  print(f'Ventas al año por mes: ')
  for i,valor in ventas_mes.items():
    print(i, ':', valor)
    #print(f'{i[0]}: {i[1]}')
  #print(ventas_mes)
  
  ventas_mes_ord = sorted(ventas_mes.items(),key=lambda ventas_mes_ord: ventas_mes_ord[1], reverse=True)
  print('El mes con la venta mayor fue:\n')
  for i in ventas_mes_ord:
    print(f'{i[0]}: {i[1]}')
    break
  return ventas_mes

def graficar_ventas_por_mes(meses, ventas_mes):
  meses = list(ventas_mes.keys())
  valores = list(ventas_mes.values())
  plt.ylabel('Ventas por mes')
  plt.xlabel('Meses del año')
  plt.bar(meses,valores)
  plt.show()
  
  return "No implementada aún"

