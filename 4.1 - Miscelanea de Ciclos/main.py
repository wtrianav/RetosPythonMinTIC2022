import funciones_ciclos as func

# Validar el ejercicio de caida libre

# Y sin embargo se mueve
print("=============================================")
print("=========== ALTURA DEL EDIFICIO =============")
print("=============================================")

altura=int(input("Ingrese la altura del edificio en metros: "))
func.simulador_caida_libre(altura)

# Descendientes
print(" ")
print("=============================================")
print("============== DESCENDIENTES ================")
print("=============================================")

generacion_solicitada=int(input('Ingrese el número de la generación: '))
func.generador_generaciones(generacion_solicitada)

# Triangulares
print(" ")
print("=============================================")
print("=============== TRIANGULARES ================")
print("=============================================")

numero_pisos=int(input("Ingrese el número de pisos que tendrá el triangulo: "))
func.constructor_triangulos(numero_pisos)

# Tableros
print(" ")
print("=============================================")
print("================= TABLEROS ==================")
print("=============================================")

func.constructor_tableros("4x10")
