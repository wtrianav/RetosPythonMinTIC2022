# Poner un menu y ejemplos de ejecucion

# Muy bien !!! Continue avanzando  . . .

# Es una función que calcula el número factorial de n
def que_calculo(n, depth):
  if n == 1:
    return 1
  else:
    resultado = n * que_calculo(n-1, depth + 1)
  return resultado

# Es una función que calcula la suma de n números
def que_calculo_2(n):
  if n == 0:
    return 0
  else:
    return que_calculo_2(n-1) + n

# Es una función que ordena una lista alrevés
def que_calculo_3(lst):
  if lst == []:
    return []
  restr = que_calculo_3(lst[1:])
  primero = lst[0:1]
  resultado = restr + primero
  return resultado

depth=1
print(que_calculo(7, depth))
print(que_calculo_2(5))
print(que_calculo_3([1,2,3,4]))