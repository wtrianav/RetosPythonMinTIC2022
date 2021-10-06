""" Programa ventas 
    Programa para el manejo de ventas por mes
    incorpora al modulo ventas.py
    Oscar Franco-Bedoya
    Junio 2-2021 """

    # Muy bien !!! Continue avanzando  . . .

#
#---------------- Zona librerias------------
import ventas as vt

M = [['Federico',23,18,11,20,10,15,12,10,18,25,16,17],
['Rodolfo',18,48,14,42,25,12,15,18,22,25,17,10],
['Pepe',30,20,15,35,25,10,18,25,23,15,18,20],
['Cleinisio',11,38,16,23,25,34,22,28,32,26,32,15],
['Rodrigo',26,34,20,42,25,25,35,33,28,18,16,19],
['Andrea',21,26,16,37,25,45,22,27,35,18,35,26],
['Gloria',11,36,26,34,22,25,28,22,30,18,35,42],
['Ana',32,22,15,12,23,32,21,22,33,52,25,22],
['Santiago',45,23,13,23,67,54,23,12,46,71,12,10],
['Conny',21,28,16,32,25,45,22,55,35,63,35,26],
['Angel',10,12,13,11,17,16,18,14,19,19,17,27],
['Juana',36,32,35,34,39,38,55,66,99,98,88,25]]

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

print("1. Empleados ordenados por ventas")
print("2. Cinco mejores vendedores")
print("3. Mes con mayores ventas y Gráfica de ventas al año")
opcion = int(input("Seleccione una opción: "))

ventas = vt.leer_ventas_empleados_mes(M)

if opcion == 1:
  vt.ordenar_vendedores_por_ventas(ventas)
elif opcion ==2:
  vt.calcular_cinco_vendedores(ventas)
elif opcion ==3:
  ventas_mes = vt.calcula_mes_mas_ventas(M, meses)
  vt.graficar_ventas_por_mes(meses,ventas_mes)
else:
  print('Opción no válida')
