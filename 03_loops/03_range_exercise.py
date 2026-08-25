###
# Ejercicios (range)
###

import os
os.system("cls")

# Ejercicio 1: Imprimir numeros del 1 al 10:
# Imprime los numeros del 1 al 10 inclusive usando un bucle for y range().

print("\nEjercicio 1:")

for _ in range(0,11):
    print(_)

# Ejercicio 2: Imprimir numeros impares del 1 al 20:
# Imprime todos los numeros impares entre 1 y 20 (inclusive) usando un bucle for y range().

print("\nEjercicio 2:")

for _ in range(1, 21, 2):
    print(_)

# Ejercicio 3: Imprimir los multiplos de 5
# Imprime los multiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().

print("\nEjercicio 3:")

for _ in range(5, 51, 5):
    print(_)

# Ejercicio 4: Imprimir numeros en orden inverso
# Imprime los numeros del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().

print("\nEjercicio 4:")

for _ in range(10, 0, -1):
    print(_)

# Ejercicio 5: Suma de numeros en un rango
# Calcula la suma de los numeros del 1 al 100 (inclusive) usando un bucle for y range().

print("\nEjercicio 5:")

for _ in range(1, 101):
    suma = 0
    suma += _
print(suma)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un numero.
# Imprime la tabla de multiplicar de ese numero (del 1 al 10) usando un bucle for y range().

print("\nEjercicio 6:")

numero = int(input("Ingresa un numero:"))
for _ in range(1, 11):
    print(f"{numero} x {_} = {numero*_}")