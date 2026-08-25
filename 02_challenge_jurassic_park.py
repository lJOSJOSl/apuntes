'''
En Jurassic Park, se ha observado que los dinosaurios carnivoros, como el temible T-Rex, depositan un numero par
de huevos, imagina que tienes una lista de numeros enteros en la que cada numero representa la cantidad de
huevos puestos por dinosaurios en el parque

Importante: Solo se consideran los huevos de los dinosaurios carnivoros (T-Rex) aquellos que son numeros pares.

Objetivo:
Escribe una funcion en Python que reciba una lista de numeros enteros y devuelva la suma total de los huevos que
pertenecen a los dinosaurios carnivoros (es decir, la suma de todos los numeros pares en la lista).
'''

import os
os.system("cls")

a = [2, 2, 2, 1]

def pair(numeros):
    '''Recorre una lista y suma solo los numeros pares'''
    suma_pares = 0
    for i in numeros:
        if i % 2 == 0:
           suma_pares = suma_pares + i
    return suma_pares

#print(pair(a))
# Para ver si un numero es par siempre usamos el modulo % nos da el resto de la division: eggs % 2: == 2
def count_carnivore_dinosaur_eggs(egg_list) -> int:
    '''
    Esta funcion recibe una lista de numeros enteros que representan la cantidad de huebos que han puesto
    diferentes dinosaurios en el parque jurasico y los de numero par son carnivoros. Devuelve un numero con la
    suma de todos los huevos de carnivoros.
    '''

    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs

    return total_carnivore_eggs
print(count_carnivore_dinosaur_eggs(a))