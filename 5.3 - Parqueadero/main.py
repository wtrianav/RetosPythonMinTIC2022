import funciones_parqueadero as parq
 
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejemplo de funcionamiento
nivel_2={"21":"|       ","22":"|       ","23":"|       ","24":"|       "}
nivel_1={"11":"|       ","12":"|       ","13":"|       ","14":"|       "}

accion=""
parq.dibujar_parqueadero(nivel_1, nivel_2,"       ",accion)
vehiculos_en_parqueadero={}
memo_park=parq.crear_parqueadero(2,4)
placa=""

while accion!="Q":
  accion = input("¿Que acción va a realizar?:\nI: Ingresar vehículo\nS: Sacar vehículo\n").upper()
  if accion.upper() in 'IS':
    placa_a=input("Digite la placa del vehículo: ").upper()
    placa=placa_a.upper().split("-")
    #print(placa[1])
    if placa[0].isalpha() and len(placa[0])==3 and placa[1].isdigit() and len(placa[1])==3:
      if accion.upper()=="I":
        print(placa_a)
        puesto_asignado=parq.ocupar_puesto_parqueadero(placa_a,memo_park,vehiculos_en_parqueadero)
        if puesto_asignado[1]==None:
          print("No hay espacios en el parqueadero")
        else:
          print("Puesto Asignado",puesto_asignado)
          parq.dibujar_parqueadero(nivel_1, nivel_2,placa_a,accion)
#          print(t)
    
      else:
        resultado=parq.liberar_puesto_parqueadero(placa_a,memo_park,vehiculos_en_parqueadero)
        if resultado=="eliminado": 
          print(f"El vehículo de placa {placa_a} salió del parqueadero ")
          parq.dibujar_parqueadero(nivel_1, nivel_2,placa_a,accion)
        else:
          print(f"El vehículo de placa {placa_a} no se encuentra en el  parqueadero ")
    else:
      print("placa no valida")
  else:
    if accion != "Q":
      print("Acción no válida")
