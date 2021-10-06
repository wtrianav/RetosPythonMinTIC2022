import manejo_billetera as bi 

# Poner un menu y ejemplos de ejecucion

# Muy bien !!! Continue avanzando  . . .

mi_billetera=bi.crear_billetera()
# print(mi_billetera)

bi.ingresar_efectivo(mi_billetera,310, 30)
print(mi_billetera)

v=bi.retirar_efectivo(mi_billetera,300, 50)
print(mi_billetera)
print(v)

v,w=bi.retirar_efectivo(mi_billetera,10, 5)
#print(v)
#print(w)
print(f"Mi billetera actualmentes tiene un saldo de {v} pesos en billetes y {w} pesos en monedas")