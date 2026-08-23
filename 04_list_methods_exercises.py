### EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

import os
os.system("cls")

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los numeros del 1 al 5.
# Añade el numero 6 al final usando append().
# Inserta el numero 10 en la posicion: 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("\n Ejercicio 1:")
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, 10)
lista[0] = 0
print(lista)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del numero 1 en lista_a usando remove().
# Elimina el elemento en el indice 3 de lista_a usando pop.(). Imprime
# el elemento eliminado
# Limpia completamente lista_b usando clear().

print("\n Ejercicio 2:")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a)
eliminado = lista_a.pop(3)
print(eliminado)
print(lista_a)
print(lista_b)
lista_b.clear()
print(lista_b)

# Ejercicio 3: Slicing y eliminacion con del
# Crea una lista con los numeros del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el indice 2
# hasta el 5 (sin incluir el 5)
# Imprime la lista resultante.

print("\n Ejercicio 3:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[:2] + numeros[5:])
del numeros[2:5]
print(numeros)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes numeros [5, 2, 8, 1, 9, 4, 2]
# Ordena la lista de forma ascendente usando sort()
# Cuenta cuantas veces aparece el numero 2 en la lista usando count().
# Comprueba si el numero 6 esta en la lista usando in

print("\n Ejercicio 4:")
numeros = [5, 2, 8, 1, 9, 4, 2]
numeros.sort()
print(numeros)
print(numeros.count(2))
print(6 in numeros)


# Ejercicio 5 Copia vs Referencia
# Crea una lista llamada original con los numeros [1, 2, 3]
# Crea una copia de la lista original llamada copia_1 usando slicing
# Crea una otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia
# Modifica el primer elemento de la lista referenacia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2 referencia) y
# observa los cambios

print("\n Ejercicio 5:")
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()

referencia = original
referencia[0] = 10
print(original)
print(copia_1)
print(copia_2)
print(referencia)


# Ejercicio 6 Ordenar strings sin diferenciar mayusculas y minisculas
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayusculas y minusculas.

frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key=str.lower)
print(frutas)