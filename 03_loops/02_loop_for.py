###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de codigo repetidamente mientras ITERA un iterable o una lista.
###

import os
os.system("cls")

print("\nBucle for:")

# Iterar una lista
frutas = ["manzana", "pera", "mandariina"]
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "josjos"
for caracter in cadena:
    print(caracter)

# enumerate()
# permite iterar sobre los elementos de un iterable y devolver un indice y el elemento:
frutas = ["manzana", "pera", "mandariina"]
for index, fruta in enumerate(frutas):
    print(f"El indice es {index} y la fruta es {fruta}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break
animales = ["perro", "gato", "pez", "loro", "pez", "canario", "raton"]
for idx, animal in enumerate(animales):
    if animal == "loro":
        print(f"El loro esta escondido en el {idx} de la lista.")
        break

# continue
animales = ["perro", "gato", "pez", "loro", "pez", "canario", "raton"]
for idx, animal in enumerate(animales):
    if animal == "loro": continue
    # continue
    print(animal)

# Comprension de listas (list comprehension)
animales = ["perro", "gato", "pez", "loro", "pez", "canario", "raton"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# muestra los numeros pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8,] if num % 2 == 0]
print(pares)