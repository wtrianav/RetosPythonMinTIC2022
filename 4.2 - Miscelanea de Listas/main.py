import funciones_listas as func

# Muy bien !!!

print("")
print("===============================================")
print("=================== M E N Ú ===================")
print("===============================================")
print("")
print("1. Suma acumulativa [3,5,6,8,9,4]")
print("2. Traductor Pig Latino")
print("3. Vitamina A")
print("4. Palindromos")
print("")
opcion = int(input("De anterior menú seleccione una opción: \n"))

if opcion == 1:
  # Suma acumulada
  lista=[]
  longitud=int(input("Ingrese la longitud de la lista:"))
  x=1
  while x<=longitud:
    datos=int(input(f"Ingrese el valor {x}:"))
    lista.append(datos)
    x=x+1
  print(lista)
  func.suma_acumulativa(lista)

if opcion == 2:
  # Traductor de español a Pig Latin
  palabras=[]
  longitud=int(input("Ingrese la longitud de la lista:"))
  x=1
  while x<=longitud:
    datos=str(input(f"Ingrese la palabra:"))
    palabras.append(datos)
    x=x+1
  print(palabras)

  nueva_lista=func.traductor_pig_latin(palabras)
  print(nueva_lista)

if opcion == 3:
  # Vitamina A
  frutas = []
  longitud = int(input('Ingrese la cantidad de frutas: ' '\n'))
  contador = 1
  while contador<= longitud:
    datos = str(input('Ingrese fruta en inglés: '))
    frutas.append(datos)
    contador = contador+1
  print(f"Las frutas que ingresaste son:{frutas}")
  nueva_lista = func.identificador_frutas(frutas)

  print(f"Las frutas que contienen vitamina A son:{nueva_lista}")

if opcion == 4:
  # Palindromos
  # Frase_1: Yo hago yoga hoy
  # Frase_2: Yo de todo te doy
  frase_1 = str(input("Ingrese la primera frase:\n"))
  frase_2 = str(input("Ingrese la segunda frase:\n"))

  palindromos_1 = func.son_palindromos(frase_1)
  palindromos_2 = func.son_palindromos(frase_2)
  print(f"¿La primera frase es palindrome?: {palindromos_1}")
  print(f"¿La segunda frase es palindrome?: {palindromos_2}")