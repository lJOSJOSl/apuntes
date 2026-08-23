###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# utilizando slicing y concatenacion, crea una nuevalista que contenga solo el mensaje "secreto"

import os
os.system("cls")

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
nuevo_mensaje = mensaje[7:]
print(nuevo_mensaje)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la ultima posicion utilizando sola la asignacion por indice

numeros = [10, 20, 30, 40, 50]
numeros[0] = 50
numeros[4] = 10
print(numeros)

numeros_2 = [10, 20, 30, 40, 50]
numeros_2[0], numeros_2[-1] = numeros_2[-1], numeros_2[0]
print(numeros_2)

# Ejercicio 3: El sandwich de listas
# Dadas las siguientes listas
# pan = ["pan arriba"]
# ingredientes = ["jamon", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el
# pan de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamon", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = []
sandwich = pan + ingredientes + pan_abajo
print(sandwich)
emparedado = pan + ingredientes + pan_abajo
print(emparedado, "e")
# Ejercicio 4: Duplicando la lista
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3]
nueva_lista = lista + lista
print(nueva_lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un numero impar de elementos, extrae el elemento que se encuentra
# en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])

print(lista[2:3])
print(lista[2])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y
# concatenación)
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado[3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6]
lista1 = lista[0:3:]
lista2 = lista[3:]
print(lista1[::-1] + lista2)
print(lista[:3][::-1] + lista[3:])

mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)