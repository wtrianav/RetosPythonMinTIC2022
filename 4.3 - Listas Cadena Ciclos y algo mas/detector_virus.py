print("")
print("===============================================")
print("============ DETECCIÓN DEL VIRUS ==============")
print("===============================================")
print("")

def detectar_virus(secuencias_geneticas):
  secuencia_virus='coronavirus'
  positivos=[]
  negativos=[]
  indice_virus=0

  for p in secuencias_geneticas:
    bandera=0
    indice=0
    indice_virus=0
    long = len(p)
    contador=0
    while indice <= long:
      while indice_virus <= 10: 
        if secuencia_virus[indice_virus] != p[indice]:
          indice_virus = indice_virus + 1 
        else:
          contador = contador + 1
          indice = indice + 1 
          if contador == long:
            positivos.append(p)
            bandera=1  
            break 

      indice = indice + 1 
    if bandera==0:
      negativos.append(p)
      
  print (f"positivos {positivos}")
  print (f"negativos {negativos}")
  
  return "" #positivos, negativos


#TODO: Todo