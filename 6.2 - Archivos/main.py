""" Programa rostros#
    Programa para el manejo de rostros codificados 
    incorpora al modulo rostros.py
    Oscar Franco-Bedoya
    Junio 2-2021 """

# No funciona correctamente, favor validar

# Poner un menu y ejemplos de ejecucion


#---------------- Zona librerias------------
import rostros as rt

rostros = rt.cargar_rostros('rostros.txt')

ndia = input("Ingrese el número de identificación del asciiano: ")

rostro = rt.calcular_estadisticas(rostros, ndia)




