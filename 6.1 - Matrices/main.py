""" Programa lineas de metro
    Programa para el manejo de conexiones entre estaciones de metro
    incorpora al modulo rostros.py
    Oscar Franco-Bedoya
    Junio 2-2021 """

# Muy bien !!! Continue avanzando  . . .


#---------------- Zona librerias------------
import metro as mt



#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================


#-------------------------------------------------------
#recorrido_filas(M)
#print("------------------\t\n")
#recorrido_columnas(M)
estaciones,numero = mt.leer_numero_estaciones()
print(estaciones)
estaciones = mt.leer_conexiones(numero, estaciones)
print('------------------')
print(estaciones)

estacion = int(input('Digite la estación que desea consultar: '))
estaciones_conectadas = mt.obtener_lista_conexiones_estacion(estaciones, estacion, numero)
print(f'La estación {estacion} esta interconectada con las siguientes estaciones {estaciones_conectadas}')
mt.obtener_wstacion_mas_conectada(estaciones,numero)
