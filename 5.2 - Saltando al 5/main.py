""" Programa Saltando al 5
    Realiza codificación y decodificación 
    de mensajes
    incorpora al modulo csi.py
    Oscar Franco-Bedoya
    Mayo 20-2021 """

#---------------- Zona librerias------------
import csi as sh

mensaje = input("Ingrese el mensaje a codificar: \n")

#def codificar_mensaje(mensaje_original):
m = sh.codificar_mensaje(mensaje)
print(f"El texto codificado es: {m}""\n")

mensaje1 = input("\nIngrese el mensaje a decodificar: \n")

#def decodificar_mensaje(mensaje_codificado):
m1 = sh.decodificar_mensaje(mensaje1)
print(f"El texto decodificado es: {m1}")
