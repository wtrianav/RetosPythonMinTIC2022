def crear_billetera():
  billetera = {"efectivo": 0,"monedas": 0}
  return billetera

def ingresar_efectivo(billetera,efectivo,monedas):
  billetera["efectivo"]+=efectivo
  billetera["monedas"]+=monedas

def retirar_efectivo(billetera,efectivo,monedas):
  if billetera["efectivo"]==0 and billetera["monedas"]==0:
    raise NameError("No tienes dinero")
    
  if (billetera["efectivo"] >= efectivo):
    billetera["efectivo"]-=efectivo
    if (billetera["monedas"] >= monedas):
      billetera["monedas"]-=monedas
    else:
      #monedas_restantes=billetera["monedas"]
      billetera["monedas"]=0
    return billetera["efectivo"], billetera["monedas"]
  
  #efectivo_restante=billetera["efectivo"]
  #monedas_restantes=billetera["monedas"]
  billetera["efectivo"]=0
  billetera["monedas"]=0

  return billetera["efectivo"], billetera["monedas"]
 
 
  






