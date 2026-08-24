###
# EJERCICIOS
###

import os
os.system("cls")

# Ejercicio 1: Cuenta atrás
# Imprime los numeros del 10 al 1 usando un bucle while.

print("\nEjercicio 1:")

contador = 10

while contador > 0:
    print(contador)
    contador -= 1

# Ejercicio 2: Suma de numeros pares (while)
# Calcula la suma de los numeros pares entre 1 y 20 (inclusive) usando un bucle while.

print("\nEjercicio 2:")

contador = 1
suma = 0
while contador <= 20:
    if contador % 2 == 0:
        suma = suma + contador
    contador += 1
print(suma)

# Ejercicio 3: Factorial de un numero
# Pide al usuario que introduzca un numero entero positivo
# Calcula su factorial usando un bucle while
# El factorial de un numero entero positivo es el producto de todos los numeros del 1 a ese numero
# Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

print("\nEjercicio 3:")

numero = int(input("Ingresa un numero entero positivo: "))
iteracion = 1
factorial = 1

while iteracion < numero:
    factorial = factorial * (iteracion + 1)
    iteracion += 1
print(factorial) 

# Ejercicio 4: Validacion de contraseña
# Pide al usuario que introduzca una contraseña
# La contraseña debe tener al menos 8 caracteres
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos
# Si la contraseña es valida, imprime "Contraseña valida"

print("\nEjercicio 4:")


password = " "
while len(password) < 8:
    password = input("Ingresa una contaseña: ")
    if len(password) < 8:
        print("La contraseña tiene que tener mas de 8 caracteres")
else:
    print("Contraseña valida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número
# (del 1 al 10 usando un bucle while)

print("\nEjercicio 5:")

numero = int(input("ingresa un numero: "))
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1

# Ejercicio 6: Numeros primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

n = int(input("Ingrese: "))
numero = 2

while n >= numero:
    divisor =  2
    es_primo = True
    while divisor < numero:
        if numero % divisor == 0:
            es_primo = False
            break

        divisor += 1

    if es_primo:
        print(numero)
    numero += 1