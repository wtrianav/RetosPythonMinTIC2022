""" Programa IoT#
    Realiza lel calculo de estadisticas de Una 
    Smarth Home
    incorpora al modulo smarth_home.py
    Oscar Franco-Bedoya
    Mayo 20-2021 """

#---------------- Zona librerias------------
import smarth_home as sh

dispositivos_hogar = "sensor,luces,ON@alarma,movimiento,OFF@sensor,humedad,OFF@electrico,tomas,OFF@electrico,nevera,ON@sensor,termometro,ON@alarma,puerta_principal,ON@electrico,home_theater,OFF@electrico,freidora_aire,ON@electrico,cafetera,ON@electrico,aire_acondicionado,ON@electrico,licuadora,OFF@alarma,puerta_garage,ON@electrico,persianas,OFF@electrico,camaras_vigilancia,ON@electrico,modem,ON@sensor,movimiento,ON"

IoT = sh.separar_cadenas(dispositivos_hogar)
contadorON,contadorOFF = sh.calcular_estadisticas(IoT)
print(contadorON)
print(contadorOFF)
