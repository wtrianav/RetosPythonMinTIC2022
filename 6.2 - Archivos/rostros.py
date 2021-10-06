
""" Modulo para el manejo de rostros de
    los habitantes del planeta ASCII
    Oscar Franco-Bedoya
    Junio 2-2021 """

#=====================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def cargar_rostros(archivo):
  fh = open(archivo)
  return fh

def imprimir_linea(codigo):
  # print(len(codigo))
  # print(codigo[0])
  # x = '9    W'
  # print(len(x))
  # print(x[0])
  # print(x[-1])
  # numero=int(len(codigo[0]))
  x = codigo[0]
  numero = int(x[0])
  # print(numero)
  caracter = x[-1]
  for i in range(0,numero):
    print(caracter,end="") 
  # caracter=codigo
  # print(caracter)
  # for i in codigo:

def imprimir_rostro(rostro):
  for linea_codigo in rostro: #recorre cada linea del rostro
    for codigo in linea_codigo: #recorre cada codigo de la linea
       #print(linea_codigo)
       #print(codigo)
       imprimir_linea(codigo) #imprime el caracter un numero de veces
    print("\n")


def calcular_estadisticas(rostros, ndia):
  rostro = []  #estructura para el rostro completo que esta formado por 5 lineas
  bandera = False
  for linea in rostros: # recorre el archivo
    # print(type(f'Tipo de linea {linea}'))
    # print(type(f'Tipo de linea {ndia}'))
    # print(len(linea))
    # print(len(ndia))
    # print(linea.isdigit())
    # if linea.isdigit()==True:
    if bandera == True:
      if linea == '---\n':
        imprimir_rostro(rostro)
        break
      codigos_linea= linea.rstrip().split(',') #obtiene la lista de codigos por cada linea
      linea = []
      for codigo in codigos_linea: #separa el numero del caracter 
        linea.append(codigo.split('\t')) 
      rostro.append(linea)
      

    if linea == ndia+'\n':
      # print (f"Si esta encontrando NDIA {linea}")
      # print(type(linea))
      bandera = True
      # imprimir_linea(linea)
    #print("\n")

  # rostros:[]
  return "No implementado"


      
    
      

