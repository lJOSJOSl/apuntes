###
# 03 - range()
# Permite crear una secuencia de numeros. Puede ser util para for, pero no solo para eso.
###

import os
os.system("cls")

print("\nrange():")

# nums = range(0, 5) #[0, 1, 2, 3, 4] (No es una lista)
# print(type(nums))

# print(type([1, 2, 3]))
# print(nums)

# Genera una secuencia de numeros del 0 al 9
# for num in nums:
#    print(num)

# range (inicio, fin)
# for num in range(5, 10):
#    print(num)

# range(inicio, fin, paso)
# for num in range(0, 10, 2):
#    print(num)

# for num in range(-5, 0):
#    print(num)

#for num in range(10, 0, -1):
#   print(num)

# nums = range(10)
# list_of_nums = list(nums)
# print(list_of_nums)

#Seria para hacerlo 5 veces
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

for _ in range(5):
    print("hacer 5 veces algo.")