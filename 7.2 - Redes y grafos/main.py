""" Programa grafos
  
    Oscar Franco-Bedoya
    Junio 2-2021 
"""


# Muy bien !!! Continue avanzando  . . .


import grafos as gr

def menu():
  print("""TALLER REDES Y GRAFOS
  1. Nodos y ejes
  2. Actores y Películas
  3. Desde cero""")
  opciones = int(input("Elige la opción que desees ejecutar: "))

  if opciones == 1:
    gr.nodos_ejes()

  if opciones == 2:
    gr.actores_peliculas()

  if opciones == 3:
    gr.desde_cero()

    
menu()