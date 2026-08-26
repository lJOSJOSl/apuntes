'''
Dado un array de numeros y un numero goal, encuentra los dos primeros numeros del array que sumen el numero goal
y devuelve sus indices. Si no existe la combinacion devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal) #[2, 3]
'''

import os
os.system("cls")

array = [4, 5, 6, 2]
goal = 8

def find_first_sum(nums, goal):
    for i in range(len(nums)):
        for n in range(i + 1, len(nums)):
            if nums[i] + nums[n] == goal:
                return [i, n]
    return None # No se encontro ninguna combinacion

resultado = find_first_sum(array, goal)
print(resultado)
