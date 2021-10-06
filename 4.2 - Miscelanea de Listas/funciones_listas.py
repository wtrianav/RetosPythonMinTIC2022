""" Modulo Listas
    Funciones para practicas con listas
    Oscar Franco-Bedoya
    Mayo 10-2021 """
# Definición de Funciones
#=================================================
#  E S P A C I O  D E  T R A B A J O   A L U M N O
# ================================================

# Suma Acumulativa
def suma_acumulativa(lista_numeros):
  #TODO Comentar código
  sumatoria=0
  lista_acumulada=list()
  for i in lista_numeros:
    sumatoria=sumatoria + i
    lista_acumulada.append(sumatoria)
  print("la suma", lista_acumulada)
  #TODO Implementar la función
  return "No implementada aún"

# Traductor Pig Latin
def traductor_pig_latin(lista_palabras):
  #TODO Comentar código
  vocales=['a','e','i','o','u']
  consonantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
  lista_traducida=[]
  for palabra in lista_palabras:
    if palabra[0] in vocales:
      lista_traducida.append(palabra+"yay")
    elif palabra[0] in consonantes:
      letra=palabra[0]
      palabrax=palabra[1:]
      palabra=palabrax + letra + "ay"
      lista_traducida.append(palabra)
  return lista_traducida
   
# Vitamina A
def identificador_frutas(lista_frutas):
  newlist = []
  for x in lista_frutas:
   if "a" in x:
    newlist.append(x)
  #TODO Implementar la función
  return newlist

# Palindromes
def son_palindromos(frase):
  # Frase_1: Yo hago yoga hoy
  # Frase_2: Yo de todo te doy
  frase = str(frase).lower().replace(' ','')
  longitud = len(frase)
  if longitud % 2 == 0:
    izquierda = frase[:longitud // 2]
    derecha = frase[longitud // 2:]
    
  else:
    izquierda = frase[:longitud // 2]
    derecha = frase[longitud // 2 + 1:]
  

  #TODO Implementar la función
  return izquierda == derecha[::-1]

