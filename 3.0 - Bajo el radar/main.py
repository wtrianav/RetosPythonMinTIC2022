""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import multas as mult

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
distancia_uno = float(input("Ingrese la distancia_uno en metros:\n"))

distancia_dos = float(input("Ingrese la distancia_dos en metros:\n"))

tiempo = int(input("Ingrese el tiempo en segundos:\n"))

multas = mult.multar_velocidad(distancia_uno, distancia_dos, tiempo)

print(multas)

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

if "Multa tipo" in multas:
  grados_alcohol = int(input("Al conductor con exceso de velocidad se le toma prueba de alcoholemia \nIngrese grados de alcohol:\n"))
  sancion = mult.multar_alcoholemia(grados_alcohol)
  print(sancion)