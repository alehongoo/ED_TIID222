#DECLARANDO ARREGLO
numeros=[10, 20, 30, 40, 50]

#IMPRIMIENDO ARREGLO
print(numeros[2])
#REASIGNANDO ARREGLO
numeros[2] = 35
print(numeros)
#AGREGAMOS UN NUEVO VALOR AL FINAL DEL ARREGLO
numeros.append(60)
print (numeros)
#ELIMINAMOS UN VALOR EN EL ARREGLO
numeros.remove(35)
print (numeros)
#ELIMINAMOS UN VALOR EN EL ARREGLO POR SU POSICION
numeros.pop(4)
print (numeros)

fruta = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]
fruta.pop(4)
print (fruta)

fruta.remove("Manzana")
print(fruta)