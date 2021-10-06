""" Programa para apoyar al marinero Seijo
    Oscar Franco-Bedoya
    Mayo 3-2021 """

import utilidades as util

def probar_funciones():
  criatura = util.aparecer_criatura()
  direccion = util.aparecer_direccion()
  return criatura, direccion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejecuta el programa varias veces para ver su funcionamiento

criatura, direccion = probar_funciones()
print(criatura, "y" ,direccion)

articulo = util.definir_articulo(criatura)
articulo_direccion = util.definir_articulo_posicion(direccion)

print("Ahoy! capitan,", articulo, criatura, articulo_direccion, direccion)



