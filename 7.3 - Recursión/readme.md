# Recursión
Este taller busca profundizar un poco mas sobre la estrategia recursiva.

# Sigueme para ver que hago

## Primera funcion
 Haga un seguimiento a la siguiente función, mostrando los valores parciales de n, depth y al final especifique que cree que calcula

```
def que_calculo(n, depth):
  if n == 1:
    return 1
  else:
    resultado = n * que_calculo(n-1, depth + 1)
    return result


depth=1
que_calculo(6, depth)
```

## Segunda funcion

```
def que_calculo_2(n):
  if n == 0:
    return 0
  else:
    return que_calculo_2(n-1) + n

que_calculo_2(6)
```
# Ultimo
Para terminar vamos a hacer un seguimiento a una función recursiva que maneja listas
```
def que_calculo_3(lst):
  if lst == []:
    return []
restr = que_calculo_3(lst[1:])
primero = lst[0:1]
resultado = restr + primero
return resultado

que_calculo_3([1,2,3,4])

```