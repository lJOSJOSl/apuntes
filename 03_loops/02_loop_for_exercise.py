###
# Ejercicios for
###

import os
os.system("cls")

# Ejercicio 1: Imprimir numeros pares
# Imprime todos los numeros pares del 2 al 20 (inclusive) usando un bucle for.

print("\nEjercicio 1:")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in numeros:
    if i % 2 == 0:
        print(i) 
for x in range(2, 31):
    if x % 2 == 0:
        print(x)
# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de numeros:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los numeros usando un bucle for.

print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]
suma = 0
for i in numeros:
    suma += i
media = suma / len(numeros)
print(f"la media de la mista es: {media}")


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de numeros
# numeros = [15, 5, 25, 10, 20]
# encuentra el numero máximo en la lista usando un bucle for.

print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
mayor = 0
for i in numeros:
    if i > mayor:
        mayor = i
print(f"El numero maximo de la lista es: {mayor}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con mas de 5 letras
# usando un bucle for y list comprehension

print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]

palabra = [palabra for palabra in palabras if len(palabra)>5]
print(f"las palabras mayores a 5 letras son: {palabra}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduza una letra.
# Cuenta cuantas palabras en la lista empiezan con
# esa letra (sin diferenciar mayusculas/minusculas)

print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

letra = input("ingresa una letra: ").lower()
contador = 0

for palabra in palabras:
    if palabra[0] == letra:
        contador += 1
print(f"La cantidad de palabras que inician con {letra} es igual a: {contador}")