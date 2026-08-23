###
# 04 - Listas Métodos
# Los métodos mas importantes para trabajar con listas.
###

import os
os.system("cls")

# Añadir o insertar elementos a la lista

lista = [1, 2, 3, 4, 5]
lista.append(6) # Añade un elemento al final
print(lista)

lista.insert(2, 2.5) #Añade un elemento por indice
print(lista)

lista1 = ["a", "b", "c", "d"]   
lista1.insert(1, "@") # Inserta un elementos en la
# posicion que le indiques como primer argumento
print(lista1)

lista1.extend(["😍", "😍"]) # Puedes agregar varios elementos
# al final de la lista
print(lista1)

# Eliminar elementos de la lista

lista1.remove("@") # Remevue la primera aparicion de la cadea de texto
print(lista1)

# (lista).pop() elimina el ultimo elemento de la lista
# A no ser que le pases el indice
ultimo = lista1.pop() # Elimina y te devuelve
print(ultimo)
print(lista1)

lista1.pop(1) # Elimina el segundo de la lista(es el indice 1)
print(lista1)

# Eliminar
del lista1[-1]
print(lista1)

lista1.clear() # clear elimina todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ["🐼", "🐨", "🐶", "😿", "🐹"]
del lista1[3:]
print(lista1)

# Más métodos útiles
print("Ordenar listas modificando la original")
numbers = [3, 10, 2, 8, 99, 101]
print(numbers)
numbers.sort()
print(numbers)

print("Ordenar listas creando una copia")
numbers = [3, 10, 2, 8, 99, 101]

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
# Aunque los resultados son iguales sort no devuelve, modifica la lista original

print("Ordenar una lista de cadenas de texto (todo minuscula)")
frutas = ["manzana", "pera", "limon", "manzana", "pera", "limon"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezcla mayuscula y minuscula)")
frutas = ["manzana", "Pera", "Limon", "manzana", "pera", "limon"]
frutas.sort(key=str.lower)
print(frutas)

# Mas metodos utiles
animals = ["🐼", "🐶", "🐨", "🐶", "🐶", "🐶", "😿", "🐹"]
print(len(animals)) # Tamaño de la lista -> 8
print(animals.count("🐶")) # Cuantas veces aparece el "🐶" -> 4
print("🐨" in animals) # Comprueba si hay un "🐨" en la lista -> True
print("😺" in animals) # -> False